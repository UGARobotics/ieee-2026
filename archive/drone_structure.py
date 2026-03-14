import time
import cflib.crtp

from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander


class Drone:

    def __init__(self):

        # Radio settings
        self.URI = 'radio://0/80/2M/E7E7E7E7E7'
        self.default_height = 0.5

        self.scf = None
        self.mc = None

        cflib.crtp.init_drivers()

    # -----------------------------
    # CONNECTION
    # -----------------------------

    def connect(self):

        try:
            self.scf = SyncCrazyflie(self.URI)
            self.scf.open_link()

            self.scf.cf.platform.send_arming_request(True)
            time.sleep(1)

            self.mc = MotionCommander(self.scf, default_height=self.default_height)
            self.mc.take_off()

            print("Connected to Crazyflie")
            return True

        except Exception as e:
            print("Connection failed:", e)
            return False

    def disconnect(self):

        try:
            if self.mc:
                self.mc.land()

            if self.scf:
                self.scf.close_link()

            print("Disconnected")

        except Exception as e:
            print("Disconnect error:", e)

    # -----------------------------
    # MOVEMENT
    # -----------------------------

    def move_up(self, distance, velocity=0.3):
        if self.mc:
            self.mc.up(distance, velocity=velocity)

    def move_down(self, distance, velocity=0.3):
        if self.mc:
            self.mc.down(distance, velocity=velocity)

    def move_forward(self, distance, velocity=0.4):
        if self.mc:
            self.mc.forward(distance, velocity=velocity)

    def move_back(self, distance, velocity=0.4):
        if self.mc:
            self.mc.back(distance, velocity=velocity)

    def move_left(self, distance, velocity=0.4):
        if self.mc:
            self.mc.left(distance, velocity=velocity)

    def move_right(self, distance, velocity=0.4):
        if self.mc:
            self.mc.right(distance, velocity=velocity)

    def hover(self, duration):
        time.sleep(duration)

    def stop(self):
        if self.mc:
            self.mc.stop()

    def land(self):
        if self.mc:
            self.mc.land()

    def shimmy(self, duration):
        time.sleep(duration/2)
        self.mc.move_forward(0.001)
        self.mc.move_backward(0.001)
        time.sleep(duration/2)


# -----------------------------
# MAIN PROCEDURE
# -----------------------------
drone = Drone()

if drone.connect():
    drone.move_up(0.3)
    drone.hover(1)
    drone.move_right(0.1)
    drone.hover(1)
    drone.land()

