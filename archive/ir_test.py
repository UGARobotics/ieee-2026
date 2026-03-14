#https://sensorkit.joy-it.net/en/sensors/ky-022
import RPi.GPIO as GPIO
import time

PIN = 24   # must be PWM-capable pin on most boards

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

pwm = GPIO.PWM(PIN, 5000)   # 38 kHz carrier
pwm.start(10)                # 50% duty cycle

print("Transmitting IR carrier")

time.sleep(5)                # transmit for 5 seconds

pwm.stop()
GPIO.cleanup()
