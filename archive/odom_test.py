from time import sleep

from odom import PinpointI2C

"""
with PinpointI2C(bus=1, address=0x31, verbose=True) as pp:
	while True:
		print(pp.read_bulk())
		sleep(1)
"""

with PinpointI2C(bus=1, address=0x31, verbose=True, ticks_per_mm=19.894) as p:
	while True:
		print(p.read_bulk())
		sleep(1)
