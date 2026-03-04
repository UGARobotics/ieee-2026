import RPi.GPIO as GPIO
import time

class ContinuousServo:
    """ A simple continuous servo wrapper class, specifically tuned for the specs with the 
    GoBilda 2000 series servos. """

    FREQUENCY = 50  # 50Hz servo frequency
    IDLE      = 0
    RUNNING   = 1

    def __init__(
            self,
            pin
    ):

        self.pin = pin
        self._command_state = None
        self._state = ContinuousServo.IDLE
    
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.FREQUENCY)
        self.pwm.start(0)

    def _set_command_state(self, state):
        self._command_state = state

    def _set_command_velocity(self, velocity):
        pulse = 1500 + (velocity / 1.0) * 1000
        duty = (pulse / 20000.0) * 100.0
        self._velocity = duty

    def move(self, velocity):        
        if velocity == 0.0:
            self._set_command_state(ContinuousServo.IDLE)
        else:
            self._set_command_velocity(velocity)
            self._set_command_state(ContinuousServo.RUNNING)

    def stop(self):
        self.pwm.stop()
        GPIO.cleanup(self.pin)

    def update(self):
        if self._command_state == ContinuousServo.IDLE:
            self.pwm.ChangeDutyCycle(0)
            self._state = ContinuousServo.IDLE
        else:
            self.pwm.ChangeDutyCycle(self._velocity)
            self._state = ContinuousServo.RUNNING
