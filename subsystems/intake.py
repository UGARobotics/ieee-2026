from phoenix6.hardware.canrange import CANrange

from subsystems.startup_system import StartupSystem

from utils.continuous_servo import ContinuousServo
from utils.positional_servo import PositionalServo

from collections import deque

import time

class Intake:
    """Subsystem for the intake system"""

    NOT_DETECTED_DUCK = 0
    DETECTED_DUCK = 1
    
    def __init__(
            self,
            pins=[12, 16],
            canivore="Main",
            startup_system: StartupSystem = None,
            tof_window_size: int = 5
    ):
        self.main_servo = ContinuousServo(pins[0])
        self.lift_servo = PositionalServo(pins[1], initial_angle=20, full_rotation_time=2.8)
        self.tof = CANrange(0, canivore)
        self.startup_system = startup_system

        self.duck_state = Intake.NOT_DETECTED_DUCK
        
        # Sliding window for TOF distance averaging
        self.tof_window_size = tof_window_size
        self.tof_readings_window = deque(maxlen=tof_window_size)
        self.tof_window_sum = 0
        self.tof_averaged_distance = 0
        self.tof_last_distance = 0

        self.ctr = 0

    def intake(self, duration):
        """Start the intake"""
        now = time.monotonic()
        end_time = now + duration
        self.main_servo.move(-1.0)
 
        while time.monotonic() < end_time:
            yield

        self.main_servo.move(0.0)
    
    def intake_slow(self, duration):
        """Start the intake"""
        now = time.monotonic()
        end_time = now + duration
        self.main_servo.move(-0.2)

        while time.monotonic() < end_time:
            yield

        self.main_servo.move(0.0)

    def intake_while_lift(self, duration):
        """Start the intake while lifting"""
        now = time.monotonic()
        end_time = now + duration
        self.main_servo.move(-0.5)
        self.lift_servo.set_angle(0)

        while time.monotonic() < end_time:
            yield

        self.main_servo.move(0.0)

    def seek(self, duration):
        """Start the intake while lifting"""
        now = time.monotonic()
        end_time = now + duration
        self.main_servo.move(-1.0)
        self.lift_servo.set_angle(130)

        while time.monotonic() < end_time:
            yield

        self.main_servo.move(0.0)

    def intake_while_drop(self, duration):
        """Start the intake while lifting"""
        now = time.monotonic()
        end_time = now + duration
        self.main_servo.move(-1.0)
        self.lift_servo.set_angle(150)

        while time.monotonic() < end_time:
            yield

        self.main_servo.move(0.0)
    
    def outtake(self, duration):
        """Start the outtake"""
        now = time.monotonic()
        end_time = now + duration
        self.main_servo.move(1.0)

        while time.monotonic() < end_time:
            yield

        self.main_servo.move(0.0)

    def lift(self):
        self.lift_servo.set_angle(0)
        while self.lift_servo.state == PositionalServo.RUNNING:
            yield

    def drop(self):
        self.lift_servo.set_angle(150)
        while self.lift_servo.state == PositionalServo.RUNNING:
            yield
            
    def drop_outtake_height(self):
        self.lift_servo.set_angle(100)
        while self.lift_servo.state == PositionalServo.RUNNING:
            yield
            
    def stop(self):
        self.main_servo.stop()
        self.lift_servo.stop()
    
    def _update_tof_sliding_window(self, new_reading: float):
        """Update sliding window average for TOF readings"""
        # If window is full, subtract the value that will be removed
        if len(self.tof_readings_window) == self.tof_window_size:
            self.tof_window_sum -= self.tof_readings_window[0]
        
        # Add new reading
        self.tof_readings_window.append(new_reading)
        self.tof_window_sum += new_reading
        
        # Calculate average
        self.tof_averaged_distance = self.tof_window_sum / len(self.tof_readings_window)
    
    def update(self):
        if self.startup_system.state == StartupSystem.WAITING:
            pass

        self.main_servo.update()
        self.lift_servo.update()

        # Get and average TOF distance
        self.tof_last_distance = self.tof.get_distance().value
        self._update_tof_sliding_window(self.tof_last_distance)

        if self.tof_averaged_distance < 0.13:
            self.duck_state = Intake.DETECTED_DUCK
        else:
            self.duck_state = Intake.NOT_DETECTED_DUCK

