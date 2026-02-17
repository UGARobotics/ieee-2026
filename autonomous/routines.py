import time

"""Contains all of the different autonomous routines/runs over time. """


def tester_auto(drivetrain):
    """Auto routine that you can change for quick tests."""

    yield from drivetrain.go_forward(20, 2.0)
#    time.sleep(1)
    yield from drivetrain.go_forward(80, 1.0)
#    time.sleep(1)
    # LOL THIS WORKS BELOW
#    yield from drivetrain.go_forward(160, 1.0)
    time.sleep(1)



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

    
