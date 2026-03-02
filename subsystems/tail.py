from utils.servo import Servo

class Tail:
    """Subsystem for wagging the tail"""

    def __init__(self, pin=17):
        self.servo = Servo(pin)        
        self.queue = []

    def wag(self):
        """Wag the tail"""        
        self.queue.append(30)
        self.queue.append(210)
        self.queue.append(30)
        self.queue.append(210)

    def update(self):
        """Called every scheduler tick to update the servo position"""
        if self.servo._state == Servo.IDLE and self.queue:
            next_angle = self.queue.pop(0)
            self.servo.set_angle(next_angle)
        
        self.servo.update()

    def stop(self):
        """Stop everything in this subsystem immediately"""
        self.servo.stop()