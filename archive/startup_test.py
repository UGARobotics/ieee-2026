import RPi.GPIO as GPIO
import time

PIN = 21  # BCM numbering

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    print("reading GPIO pin... press ctrl+c to stop\n")
    
    while True:
        pin_state = GPIO.input(PIN)

        if pin_state == GPIO.HIGH:
            print("HIGH (power detected)")
        else:
            print("LOW (no power)")

        time.sleep(0.2)

except KeyboardInterrupt:
    print("\nexiting")

finally:
    GPIO.cleanup()
