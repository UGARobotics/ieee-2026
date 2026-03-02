import time

from utils.motor import Motor
from subsystems.odometry import Odometry

class Drivetrain:
    
    TIME_PER_INCH   = 0.158333333     # Adjust value for testing
    TIME_PER_PI     = 4.2             # Adjust value for testing

    def __init__(self, motors: list[Motor], odometry: Odometry = None):
        # in order of front left, front right, back left, back right
        self.motors = motors
        self.odometry = odometry

    def go_forward(self, duty, distance):
        # loop until bot's position is within some threshold of the target position, with a timeout to prevent infinite loops
        _, y = self.odometry.get_position()
        target_y = y + distance

        kP = 0.1
        kI = 0.0
        kD = 0.1

        integral = 0
        last_error = 0

        while abs(y - target_y) > 0.1:  # 0.1 inch threshold
            y, _ = self.odometry.get_position()
            error = target_y - y

            integral += error
            derivative = error - last_error
            last_error = error

            output = kP*error + kI*integral + kD*derivative

            self.motors[0].move(output)
            self.motors[1].move(-output)
            self.motors[2].move(output)
            self.motors[3].move(-output)
            _, y = self.odometry.get_position()
            yield
        
        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()

    def go_backward(self, duty, distance):
        
        # loop until bot's position is within some threshold of the target position, with a timeout to prevent infinite loops
        _, y = self.odometry.get_position()
        target_y = y - distance

        self.motors[0].move(-duty)  # front left
        self.motors[1].move(duty)  # front right
        self.motors[2].move(-duty)  # back left
        self.motors[3].move(duty)  # back right

        while abs(y - target_y) > 0.1:  # 0.1 inch threshold
            _, y = self.odometry.get_position()
            yield
        
        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()

    def strafe_left(self, duty, distance):
        
        # loop until bot's position is within some threshold of the target position, with a timeout to prevent infinite loops
        x, _ = self.odometry.get_position()
        target_x = x - distance

        self.motors[0].move(duty)  # front left
        self.motors[1].move(duty)  # front right
        self.motors[2].move(-duty)  # back left
        self.motors[3].move(-duty)   # back right

        while abs(x - target_x) > 0.1:  # 0.1 inch threshold
            x, _ = self.odometry.get_position()
            yield
        
        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()

    def strafe_right(self, duty, distance):
        
        # loop until bot's position is within some threshold of the target position, with a timeout to prevent infinite loops
        x, _ = self.odometry.get_position()
        target_x = x + distance

        self.motors[0].move(-duty)  # front left
        self.motors[1].move(-duty)  # front right
        self.motors[2].move(duty)  # back left
        self.motors[3].move(duty)   # back right

        while abs(x - target_x) > 0.1:  # 0.1 inch threshold
            x, _ = self.odometry.get_position()
            yield
        
        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()

        
    def go_forward_timed(self, duty, distance):
        duration = distance * self.TIME_PER_INCH
        self.motors[0].move(duty, duration)  # front left
        self.motors[1].move(-duty, duration)  # front right
        self.motors[2].move(duty, duration)  # back left
        self.motors[3].move(-duty, duration)  # back right

        end_time = time.monotonic() + duration
        while time.monotonic() < end_time:
            yield

    def go_backward_timed(self, duty, distance):
        duration = distance * self.TIME_PER_INCH
        self.motors[0].move(-duty, duration)  # front left
        self.motors[1].move(duty, duration)  # front right
        self.motors[2].move(-duty, duration)  # back left
        self.motors[3].move(duty, duration)  # back right

        end_time = time.monotonic() + duration
        while time.monotonic() < end_time:
            yield

    def turn_left_timed(self, duty, distance):
        duration = distance * self.TIME_PER_PI
        self.motors[0].move(duty, duration)  # front left
        self.motors[1].move(duty, duration)  # front right
        self.motors[2].move(duty, duration)  # back left
        self.motors[3].move(duty, duration)  # back right
        
        end_time = time.monotonic() + duration
        while time.monotonic() < end_time:
            yield

    def turn_right_timed(self, duty, distance):
        duration = distance * self.TIME_PER_PI
        self.motors[0].move(-duty, duration)  # front left
        self.motors[1].move(-duty, duration)  # front right
        self.motors[2].move(-duty, duration)  # back left
        self.motors[3].move(-duty, duration)  # back right
        
        end_time = time.monotonic() + duration
        while time.monotonic() < end_time:
            yield

    def strafe_left_timed(self, duty, distance):
        duration = distance * self.TIME_PER_INCH
        self.motors[0].move(duty, duration)  # front left
        self.motors[1].move(duty, duration)  # front right
        self.motors[2].move(-duty, duration)  # back left
        self.motors[3].move(-duty, duration)  # back right
        
        end_time = time.monotonic() + duration
        while time.monotonic() < end_time:
            yield

    def strafe_right_timed(self, duty, distance):
        duration = distance * self.TIME_PER_INCH
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
