import time

"""Contains all of the different autonomous routines/runs over time. """

def tester_auto(drivetrain):
    """Auto routine that you can change for quick tests."""

    yield from drivetrain.turn_right(15, 2.2)

    
def timed_auto(drivetrain):
    TIME_PER_INCH = 0.158333333
    TIME_PER_PI=4.2

    # GRAB DUCK 1
    # 6in fw
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 6)
    # 3in strafe right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 3)
    # 6in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 6)
    # pause a second
    time.sleep(1)

    # DEPOSIT FLAG
    # pi/2 turn
    yield from drivetrain.turn_right(15, TIME_PER_PI * 0.5)
    # 6in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 6)
    # 8in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 8)
    # pause a second
    time.sleep(1)

    # PRESSING ANTENNA BUTTON
    # 3in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 3)
    # 3in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 3)
    # 3in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 3)
    # 3in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 3)
    # 3in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 3)
    # 3in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 3)
    # 3in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 3)

    # DROPPING FIRST DUCK
    # 8in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 8)
    # 6in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 6)
    # 3in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 3)
    # pause a second
    time.sleep(1)

    # REALIGN THEN GRAB SECOND DUCK
    # 3in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 3)
    # strafe right into wall
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 32)
    # 8in strafe left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 8)
    # pause
    time.sleep(1)

    # REALIGN
    # pi rotate
    yield from drivetrain.turn_right(15, TIME_PER_PI * 1)
    # 10in strafe left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 10)
    # 3in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 6)
    # 8in strafe right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 8)
    # 7in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 7)
    # pause
    time.sleep(1)

    # FOR KEYPAD ANTENNA 73738#
    # 2in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 2)
    # 1in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 1)
    # pause
    time.sleep(1)
    # 1in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 1)
    # 1in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 1)
    # pause
    time.sleep(1)
    # 1in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 1)
    # 1in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 1)
    # pause
    time.sleep(1)
    # 1in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 1)
    # 1in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 1)
    # pause
    time.sleep(1)
    # 1in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 1)
    # 1in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 1)
    # pause
    time.sleep(1)
    # 1in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 1)
    # 1in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 1)
    # pause
    time.sleep(1)

    # DROPPING OFF SECOND DUCK
    # 10in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 10)
    # 24in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 24)
    # 3in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 3)
    # pause
    time.sleep(1)
    # 3in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 3)
    # 12in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 12)
    # pi
    yield from drivetrain.turn_right(15, TIME_PER_PI * 1)
    # 36in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 36)

    # PICKING UP THIRD DUCK
    # 16in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 16)
    # pause
    time.sleep(1)
    # 2in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 2)

    # DROPPING OFF THIRD DUCK
    # pi
    yield from drivetrain.turn_right(15, TIME_PER_PI * 1)
    # 3in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 3)
    # 6in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 6)
    # pause
    time.sleep(1)

    # PICKING UP FOURTH DUCK
    # 1in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 1)
    # 2in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 2)
    # pi/2 left
    yield from drivetrain.turn_left(15, TIME_PER_PI * 0.5)
    # 3in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 3)
    # 24in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 24)
    # 12in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 12)
    # 16in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 16)
    # 3in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 3)
    # 6in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 6)
    # pause
    time.sleep(1)

    # DOING THE DAIL ANTENNA
    # 3in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 3)
    # 20in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 20)
    # pause
    time.sleep(1)

    # DROPPING OFF FOURTH DUCK
    # 6in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 6)
    # pi/2 right
    yield from drivetrain.turn_right(15, TIME_PER_PI * 0.5)
    # 12in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 12)
    # 16in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 16)
    # 3in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 3)
    # 24in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 24)
    # pause
    time.sleep(1)

    # PICK UP FIFTH DUCK
    # 6in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 6)
    # 30in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 30)
    # AGAINST ANTENNA
    # 2in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 2)
    # 12in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 12)
    # 12in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 12)
    # 20in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 20)
    # 10in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 10)
    # 12in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 12)
    # 6in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 6)
    # pause
    time.sleep(1)

    # DROP OFF FIFTH DUCK
    # 6in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 6)
    # 12in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 12)
    # 10in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 10)
    # 20in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 20)
    # 12in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 12)
    # 12in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 12)
    # 20in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 20)
    # 8in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 8)
    # pause
    time.sleep(1)
    # 8in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 8)

    # PICK UP SIXTH DUCK AND DO WEIGHT ANTENNA
    # 6in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 6)
    # 30in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 30)
    # 2in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 2)
    # 12in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 12)
    # 12in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 12)
    # 20in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 20)
    # 12in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 12)
    # pi/2 right
    yield from drivetrain.turn_right(15, TIME_PER_PI * 0.5)
    # 12in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 12)
    # 12in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 12)
    # CORNER
    # 28in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 28)
    
    # 6in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 6)
    # IN CRATER
    # TODO: WE GO FULL ROTATION 2PI + PI/2
    # 30in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 30)

    # RESET
    # 20in right
    yield from drivetrain.strafe_right(15, TIME_PER_INCH * 20)

    # DROP OFF SIXTH DECK
    # 12in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 12)
    # 12in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 12)
    # pi/2 left
    yield from drivetrain.turn_left(15, TIME_PER_PI * 0.5)
    # 20in fwd
    yield from drivetrain.go_forward(15, TIME_PER_INCH * 20)
    # pause
    time.sleep(1)

    # BACK IN BOX
    # 20in left
    yield from drivetrain.strafe_left(15, TIME_PER_INCH * 20)
    # 20in back
    yield from drivetrain.go_backward(15, TIME_PER_INCH * 20)
    
    

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

    
