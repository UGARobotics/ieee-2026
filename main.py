from scheduler.scheduler import Scheduler
from subsystems.odometry import Odometry
from subsystems.tail import Tail
from utils.motor import Motor
from subsystems.drivetrain import Drivetrain
from autonomous.routines import basic_auto, tester_auto

import time

# initialize motors
front_right = Motor(0)
front_left = Motor(1)
back_left = Motor(2)
back_right = Motor(3)

time.sleep(3)

# initialize subsystems
odometry = Odometry()
tail = Tail()
drivetrain = Drivetrain([front_left, front_right, back_left, back_right])

scheduler = Scheduler(tick_hz=50)
scheduler.add_subsystem(drivetrain)
scheduler.add_subsystem(odometry)
scheduler.add_subsystem(tail)
# scheduler.add_subsystem(servo_system)

# run the auto routine
try:
    # this is going to run until the routine is complete
    scheduler.run_routine(tester_auto(drivetrain, odometry, tail))

except KeyboardInterrupt:
    # emergency stop
    print("Stopping all subsystems...")
    scheduler.stop_all()
