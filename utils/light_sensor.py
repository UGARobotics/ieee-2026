import board
import adafruit_veml7700

from collections import deque
 
class LightSensor:
    """Light sensor handler for I2C controlled light sensors with support for dual sensors"""
    
    UNDETECTED = 0  # no light detected
    DETECTED = 1    # light detected
    
    
    LIGHT_DETECTION_THRESHOLD = 1100
    
    def __init__(
        self,
        window_size: int = 5
    ):
        """ Initialize light sensor """

        self.state = self.UNDETECTED
        self.last_light_level = 0
        
        self.window_size = window_size
        self.readings_window = deque(maxlen=window_size)
        self.window_sum = 0
        self.averaged_light_level = 0

        self.i2c = board.I2C()
        self._sensor = adafruit_veml7700.VEML7700(self.i2c)
        
    def _read_light_level(self) -> int:
        """ Read ambient light level from VEML7700 ALS register """
        return self._sensor.light_level
    
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
