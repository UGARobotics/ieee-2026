import time
from utils.light_sensor import LightSensor

light_sensor = LightSensor(
    bus=1,
    address_primary=0x10,
    use_secondary=False
)

try:
    while True:
        light_sensor.update()
        print(f"Raw: {light_sensor.get_light_level()} | Averaged: {light_sensor.get_averaged_light_level()} | State: {light_sensor.get_state()}")
        time.sleep(0.1)
except KeyboardInterrupt:
    light_sensor.stop()
    print("Stopped")
