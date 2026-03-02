import RPi.GPIO as GPIO
import time

class PositionalServo:
    """ A simple positional servo wrapper class, specifically tuned for the specs with the 
    GoBilda 2000 series servos. """

    FREQUENCY = 50  # 50Hz servo frequency
    IDLE      = 0
    RUNNING   = 1

    def __init__(
            self,
            pin,
            initial_angle=0.0
    ):

        self.pin = pin
        self._end_time = 0.0
        self._angle = initial_angle
        self._state = PositionalServo.IDLE
    
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.FREQUENCY)
        self.pwm.start(0)

    def set_angle(self, angle):
        now = time.monotonic()
        self._end_time = now + 1.3  # we can adjust this duration as needed, current 1.3 seconds
        self._angle = angle
        
    def publish_angle(self, angle):
        # map 0–300° to 500–2500 µs
        pulse = 500 + (angle / 300.0) * 2000
        duty = (pulse / 20000.0) * 100.0
        self.pwm.ChangeDutyCycle(duty)
    
    def stop(self):
        self.pwm.stop()
        GPIO.cleanup(self.pin)

    def update(self):
        if time.monotonic() >= self._end_time:            
            self.pwm.ChangeDutyCycle(0)  # Stop the servo
            self._state = PositionalServo.IDLE
        else:
            self.publish_angle(self._angle)
            self._state = PositionalServo.RUNNING
