from utils.continuous_servo import ContinuousServo
from utils.positional_servo import PositionalServo

import time

class Intake:
    """Subsystem for the intake system"""
    def __init__(self, pins=[12, 16]):
        self.main_servo = ContinuousServo(pins[0])
        self.lift_servo = PositionalServo(pins[1], initial_angle=20, full_rotation_time=2.8)

    def intake(self, duration):
        """Start the intake"""
        now = time.monotonic()
        end_time = now + duration
        self.main_servo.move(1.0)

        while time.monotonic() < end_time:
            yield

        self.main_servo.move(0.0)
    
    def intake_slow(self, duration):
        """Start the intake"""
        now = time.monotonic()
        end_time = now + duration
        self.main_servo.move(0.2)

        while time.monotonic() < end_time:
            yield

        self.main_servo.move(0.0)

    def intake_while_lift(self, duration):
        """Start the intake while lifting"""
        now = time.monotonic()
        end_time = now + duration
        self.main_servo.move(0.5)
        self.lift_servo.set_angle(100)

        while time.monotonic() < end_time:
            yield

        self.main_servo.move(0.0)
    
    def outtake(self, duration):
        """Start the outtake"""
        now = time.monotonic()
        end_time = now + duration
        self.main_servo.move(-1.0)

        while time.monotonic() < end_time:
            yield

        self.main_servo.move(0.0)

    def lift(self):
        # TODO: fix angle
        self.lift_servo.set_angle(20)
        while self.lift_servo.state == PositionalServo.RUNNING:
            yield

    def drop(self):
        # TODO: fix angle
        self.lift_servo.set_angle(160)
        while self.lift_servo.state == PositionalServo.RUNNING:
            yield

    def stop(self):
        self.main_servo.stop()
        self.lift_servo.stop()
    
    def update(self):
        self.main_servo.update()
        self.lift_servo.update()
