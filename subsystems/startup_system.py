import RPi.GPIO as GPIO
import time

from utils.light_sensor import LightSensor


IDLE = 1 # will start off as IDLE
RUNNING = 2 # when light is detected
WAITING = 3 # IDLE -> WAITING when gpio input detected

class StartupSystem:
    """Subsystem for the startup system"""
    def __init__(self, pin=-1): # dummy pin num rn
        self.pin = pin
        self._command_state = StartupSystem.IDLE # starts as IDLE

        GPIO.setmode(GPIO.BCM) # GPIO num instead of actual pin num
        GPIO.setup(self.pin, GPIO.IN) # waiting for input
        
        self.light_sensor = LightSensor(pin)    

    def _set_command_set(self, state):
        self._set_command_state = state

    def _is_high(self) -> bool:
        if GPIO.HIGH == 1 and self._set_command_state == StartupSystem.IDLE:
            return True
        else:
            return False

    def update(self):
        if self._is_high(): # is high + idle -> waiting
            self._command_state = StartupSystem.WAITING

        elif self._command_state == StartupSystem.WAITING:
            pass
            # needs to check for status of light here
            # self.light_sensor.update()
            # if light_sensor detects light: WAITING -> RUNNING

    def stop(self):
        self._set_command_state(StartupSystem.IDLE) # idk
        GPIO.cleanup(self.pin)