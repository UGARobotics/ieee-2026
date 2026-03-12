import time

from smbus2 import SMBus
from collections import deque

class LightSensor:
    """Light sensor handler for I2C controlled light sensors with support for dual sensors"""
    
    UNDETECTED = 0  # no light detected
    DETECTED = 1    # light detected
    
    # VEML7700 Lux Sensor registers
    REG_ALS_CONF = 0x00      # Configuration register
    REG_ALS_DATA = 0x04      # ALS data register (ambient light level in lux)
    
    # TODO: adjust based on light sensitivity
    LIGHT_DETECTION_THRESHOLD = 100
    
    def __init__(
        self,
        bus: int = 1,
        address_primary: int = 0x10,
        address_secondary: int = 0x11,
        use_secondary: bool = False,
        window_size: int = 5
    ):
        """ Initialize light sensor """
        self.bus_num = bus
        self.address_primary = address_primary
        self.address_secondary = address_secondary
        self.address = address_secondary if use_secondary else address_primary
        self._bus = None
        
        self.state = self.UNDETECTED
        self.last_light_level = 0
        
        self.window_size = window_size
        self.readings_window = deque(maxlen=window_size)
        self.window_sum = 0
        self.averaged_light_level = 0
        
        # open bus
        self._bus = SMBus(self.bus_num)
        
    def switch_to_primary(self):
        """Switch to the primary sensor"""
        self.address = self.address_primary
    
    def switch_to_secondary(self):
        """Switch to the secondary sensor"""
        self.address = self.address_secondary
    
    def _read_light_level(self) -> int:
        """ Read ambient light level from VEML7700 ALS register """
        if not self._bus:
            raise RuntimeError("I2C bus not open")

        # Read 2 bytes from ALS_DATA register (0x04)
        # Returns 16-bit lux value
        data = self._bus.read_i2c_block_data(self.address, self.REG_ALS_DATA, 2)
        
        # Combine bytes: low byte first, then high byte
        light_level = (data[1] << 8) | data[0]
        return light_level
    
    def _update_sliding_window(self, new_reading: int):
        """ Sliding window helps filter the noise from false readings """
        # If window is full, subtract the value that will be removed
        if len(self.readings_window) == self.window_size:
            self.window_sum -= self.readings_window[0]
        
        # Add new reading
        self.readings_window.append(new_reading)
        self.window_sum += new_reading
        
        # Calculate average
        self.averaged_light_level = self.window_sum // len(self.readings_window)
    
    def update(self):
        """ Called every scheduler tick - reads light sensor, updates sliding window, and updates state """

        # Read raw sensor value
        self.last_light_level = self._read_light_level()
        
        # Update sliding window average
        self._update_sliding_window(self.last_light_level)
        
        # Determine state based on averaged value (filters noise)
        if self.averaged_light_level > self.LIGHT_DETECTION_THRESHOLD:
            self.state = self.DETECTED
        else:
            self.state = self.UNDETECTED
    
    def stop(self):
        """Stop the light sensor subsystem"""
        if self._bus:
            self._bus.close()




light_sensor = LightSensor(
    bus=1,
    address_primary=0x10,
    address_secondary=0x11,
    use_secondary=False
)

try:
    counter = 0
    while True:
        if counter % 100 == 0 and counter > 0:
            if light_sensor.address == 0x10:
                light_sensor.switch_to_secondary()
                print("Switched to secondary (0x11)")
            else:
                light_sensor.switch_to_primary()
                print("Switched to primary (0x10)")
        
        light_sensor.update()
        print(f"Address: 0x{light_sensor.address:02x} | Raw: {light_sensor.last_light_level} | Averaged: {light_sensor.averaged_light_level} | State: {light_sensor.state}")
        time.sleep(0.1)
        counter += 1
except KeyboardInterrupt:
    light_sensor.stop()
    print("Stopped")
