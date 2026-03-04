import time

from utils.motor import Motor
from subsystems.odometry import Odometry

class Drivetrain:
    SLIP            = 0.12              # Adjust value for testing

    def __init__(self, motors: list[Motor], odometry: Odometry = None):
        # in order of front left, front right, back left, back right
        self.motors = motors
        self.odometry = odometry

    def go_forward(self, distance):
        _, y, _ = self.odometry.get_position()
        target_y = y + distance

        self.motors[0].move(15)
        self.motors[1].move(-15)
        self.motors[2].move(15)
        self.motors[3].move(-15)

        while abs(target_y - y) > self.SLIP:
            _, y, _ = self.odometry.get_position()
            print(abs(target_y - y))
            yield        

        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()


    def go_backward(self, distance):
        _, y, _ = self.odometry.get_position()
        target_y = y - distance

        self.motors[0].move(-15)
        self.motors[1].move(15)
        self.motors[2].move(-15)
        self.motors[3].move(15)

        while abs(y - target_y) > self.SLIP:
            _, y, _ = self.odometry.get_position()
            print(abs(y-target_y))
            yield        

        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()

    def strafe_left(self, distance):
        
        x, _, _ = self.odometry.get_position()
        target_x = x - distance

        self.motors[0].move(15)
        self.motors[1].move(15)
        self.motors[2].move(-15)
        self.motors[3].move(-15)

        while abs(x - target_x) > self.SLIP:
            x, _, _ = self.odometry.get_position()
            print(abs(x - target_x))
            yield
        
        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()

    def strafe_right(self, distance):
        
        x, _, _ = self.odometry.get_position()
        target_x = x + distance

        self.motors[0].move(-15)
        self.motors[1].move(-15)
        self.motors[2].move(15)
        self.motors[3].move(15)

        while abs(x - target_x) > self.SLIP:
            x, _, _ = self.odometry.get_position()
            print(abs(x - target_x))
            yield
        
        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()

    def turn_left(self, duration):
        
        self.motors[0].move(-5)
        self.motors[1].move(-5)
        self.motors[2].move(-5)
        self.motors[3].move(-5)

        now = time.monotonic()
        end_time = now + duration

        while time.monotonic() <= end_time:
            yield
        
        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()


    def turn_right(self, duration):
        
        self.motors[0].move(5)
        self.motors[1].move(5)
        self.motors[2].move(5)
        self.motors[3].move(5)

        now = time.monotonic()
        end_time = now + duration

        while time.monotonic() <= end_time:
            yield
        
        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()

    def check_all_faults(self):
        self.motors[0].check_faults()
        self.motors[1].check_faults()
        self.motors[2].check_faults()
        self.motors[3].check_faults()

    def stop(self):
        for m in self.motors:
            m.stop()

    def update(self):
        for m in self.motors:
            m.update()
























