from utils.positional_servo import PositionalServo

class ButtonPresser:
    """Subsystem for the button pressing mechanism"""

    def __init__(self, pin=15):
        self.servo = PositionalServo(pin, full_rotation_time = 5)

    def press(self):
        self.servo.set_angle(140)
        while self.servo.state == PositionalServo.RUNNING:
            print("here")
            yield
    
    def unpress(self):
        self.servo.set_angle(100)
        while self.servo.state == PositionalServo.RUNNING:
            yield

    def stop(self):
        self.servo.stop()

    def update(self):
        self.servo.update()
