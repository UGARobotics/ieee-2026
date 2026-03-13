import RPi.GPIO as GPIO
import time

from utils.light_sensor import LightSensor

class StartupSystem:
    """Subsystem for the startup system"""
    IDLE = 0 # will start off as IDLE
    WAITING = 1 # IDLE -> WAITING when gpio input detected
    RUNNING = 2 # when light is detected

    def __init__(self, pin=21):
        self.pin = pin
        self.state = StartupSystem.IDLE # starts as IDLE

        GPIO.setmode(GPIO.BCM) # GPIO num instead of actual pin num
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # waiting for input
        
        # Initialize I2C light sensor (primary address by default)
        self.light_sensor = LightSensor()    

    def _is_high(self) -> bool:
        pin_state = GPIO.input(self.pin)

        return pin_state == GPIO.HIGH

    def update(self):
        self.light_sensor.update()
        if self.state == StartupSystem.IDLE and self._is_high(): # is high + idle -> waiting

            # swap state if testing without light sensor
            # self.state = StartupSystem.RUNNING
            self.state = StartupSystem.WAITING
        elif self.state == StartupSystem.WAITING:
            # Check status of light sensor
            
            if self.light_sensor.state == LightSensor.DETECTED:
                self.state = StartupSystem.RUNNING
        else:
            # Either not looking for light or already running, so do nothing
            pass

    def stop(self):
        GPIO.cleanup(self.pin)
        self.light_sensor.stop()
