from scheduler.scheduler import Scheduler
from utils.motor import Motor
from subsystems.odometry import Odometry
from subsystems.tail import Tail
from subsystems.drivetrain import Drivetrain
from subsystems.intake import Intake
from subsystems.button_presser import ButtonPresser
from subsystems.startup_system import StartupSystem
from autonomous.routines import core_odometry_routine, all_subsystems_test, tester_auto_button_presser, tester_auto_intake, tester_auto_tail

import time

# initialize motors
front_right = Motor(0)
front_left = Motor(1)
back_left = Motor(2)
back_right = Motor(3)

time.sleep(3)

# initialize subsystems
odometry = Odometry()
intake = Intake()
tail = Tail()
button_presser = ButtonPresser()
drivetrain = Drivetrain([front_left, front_right, back_left, back_right], odometry=odometry, intake=intake)

startup_system = StartupSystem()


scheduler = Scheduler(tick_hz=50)
scheduler.add_subsystem(drivetrain)
scheduler.add_subsystem(odometry)
scheduler.add_subsystem(intake)
scheduler.add_subsystem(tail)
scheduler.add_subsystem(button_presser)
scheduler.add_subsystem(startup_system)

# run the auto routine
try:
    # this is going to run until the routine is complete
    # scheduler.run_routine(all_subsystems_test(drivetrain, odometry, intake, tail, button_presser,startup_system))
    # scheduler.run_routine(core_odometry_routine(drivetrain, odometry, intake, tail, button_presser,startup_system))
    # scheduler.run_routine(tester_auto_button_presser(startup_system, button_presser))
    scheduler.run_routine(tester_auto_intake(startup_system, intake))
    # scheduler.run_routine(tester_auto_tail(tail))

except KeyboardInterrupt:
    # emergency stop
    print("Stopping all subsystems...")
    scheduler.stop_all()
