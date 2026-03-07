import RPi.GPIO as GPIO
import time

DETECTED = 0 # light detected
UNDETECTED = 1 # no light detected

class LightSensor:
    """
    Subsystem for light sensor - wip since not hooked up
    """
    def __init__(
            self, 
            pin,
    ):
        
        self.pin = pin
        self.state = None

    def stop(self):
      pass

    
    def update(self): 
        pass