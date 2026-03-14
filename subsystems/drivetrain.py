import time

from utils.motor import Motor
from subsystems.odometry import Odometry
from subsystems.intake import Intake

class Drivetrain:
    SLIP            = 0.1              # Adjust value for testing
    TIME_PER_PI     = 4.11             # Time in seconds

    def __init__(self, motors: list[Motor], odometry: Odometry = None, intake: Intake = None):
        # in order of front left, front right, back left, back right
        self.motors = motors
        self.odometry = odometry
        self.intake = intake

    def go_forward(self, distance, holding=False, seeking=False):
        _, y, _ = self.odometry.get_position()
        target_y = y + distance

        if holding:
            self.intake.main_servo.move(-0.5)
            self.intake.lift_servo.set_angle(100)
        elif seeking:
            self.intake.main_servo.move(-1.0)
            self.intake.lift_servo.set_angle(160)

        self.motors[0].move(15)
        self.motors[1].move(-15)
        self.motors[2].move(15)
        self.motors[3].move(-15)


        while abs(target_y - y) > self.SLIP:
            _, y, _ = self.odometry.get_position()
            print(abs(target_y - y))
            yield        

        if holding or seeking:
            self.intake.main_servo.move(0)

        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()



    def go_backward(self, distance, holding=False):
        _, y, _ = self.odometry.get_position()
        target_y = y - distance

        if holding:
            self.intake.main_servo.move(-0.5)
            self.intake.lift_servo.set_angle(100)

        self.motors[0].move(-15)
        self.motors[1].move(15)
        self.motors[2].move(-15)
        self.motors[3].move(15)


        while abs(y - target_y) > self.SLIP:
            _, y, _ = self.odometry.get_position()
            print(abs(y-target_y))
            yield

        if holding:
            self.intake.main_servo.move(0)

        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()

    def strafe_left(self, distance, holding=False):
        x, _, _ = self.odometry.get_position()
        target_x = x - distance
        
        if holding:
            self.intake.main_servo.move(-0.5)
            self.intake.lift_servo.set_angle(100)

        self.motors[0].move(15)
        self.motors[1].move(15)
        self.motors[2].move(-15)
        self.motors[3].move(-15)

        while abs(x - target_x) > self.SLIP:
            x, _, _ = self.odometry.get_position()
            print(abs(x - target_x))
            yield

        if holding:
            self.intake.main_servo.move(0)
                    
        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()

    def strafe_right(self, distance, holding=False):
        x, _, _ = self.odometry.get_position()
        target_x = x + distance

        if holding:
            self.intake.main_servo.move(-0.5)
            self.intake.lift_servo.set_angle(100)

        self.motors[0].move(-15)
        self.motors[1].move(-15)
        self.motors[2].move(15)
        self.motors[3].move(15)

        while abs(x - target_x) > self.SLIP:
            x, _, _ = self.odometry.get_position()
            print(abs(x - target_x))
            yield

        if holding:
            self.intake.main_servo.move(0)

        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()

    def turn_left(self, rotation, holding=False, shimmy=False):

        duration = rotation * self.TIME_PER_PI

        if shimmy:
            self.intake.main_servo.move(-0.5)
        elif holding:
            self.intake.main_servo.move(-0.5)
            self.intake.lift_servo.set_angle(100)

        self.motors[0].move(-15)
        self.motors[1].move(-15)
        self.motors[2].move(-15)
        self.motors[3].move(-15)

        now = time.monotonic()
        end_time = now + duration

        while time.monotonic() <= end_time:
            yield

        if holding or shimmy:
            self.intake.main_servo.move(0)
        
        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()


    def turn_right(self, rotation, holding=False, shimmy=False):
        
        duration = rotation * self.TIME_PER_PI

        if shimmy:
            self.intake.main_servo.move(-0.5)
        elif holding:
            self.intake.main_servo.move(-0.5)
            self.intake.lift_servo.set_angle(100)
        
        self.motors[0].move(15)
        self.motors[1].move(15)
        self.motors[2].move(15)
        self.motors[3].move(15)

        now = time.monotonic()
        end_time = now + duration

        while time.monotonic() <= end_time:
            yield
            
        if holding or shimmy:
            self.intake.main_servo.move(0)
        
        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()

    def go_forward_timed(self, duration):
        now = time.monotonic()
        end_time = now + duration

        self.motors[0].move(15)
        self.motors[1].move(-15)
        self.motors[2].move(15)
        self.motors[3].move(-15)

        while time.monotonic() <= end_time:
            yield

        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()


    def go_backward_timed(self, duration):
        now = time.monotonic()
        end_time = now + duration

        self.motors[0].move(-15)
        self.motors[1].move(15)
        self.motors[2].move(-15)
        self.motors[3].move(15)

        while time.monotonic() <= end_time:
            yield

        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()

    def strafe_left_timed(self, duration):
        now = time.monotonic()
        end_time = now + duration

        self.motors[0].move(15)
        self.motors[1].move(15)
        self.motors[2].move(-15)
        self.motors[3].move(-15)

        while time.monotonic() <= end_time:
            yield

        self.motors[0].stop()
        self.motors[1].stop()
        self.motors[2].stop()
        self.motors[3].stop()

    def strafe_right_timed(self, duration):
        now = time.monotonic()
        end_time = now + duration

        self.motors[0].move(-15)
        self.motors[1].move(-15)
        self.motors[2].move(15)
        self.motors[3].move(15)

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
























