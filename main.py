from scheduler.scheduler import Scheduler
from utils.motor import Motor
from subsystems.drivetrain import Drivetrain
from autonomous.routines import basic_auto

# initialize motors
front_right = Motor(0)
front_left = Motor(1)
back_left = Motor(2)
back_right = Motor(3)

# initialize subsystems
drivetrain = Drivetrain([front_left, front_right, back_left, back_right])

scheduler = Scheduler(tick_hz=50)
scheduler.add_subsystem(drivetrain)
# scheduler.add_subsystem(servo_subsystem)
# scheduler.add_subsystem(odom_subsystem)

# run the auto routine
try:
    # this is going to run until the routine is complete
    scheduler.run_routine(basic_auto(drivetrain))

except KeyboardInterrupt:
    # emergency stop
    print("Stopping all subsystems...")
    scheduler.stop_all()
