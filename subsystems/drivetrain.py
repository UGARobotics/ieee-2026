import time

from utils.motor import Motor

class Drivetrain:
    def __init__(self, motors: list[Motor]):
        # in order of front left, front right, back left, back right
        self.motors = motors

    def go_forward(self, duty, duration):
        self.motors[0].move(duty, duration)  # front left
        self.motors[1].move(-duty, duration)  # front right
        self.motors[2].move(duty, duration)  # back left
        self.motors[3].move(-duty, duration)  # back right

        end_time = time.monotonic() + duration
        while time.monotonic() < end_time:
            yield

    def go_backward(self, duty, duration):
        self.motors[0].move(-duty, duration)  # front left
        self.motors[1].move(duty, duration)  # front right
        self.motors[2].move(-duty, duration)  # back left
        self.motors[3].move(duty, duration)  # back right

        end_time = time.monotonic() + duration
        while time.monotonic() < end_time:
            yield

    def turn_left(self, duty, duration):
        self.motors[0].move(duty, duration)  # front left
        self.motors[1].move(duty, duration)  # front right
        self.motors[2].move(duty, duration)  # back left
        self.motors[3].move(duty, duration)  # back right
        
        end_time = time.monotonic() + duration
        while time.monotonic() < end_time:
            yield

    def turn_right(self, duty, duration):
        self.motors[0].move(-duty, duration)  # front left
        self.motors[1].move(-duty, duration)  # front right
        self.motors[2].move(-duty, duration)  # back left
        self.motors[3].move(-duty, duration)  # back right
        
        end_time = time.monotonic() + duration
        while time.monotonic() < end_time:
            yield

    def strafe_left(self, duty, duration):
        self.motors[0].move(duty, duration)  # front left
        self.motors[1].move(duty, duration)  # front right
        self.motors[2].move(-duty, duration)  # back left
        self.motors[3].move(-duty, duration)  # back right
        
        end_time = time.monotonic() + duration
        while time.monotonic() < end_time:
            yield

    def strafe_right(self, duty, duration):
        self.motors[0].move(-duty, duration)  # front left
        self.motors[1].move(-duty, duration)  # front right
        self.motors[2].move(duty, duration)  # back left
        self.motors[3].move(duty, duration)  # back right
        
        end_time = time.monotonic() + duration
        while time.monotonic() < end_time:
            yield

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