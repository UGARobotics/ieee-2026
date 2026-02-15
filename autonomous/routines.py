import time

"""Contains all of the different autonomous routines/runs over time. """

def basic_auto(drivetrain):
    """Basic autonomous routine, the yields allow the scheduler to interleave updates."""

    yield from drivetrain.turn_left(0.05, 1.0)
    time.sleep(1)
    yield from drivetrain.turn_right(0.05, 1.0)
    time.sleep(1)
    yield from drivetrain.go_forward(0.05, 1.0)
    time.sleep(1)
    yield from drivetrain.go_backward(0.05, 1.0)
    time.sleep(1)
    yield from drivetrain.strafe_left(0.05, 1.0)
    time.sleep(1)
    yield from drivetrain.strafe_right(0.05, 1.0)
    
