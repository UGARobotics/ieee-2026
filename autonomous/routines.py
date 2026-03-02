import time

"""Contains all of the different autonomous routines/runs over time. """

def tester_auto(drivetrain, odometry):
    # time per inch at speed of 20

    """Auto routine that you can change for quick tests."""
    yield from drivetrain.go_forward(20, 12)
    print(odometry.get_position())
    yield from drivetrain.strafe_left(20, 12)
    print(odometry.get_position())
    yield from drivetrain.go_backward(20, 12)
    print(odometry.get_position())
    yield from drivetrain.strafe_right(20, 12)
    print(odometry.get_position())
    
def timed_auto(drivetrain):
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
    
def timed_auto_with_distance(drivetrain):
    # GRAB DUCK 1
    # 7in strafe right
    yield from drivetrain.strafe_right(20, 7)
    # 21in Forward
    yield from drivetrain.go_forward(20, 21)
    # Intake down to pickup position while spinning in
    #  intake.down()
    #  intake.spin_in()
    # Intake up to duck store position while spinning in slowly, keep spinning in until dropoff
    #  intake.up_slow()

    # DROP OFF FIRST DUCK
    # pi/2 turn right
    yield from drivetrain.turn_right(20,0.5)
    # 9in Forward
    yield from drivetrain.go_forward(20, 9)
    # 13.75in Strafe left to be at wall, (maybe an extra inch to go farther and help align if needed)
    yield from drivetrain.strafe_left(20, 13.75)
    # Intake down to dropoff position
    #  intake.down()
    # Intake spin in opposite direction to dropoff duck
    #  intake.spin_out()
    # Intake stop spinning
    #  intake.stop()
    # Intake up to stored position
    #  intake.up()

    # DROP OFF FLAG
    # 7in Back
    yield from drivetrain.go_backward(20, 7)
    # 6in Strafe right
    yield from drivetrain.strafe_right(20, 6)
    # Button pressing mech down to lowest position (to drop off)
    #  button_mech.down()
    # 12in Strafe right
    yield from drivetrain.strafe_right(20, 12)

    # PRESSING ANTENNA BUTTON
    # Button pressing mech down to big red button position (to drop off)
    #  button_mech.down_to_button()
    # 8.75in Back
    yield from drivetrain.go_backward(20, 8.75)
    # 2in Strafe Left
    yield from drivetrain.strafe_left(20, 2)
    # 1in Strafe Right
    yield from drivetrain.strafe_right(20, 1)
    # 1in Strafe Left
    yield from drivetrain.strafe_left(20, 1)
    # 1in Strafe Right
    yield from drivetrain.strafe_right(20, 1)
    # 1in Strafe Left
    yield from drivetrain.strafe_left(20, 1)
    # 2in Strafe Right
    yield from drivetrain.strafe_right(20, 2)
    # Button Pressing Mech back to stored position
    #  button_mech.up()

    # REALIGN THEN GRAB SECOND DUCK
    # 22.625in Strafe Right (to hit wall, maybe another 0.5in to make sure you're lined up)
    yield from drivetrain.strafe_right(20, 22.625)
    # Already at wall, maybe 0.5in back to make sure you're lined up
    yield from drivetrain.go_backward(20, 0.5)
    # You're back at the starting point, can reset position to initial rn 
    # 5.75in Strafe Left
    yield from drivetrain.strafe_left(20, 5.75)
    # 12.5in Forward
    yield from drivetrain.go_forward(20, 12.5)
    # Intake down to pickup position while spinning in
    #  intake.down()
    #  intake.spin_in()
    # Intake up to duck store position while spinning in slowly, keep spinning in until drop-off
    #  intake.up_slow()

    # FOR KEYPAD ANTENNA 73738#
    # pi rotate right
    yield from drivetrain.turn_right(20, 1)
    # 6.5in Strafe Right
    yield from drivetrain.strafe_right(20, 6.5)
    # 21.3in Back
    yield from drivetrain.go_backward(20, 21.3)

    # Keypad Rotate to row 3 keypad position
    # 2in Strafe Left (hit the 7)
    yield from drivetrain.strafe_left(20, 2)
    # 2in Strafe Right
    yield from drivetrain.strafe_right(20, 2)

    # Keypad rotate to row 1 keypad position 
    # Keypad move leg to column 3 position
    # 2in Strafe Left (hit the 3)
    yield from drivetrain.strafe_left(20, 2)
    # 2in Strafe Right 
    yield from drivetrain.strafe_right(20, 2)

    # Keypad rotate to row 3 keypad position
    # Keypad move leg to column 1 position
    # 2in Strafe Left (hit the 7)
    yield from drivetrain.strafe_left(20, 2)
    # 2in Strafe Right 
    yield from drivetrain.strafe_right(20, 2)

    # Keypad rotate to row 1 keypad position 
    # Keypad move leg to column 3 position
    # 2in Strafe Left (hit the 3)
    yield from drivetrain.strafe_left(20, 2)
    # 2in Strafe Right 
    yield from drivetrain.strafe_right(20, 2)

    # Keypad rotate to row 3 keypad position
    # Keypad move leg to column 2 position
    # 2in Strafe Left (hit the 8)
    yield from drivetrain.strafe_left(20, 2)
    # 2in Strafe Right 
    yield from drivetrain.strafe_right(20, 2)

    # Keypad rotate to row 4 keypad position
    # Keypad move leg to column 3 position
    # 2in Strafe Left (hit the #)
    yield from drivetrain.strafe_left(20, 2)
    # 2in Strafe Right 
    yield from drivetrain.strafe_right(20, 2)

    # Keypad move leg to column 1 position
    # Keypad rotate to stored position
    #  button_mech.keypad_stored()

    # DROPPING OFF SECOND DUCK
    # 3in Back
    yield from drivetrain.go_backward(20, 3)
    # 18in Strafe Right
    yield from drivetrain.strafe_right(20, 18)
    # Intake down to dropoff position
    #  intake.down()
    # Intake spin in opposite direction to dropoff duck
    #  intake.spin_out()
    # Intake stop spinning
    #  intake.stop()
    # Intake up to stored position
    #  intake.up()

    # PICKING UP THIRD DUCK
    # 3in Back
    yield from drivetrain.go_backward(20, 3)
    # Rotate pi Right
    yield from drivetrain.turn_right(20, 1)
    # 4.5in Strafe Left (hits wall, maybe another 0.5" to make sure you're against it)
    yield from drivetrain.strafe_left(20, 4.85)
    # 10in Forward
    yield from drivetrain.go_forward(20, 10)
    # Intake down to pickup position while spinning in
    #  intake.down()
    #  intake.spin_in()
    # Intake up to duck store position while spinning in slowly, keep spinning in until dropoff
    #  intake.up_slow()

    # DROPPING OFF THIRD DUCK
    # 10in Back
    yield from drivetrain.go_backward(20, 10)
    # 3in Strafe Right
    yield from drivetrain.strafe_right(20, 3)
    # pi Turn Right
    yield from drivetrain.turn_right(20, 1)
    # 3in Strafe Right (to be against wall)
    yield from drivetrain.strafe_right(20, 3)
    # 4in Back
    yield from drivetrain.go_backward(20, 4)
    # Intake down to dropoff position
    #  intake.down()
    # Intake spin in opposite direction to dropoff duck
    #  intake.spin_out()
    # Intake stop spinning
    #  intake.stop()
    # Intake up to stored position
    #  intake.up()

    # PICKING UP FOURTH DUCK
    # 29in back 
    yield from drivetrain.go_backward(20, 29)
    # 9in Strafe Left
    yield from drivetrain.strafe_left(20, 9)
    # 135deg Turn Left
    yield from drivetrain.turn_left(20, 0.75)  # 0.75*pi ≈ 135deg
    # Intake down to pickup position while spinning in
    #  intake.down()
    #  intake.spin_in()
    # Intake up to duck store position while spinning in slowly, keep spinning in until dropoff
    #  intake.up_slow()

    # DOING THE DIAL ANTENNA
    # 45deg Turn Left
    yield from drivetrain.turn_left(20, 0.125)  # 0.125*pi ≈ 45deg
    # 2in Forward
    yield from drivetrain.go_forward(20, 2)
    # 11.25in Strafe Left (to be against wall, may want to go another 0.5" to make sure you're against wall)
    yield from drivetrain.strafe_left(20, 11.25)
    # 2.5in Back
    yield from drivetrain.go_backward(20, 2.5)
    # Turn Dial servo 720deg CW
    #  dial_servo.turn_cw(2)  # 2 full rotations

    # DROPPING OFF FOURTH DUCK
    # 2in Forward
    yield from drivetrain.go_forward(20, 2)
    # 9in Strafe Right
    yield from drivetrain.strafe_right(20, 9)
    # pi/2 Right
    yield from drivetrain.turn_right(20, 0.5)
    # 11.25in Strafe Right (to be against wall, may want to go an additional 0.5" to make sure you're lined up)
    yield from drivetrain.strafe_right(20, 11.55)
    # 31.5in Forward
    yield from drivetrain.go_forward(20, 31.5)
    # 4in Strafe Left
    yield from drivetrain.strafe_left(20, 4)
    # Intake down to dropoff position
    #  intake.down()
    # Intake spin in opposite direction to dropoff duck
    #  intake.spin_out()
    # Intake stop spinning
    #  intake.stop()
    # Intake up to stored position
    #  intake.up()

    # PICK UP FIFTH DUCK
    # 4in Strafe Right (to be against wall, may want to go an additional 0.5")
    yield from drivetrain.strafe_right(20, 4.35)
    # 32in Back
    yield from drivetrain.go_backward(20, 32)
    # 34.74in Strafe Left (to be against wall, may want to go an additional 0.5in)
    yield from drivetrain.strafe_left(20, 35)
    # 8.75in Back (to be against corner, may want to go an additional 0.5")
    yield from drivetrain.go_backward(20, 8.75)
    # 14in Forward
    yield from drivetrain.go_forward(20, 14)
    # Intake down to pickup position while spinning in
    #  intake.down()
    #  intake.spin_in()
    # Intake up to duck store position while spinning in slowly, keep spinning in until dropoff
    #  intake.up_slow()

    # DROP OFF FIFTH DUCK
    # 3in Strafe Right
    yield from drivetrain.strafe_right(20, 3)
    # Turn pi/2 Right
    yield from drivetrain.turn_right(20, 0.5)
    # 2.75in Back (to be against wall)
    yield from drivetrain.go_backward(20, 3)
    # 27.5in Strafe Left
    yield from drivetrain.strafe_left(20, 27.5)
    # 9in Forward (this will dip into the crater, but it should be fine and odom wheels will stay on the floor)
    yield from drivetrain.go_forward(20, 9)
    # 8in Strafe Left
    yield from drivetrain.strafe_left(20, 8)
    # 8in Forward
    yield from drivetrain.go_forward(20, 8)
    # Intake down to dropoff position
    #  intake.down()
    # Intake spin in opposite direction to dropoff duck
    #  intake.spin_out()
    # Intake stop spinning
    #  intake.stop()
    # Intake up to stored position
    #  intake.up()

    # PICK UP SIXTH DUCK AND DO WEIGHT ANTENNA (from the front side now)
    # Rotate pi/2 Right
    yield from drivetrain.turn_right(20, 0.5)
    # Strafe 1in Right
    yield from drivetrain.strafe_right(20, 1)
    # 8.25in Forward (This will enter the crater a little bit to grab the duck)
    yield from drivetrain.go_forward(20, 8.25)
    # Intake down to CRATER Pickup position while spinning in
    #  intake.down_crater()
    #  intake.spin_in()
    # Intake up to duck store position while spinning in slowly, keep spinning in until dropoff
    #  intake.up_slow()
    # 3in Forward (This will enter the crater A LOT and we will have to tune in exactly how much to drive forward here to dip in but not too far)
    yield from drivetrain.go_forward(20, 3)

    # IN CRATER
    # TODO: WE GO FULL ROTATION 2PI + PI/2
    

    # RESET
    # 44.25in Back (to be against wall, may want to go an additional 0.5")
    yield from drivetrain.go_backward(20, 44.75)
    # 16.25in Strafe Right (to be in corner, may want to go an additional 0.5" to make sure you're in the right spot)
    yield from drivetrain.strafe_right(20, 16.75)

    # DROP OFF SIXTH DUCK
    # 17.25in Strafe Left
    yield from drivetrain.strafe_left(20, 17.25)
    # 12in Forward
    yield from drivetrain.go_forward(20, 12)
    # Turn pi/2 Left
    yield from drivetrain.turn_left(20, 0.5)
    # Strafe Right 14in
    yield from drivetrain.strafe_right(20, 14)
    # Intake down to dropoff position
    #  intake.down()
    # Intake spin in opposite direction to dropoff duck
    #  intake.spin_out()
    # Intake stop spinning
    #  intake.stop()
    # Intake up to stored position
    #  intake.up()

    # Drone Take off
    # Strafe Right 10in
    yield from drivetrain.strafe_right(20, 10)
    # Drone take off straight vertical at least 15in
    #  drone.take_off(15)
    # Bot Strafe Left 36in (to be against wall, may want to go a bit further to make sure it's against the wall)
    yield from drivetrain.strafe_left(20, 36)
    # Drone Looks at antennas (hopefully w/o moving but we'll see what the drone can see later) and get colors, transmits to the earth, then strafes 36in right and lands vertically down on the bot
    #  drone.look_and_transmit()
    yield from drivetrain.strafe_right(20, 36)
    #  drone.land()

    # BACK TO START BOX
    # Back 17in to get back to start box, may want to strafe right 0.5" and back 0.5" to make sure we're in
    yield from drivetrain.go_backward(20, 17)
    yield from drivetrain.strafe_right(20, 0.5)
    yield from drivetrain.go_backward(20, 0.5)

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

    
