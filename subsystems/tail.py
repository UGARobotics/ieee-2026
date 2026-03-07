import time

from utils.continuous_servo import ContinuousServo

class Tail:
    """Subsystem for wagging the tail"""

    TIME_PER_WAG = 3.2
    
    def __init__(self, pin=14):
        self.servo = ContinuousServo(pin)

    def wag(self, duration):
        """Wag the tail"""
        now = time.monotonic()
        end_time = now + duration
        self.servo.move(1.0)

        while time.monotonic() < end_time:
            yield

        self.servo.move(0.0)

    def backwag(self, duration):
        """Backwag the tail"""
        now = time.monotonic()
        end_time = now + duration
        self.servo.move(-1.0)

        while time.monotonic() < end_time:
            yield

        self.servo.move(0.0)

    def update(self):
        self.servo.update()

    def stop(self):
        """Stop everything in this subsystem immediately"""
        self.servo.stop()
