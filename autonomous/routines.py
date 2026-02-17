import time

"""Contains all of the different autonomous routines/runs over time. """

def basic_auto(drivetrain):
    """Basic autonomous routine, the yields allow the scheduler to interleave updates."""

    yield from drivetrain.turn_left(20, 2.0)
    time.sleep(1)
    yield from drivetrain.turn_right(20, 4.0)
    time.sleep(1)
    yield from drivetrain.turn_left(20, 2.0)
    time.sleep(1)
    yield from drivetrain.go_forward(20, 2.0)
    time.sleep(1)
    yield from drivetrain.go_backward(20, 4.0)
    time.sleep(1)
    yield from drivetrain.go_forward(20, 2.0)
    time.sleep(1)
    yield from drivetrain.strafe_left(20, 2.0)
    time.sleep(1)
    yield from drivetrain.strafe_right(20, 4.0)
    time.sleep(1)
    yield from drivetrain.strafe_left(20, 2.0)

    
