from utils.positional_servo import PositionalServo

class ButtonPresser:
    """Subsystem for the button pressing mechanism"""

    def __init__(self, pin=15):
        self.servo = PositionalServo(pin, full_rotation_time = 3.0, initial_angle=210)

    def press(self):
        # TODO: adjust angle
        self.servo.set_angle(160)
        while self.servo.state == PositionalServo.RUNNING:
            yield
    
    def unpress(self):
        # TODO: adjust angle
        self.servo.set_angle(210)
        while self.servo.state == PositionalServo.RUNNING:
            yield

    def stop(self):
        self.servo.stop()

    def update(self):
        self.servo.update()
