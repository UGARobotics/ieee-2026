"""Contains all of the different autonomous routines/runs over time. """

def basic_auto(drivetrain):
    """Basic autonomous routine, the yields allow the scheduler to interleave updates."""

    yield from drivetrain.go_forward(0.5, 2.0)
    yield from drivetrain.turn_left(0.3, 1.0)
    yield from drivetrain.go_forward(0.5, 2.0)
