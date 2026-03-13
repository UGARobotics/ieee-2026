import board
import adafruit_veml7700


i2c = board.I2C()
sensor = adafruit_veml7700.VEML7700(i2c)


while True:
    print(sensor.light)
