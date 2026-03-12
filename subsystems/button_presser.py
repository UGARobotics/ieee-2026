from utils.positional_servo import PositionalServo

class ButtonPresser:
    """Subsystem for the button pressing mechanism"""

    def __init__(self, pin=20):
        self.servo = PositionalServo(pin, full_rotation_time = 4.2, initial_angle=280)

    def press(self):
        self.servo.set_angle(155)
        while self.servo.state == PositionalServo.RUNNING:
            yield
    
    def unpress(self):
        self.servo.set_angle(140)
        while self.servo.state == PositionalServo.RUNNING:
            yield

    def stop(self):
        self.servo.stop()

    def update(self):
        self.servo.update()
