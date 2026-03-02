from utils.servo import Servo

class Tail:
    """Subsystem for wagging the tail"""

    def __init__(self, pin: int):
        self.servo = Servo(pin)

    def wag(self):
        """Wag the tail"""

        self.servo.set_angle(30)
        self.servo.set_angle(210)
        self.servo.set_angle(30)
        self.servo.set_angle(210)

    def update(self):
        """Called every scheduler tick to update the servo position"""
        self.servo.update()

    def stop(self):
        """Stop everything in this subsystem immediately"""
        self.servo.stop()