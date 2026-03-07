import RPi.GPIO as GPIO
import time

from utils.light_sensor import LightSensor


IDLE = 0 # will start off as IDLE
WAITING = 1 # IDLE -> WAITING when gpio input detected
RUNNING = 2 # when light is detected

class StartupSystem:
    """Subsystem for the startup system"""
    def __init__(self, pin=-1):
        # TODO: adjust pin number
        self.pin = pin
        self.state = StartupSystem.IDLE # starts as IDLE

        GPIO.setmode(GPIO.BCM) # GPIO num instead of actual pin num
        GPIO.setup(self.pin, GPIO.IN) # waiting for input
        
        # TODO: initialize light sensor here when we have it set up
        # self.light_sensor = LightSensor(pin)    

    def _is_high(self) -> bool:
        if GPIO.HIGH == 1:
            return True
        else:
            return False

    def update(self):
        if self.state == StartupSystem.IDLE and self._is_high(): # is high + idle -> waiting
            self.state = StartupSystem.WAITING
        elif self.state == StartupSystem.WAITING:
            pass
            # TODO: needs to check for status of light here
            # self.light_sensor.update()
            # if light_sensor detects light: WAITING -> RUNNING
        else:
            pass
            # Either not looking for light or already running, so do nothing

    def stop(self):
        GPIO.cleanup(self.pin)
