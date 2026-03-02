from utils.servo import Servo

class Tail:
    """Subsystem for wagging the tail"""

    def __init__(self, pin: int):
        self.servo = Servo(pin)        
        self.queue = []

    def wag(self):
        """Wag the tail"""        
        self.servo.set_angle(30)
        self.servo.set_angle(210)
        self.servo.set_angle(30)
        self.servo.set_angle(210)

    def update(self):
        """Called every scheduler tick to update the servo position"""
        if self.servo._state == Servo.IDLE and self.queue:
            next_angle = self.queue.pop(0)
            self.servo.set_angle(next_angle)
        
        self.servo.update()

    def stop(self):
        """Stop everything in this subsystem immediately"""
        self.servo.stop()