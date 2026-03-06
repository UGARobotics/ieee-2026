from scheduler.scheduler import Scheduler
from utils.motor import Motor
from subsystems.odometry import Odometry
from subsystems.tail import Tail
from subsystems.drivetrain import Drivetrain
from subsystems.intake import Intake
from autonomous.routines import tester_auto_tail

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
drivetrain = Drivetrain([front_left, front_right, back_left, back_right], odometry=odometry)
intake = Intake()

scheduler = Scheduler(tick_hz=50)
#scheduler.add_subsystem(drivetrain)
#scheduler.add_subsystem(odometry)
#scheduler.add_subsystem(intake)
scheduler.add_subsystem(tail)

# run the auto routine
try:
    # this is going to run until the routine is complete
    scheduler.run_routine(tester_auto_tail(tail))

except KeyboardInterrupt:
    # emergency stop
    print("Stopping all subsystems...")
    scheduler.stop_all()
