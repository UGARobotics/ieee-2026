from subsystems.startup_system import StartupSystem

from utils.positional_servo import PositionalServo

class ButtonPresser:
    """Subsystem for the button pressing mechanism"""

    def __init__(self, pin=20, startup_system: StartupSystem):
        self.servo = PositionalServo(pin, full_rotation_time = 3.8, initial_angle=280)
        self.startup_system = startup_system

    def press_fourth(self):
        self.servo.set_angle(145)
        while self.servo.state == PositionalServo.RUNNING:
            yield

    def press_third(self):
        self.servo.set_angle(155)
        while self.servo.state == PositionalServo.RUNNING:
            yield

    def press_second(self):
        self.servo.set_angle(168)
        while self.servo.state == PositionalServo.RUNNING:
            yield

    def press_first(self):
        self.servo.set_angle(178)
        while self.servo.state == PositionalServo.RUNNING:
            yield
    
    def unpress(self):
        self.servo.set_angle(135)
        while self.servo.state == PositionalServo.RUNNING:
            yield

    def dogoff(self):
        self.servo.set_angle(160)
        while self.servo.state == PositionalServo.RUNNING:
            yield

    def reset(self):
        self.servo.set_angle(280)
        while self.servo.state == PositionalServo.RUNNING:
            yield

    def stop(self):
        self.servo.stop()

    def update(self):
        if self.startup_system.state == StartupSystem.WAITING:
            pass

        self.servo.update()
