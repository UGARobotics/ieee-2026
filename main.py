"""

This is the entry point for running autonomous routines using the Scheduler framework.

Structure Overview:
-------------------
1. Motors:
   - Individual TalonFX motors are wrapped in the Motor class.
   - Each Motor maintains its own state machine (IDLE / RUNNING) and duration-based motion.
   - Motors are updated periodically by the Scheduler.

2. Drivetrain:
   - Drivetrain subsystem coordinates multiple motors for movement.
   - Provides high-level commands like `go_forward` and `turn_left`.
   - These commands are implemented as generators, allowing non-blocking execution.

3. Scheduler:
   - Manages all subsystems (motors, drivetrain, odometry, servos, etc.) at a fixed tick rate (50 Hz here).
   - Calls each subsystem's `update()` method every tick.
   - Feeds the enable signal automatically via `feed_enable()`.
   - Supports running generator-based autonomous routines until completion.
   - Stops all motors safely on completion or emergency.

4. Autonomous routines:
   - Written as Python generators (`yield` / `yield from`) for sequential, readable control flow.
   - Scheduler interleaves subsystem updates between yields, enabling concurrent motor execution.

"""


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
