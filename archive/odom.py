from __future__ import annotations

from dataclasses import dataclass
import struct
import time
from typing import Optional

from smbus2 import SMBus, i2c_msg

I2C_ADDR_DEFAULT = 0x31

class PinpointI2CError(RuntimeError):
	pass

@dataclass(frozen=True)
class Pose2D:
	x: float
	y: float
	h: float

@dataclass(frozen=True)
class BulkRead:
	status: int
	loop_time_us: int
	enc_x: int
	enc_y: int
	pos: Pose2D
	vel: Pose2D

class PinpointI2C:
	# Register addresses
	REG_DEVICE_ID = 1
	REG_DEVICE_VER = 2
	REG_DEVICE_STAT = 3
	REG_DEVICE_CTRL = 4
	REG_LOOP_TIME = 5
	REG_X_ENCODER = 6
	REG_Y_ENCODER = 7
	REG_X_POS = 8
	REG_Y_POS = 9
	REG_H_ORIENT = 10
	REG_X_VEL = 11
	REG_Y_VEL = 12
	REG_H_VEL = 13
	REG_TICKS_PER_MM = 14
	REG_X_OFFSET = 15
	REG_Y_OFFSET = 16
	REG_YAW_SCALAR = 17
	REG_BULK_READ = 18
	
	# Status bits
	STATUS_READY = 1 << 0
	STATUS_CALIBRATING = 1 << 1
	STATUS_X_MISSING = 1 << 2
	STATUS_Y_MISSING = 1 << 3
	
	# Control bits
	CTRL_RESET_IMU = 1 << 0
	CTRL_RESET_IMU_AND_POS = 1 << 1
	CTRL_SET_Y_REV = 1 << 2
	CTRL_SET_Y_FWD = 1 << 3
	CTRL_SET_X_REV = 1 << 4
	CTRL_SET_X_FWD = 1 << 5
	
	def __init__(
		self,
		bus: int = 1,
		address: int = I2C_ADDR_DEFAULT,
		init_on_open: bool = True,
		init_timeout_s: float = 2.0,
		poll_interval_s: float = 0.02,
		reset_on_init: bool = True,
		verbose: bool = False,
		ticks_per_mm: float | None = None,
		x_offset: float = 0.0,
		y_offset: float = 0.0,
		yaw_scalar: float = 1.0
	):
		self.bus_num = bus
		self.address = address
		self._bus = None
		
		self.init_on_open = init_on_open
		self.init_timeout_s = init_timeout_s
		self.poll_interval_s = poll_interval_s
		self.reset_on_init = reset_on_init
		self.verbose = verbose
		
		self.ticks_per_mm = ticks_per_mm
		self.x_offset = x_offset
		self.y_offset = y_offset
		self.yaw_scalar = yaw_scalar
	
	def __enter__(self) -> "PinpointI2C":
		self._bus = SMBus(self.bus_num)
		if self.init_on_open:
			self.initialize(
				timeout_s=self.init_timeout_s,
				poll_interval_s=self.poll_interval_s,
				reset=self.reset_on_init,
				verbose=self.verbose,
				ticks_per_mm=self.ticks_per_mm,
				x_offset=self.x_offset,
				y_offset=self.y_offset,
				yaw_scalar=self.yaw_scalar
			)
		return self
	
	def initialize(
		self,
		timeout_s: float = 2.0,
		poll_interval_s: float = 0.02,
		reset: bool = True,
		verbose: bool = False,
		ticks_per_mm: float | None = None,
		x_offset: float = 0.0,
		y_offset: float = 0.0,
		yaw_scalar: float = 1.0
	) -> None:
		if self.ticks_per_mm is None:
			raise PinpointI2CError("ticks_per_mm must be provided to PinpointI2C()")			

		if verbose:
			print(f"[odom] init: addr=0x{self.address:02X} bus={self.bus_num}")
		
		time.sleep(0.1)
		self.check_identity()
		
		status = self.read_status()
		if verbose:
			print(f"[odom] status (pre): {self._decode_status(status)}")
		
		if status & self.STATUS_X_MISSING:
			raise PinpointI2CError("X odometry pod not detected")
		if status & self.STATUS_Y_MISSING:
			raise PinpointI2CError("Y odometry pod not detected")
		
		# Wait ready before commands
		self._wait_ready(timeout_s=timeout_s, poll_interval_s=poll_interval_s, verbose=verbose)
		
		if reset:
			if verbose:
				print("[odom] issuing reset IMU+position")
			self.reset_imu_and_pos()
			self._wait_ready(timeout_s=timeout_s, poll_interval_s=poll_interval_s, verbose=verbose)
		
		if verbose:
			print(f"[odom] setting ticks/mm = {self.ticks_per_mm}")
		self.set_ticks_per_mm(self.ticks_per_mm)

		if verbose and (self.x_offset != 0.0 or self.y_offset != 0.0):
			print(
				f"[odom] setting pod offsets: "
				f"x={self.x_offset}, y={self.y_offset}"
			)
		self.set_pod_offsets(self.x_offset, self.y_offset)

		if verbose and self.yaw_scalar != 1.0:
			print(f"[odom] setting yaw scalar = {self.yaw_scalar}")
		self.set_yaw_scalar(self.yaw_scalar)
		
		if verbose:
			final = self.read_status()
			print(f"[odom] init complete: {self._decode_status(final)}")
	
	def _wait_ready(self, timeout_s: float, poll_interval_s: float, verbose: bool = False) -> None:
		deadline = time.monotonic() + timeout_s
		last_status = None
		next_log = 0.0
		
		stable_needed = 3
		stable = 0
		
		while time.monotonic() < deadline:
			last_status = self.read_status()
			
			if (last_status & ~0x0F) != 0:
				stable = 0
				if verbose:
					now = time.monotonic()
					if now >= next_log:
						next_log = now + 0.2
						print(f"[odom] waiting: invalud status 0x{last_status:08x} (ignoring)")
				time.sleep(poll_interval_s)
				continue
			
			# Fail if lose pods
			if last_status & self.STATUS_X_MISSING:
				raise PinpointI2CError("X odometry pod not detected")
			if last_status & self.STATUS_Y_MISSING:
				raise PinpointI2CError("Y odometry pod not detected")
			
			ready = bool(last_status & self.STATUS_READY)
			calibrating = bool(last_status & self.STATUS_CALIBRATING)
			
			if ready and not calibrating:
				stable += 1
				if stable >= stable_needed:
					if verbose:
						print(f"[odom] ready: {self._decode_status(last_status)} (stable x{stable_needed})")
					return
			else:
				stable = 0
			
			if verbose:
				now = time.monotonic()
				if now >= next_log:
					next_log = now + 0.2
					print(f"[odom] waiting: {self._decode_status(last_status)}")
			
			time.sleep(poll_interval_s)
		
		# timeout
		raise PinpointI2CError(f"Timed out waiting for ready after {timeout_s:.2f}s")
	
	def _decode_status(self, status: int) -> str:
		parts = [f"0x{status:08x}"]
		parts.append("READY" if (status & self.STATUS_READY) else "NOT_READY")
		if status & self.STATUS_CALIBRATING:
			parts.append("CALIBRATING")
		if status & self.STATUS_X_MISSING:
			parts.append("X_MISSING")
		if status & self.STATUS_Y_MISSING:
			parts.append("y_MISSING")
		return "|".join(parts)

	def __exit__(self, exc_type, exc, tb) -> None:
		bus = self._bus
		self._bus = None
		if bus is not None:
			bus.close()
	
	@property
	def bus(self) -> SMBus:
		if self._bus is None:
			raise PinpointI2CError("Bus not open.")
		return self._bus
	
	# I2C Helpers
	def _read_bytes(self, reg: int, n: int) -> bytes:
		# Write register address (STOP after this)
		self.bus.write_byte(self.address, reg & 0xFF)

		# Now do a plain read
		data = self.bus.read_i2c_block_data(self.address, 0, n)
		return bytes(data)
	
	def _write_bytes(self, reg: int, data: bytes) -> None:
		self.bus.write_i2c_block_data(self.address, reg & 0xFF, list(data))
	
	def _read_u32(self, reg: int) -> int:
		raw = self._read_bytes(reg, 4)
		return struct.unpack("<I", raw)[0]
	
	def _write_u32(self, reg: int, value: int) -> None:
		self._write_bytes(reg, struct.pack("<I", value & 0xFFFFFFFF))
	
	def _read_f32(self, reg: int) -> float:
		raw = self._read_bytes(reg, 4)
		return struct.unpack("<f", raw)[0]
	
	def _write_f32(self, reg: int, value: float) -> None:
		self._write_bytes(reg, struct.pack("<f", float(value)))
	
	# API
	def check_identity(self) -> None:
		dev_id = self._read_u32(self.REG_DEVICE_ID)
		if dev_id != 2:
			raise PinpointI2CError(f"Unexpected Device ID {dev_id} (expected 2)")
	
	def read_status(self) -> int:
		return self._read_u32(self.REG_DEVICE_STAT)
	
	def is_ready(self) -> bool:
		return bool(self.read_status() & self.STATUS_READY)
	
	def reset_imu(self) -> None:
		self._write_u32(self.REG_DEVICE_CTRL, self.CTRL_RESET_IMU)
	
	def reset_imu_and_pos(self) -> None:
		self._write_u32(self.REG_DEVICE_CTRL, self.CTRL_RESET_IMU_AND_POS)
	
	def set_encoder_directions(self, x_reversed: bool, y_reversed: bool) -> None:
		cmd = 0
		cmd |= self.CTRL_SET_X_REV if x_reversed else self.CTRL_SET_X_FWD
		cmd |= self.CTRL_SET_Y_REV if y_reversed else self.CTRL_SET_Y_FWD
		self._write_u32(self.REG_DEVICE_CTRL, cmd)
	
	def set_ticks_per_mm(self, ticks_per_mm: float) -> None:
		self._write_f32(self.REG_TICKS_PER_MM, ticks_per_mm)
	
	def set_pod_offsets(self, x_offset: float, y_offset: float) -> None:
		self._write_f32(self.REG_X_OFFSET, x_offset)
		self._write_f32(self.REG_Y_OFFSET, y_offset)
	
	def set_yaw_scalar(self, yaw_scalar: float) -> None:
		self._write_f32(self.REG_YAW_SCALAR, yaw_scalar)
	
	def read_raw_encoders(self) -> tuple[int, int]:
		x = self._read_u32(self.REG_X_ENCODER)
		y = self._read_u32(self.REG_Y_ENCODER)
		
		return x, y
	
	def read_pose(self) -> Pose2D:
		x = self._read_f32(self.REG_X_POS)
		y = self._read_f32(self.REG_Y_POS)
		h = self._read_f32(self.REG_H_ORIENT)
		return Pose2D(x=x, y=y, h=h)
	
	def read_velocity(self) -> Pose2D:
		vx = self._read_f32(self.REG_X_VEL)
		vy = self._read_f32(self.REG_Y_VEL)
		vh = self._read_f32(self.REG_H_VEL)
		return Pose2D(x=vx, y=vy, h=vh)
	
	def read_bulk(self) -> BulkRead:
		self.bus.write_byte(self.address, self.REG_BULK_READ)

		part1 = self.bus.read_i2c_block_data(self.address, 0, 32)
		part2 = self.bus.read_i2c_block_data(self.address, 0, 8)

		raw = bytes(part1 + part2)

		(status, loop_time, enc_x, enc_y,
		 x, y, h, vx, vy, vh) = struct.unpack("<IIIIffffff", raw)

		return BulkRead(
			status=status,
			loop_time_us=loop_time,
			enc_x=enc_x,
			enc_y=enc_y,
			pos=Pose2D(x=x, y=y, h=h),
			vel=Pose2D(x=vx, y=vy, h=vh),
		)

