"""Contains all of the different autonomous routines/runs over time. """

def basic_auto(drivetrain, odometry):
    """Basic autonomous routine, the yields allow the scheduler to interleave updates."""

    yield from drivetrain.go_forward(0.04, 5.0)
    print(odometry.get_position())
    yield from drivetrain.go_forward(0.02, 2.5)
    print(odometry.get_position())
    yield from drivetrain.go_forward(0.0, 1)
    print(odometry.get_position())
    yield from drivetrain.turn_left(0.025, 2.0)
    print(odometry.get_position())
    yield from drivetrain.turn_left(0.0, 1)
    print(odometry.get_position())
    drivetrain.check_all_faults()
    #yield from drivetrain.go_forward(0.05, 2.0)
