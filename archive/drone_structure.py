
"""
This script shows a simple scripted flight path using the MotionCommander class.

Simple example that connects to the crazyflie at `URI` and runs a
sequence. Change the URI variable to your Crazyflie configuration.
"""
import logging
import time
import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
import cv2

class Drone:
    def __init__(self):


        # Radio Basics
        self.URI = 'radio://0/80/2M/E7E7E7E7E7'
        self.logging.basicConfig(level=logging.ERROR)
        self.scf = None
        self.mc = None

        cflib.crtp.init_drivers()

        # Camera Basics
        self.cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    def connect(self):
        try:
            self._scf = SyncCrazyflie(self.URI).__enter__()
            self._scf.cf.platform.send_arming_request(True)
            time.sleep(1.0)
            self._mc = MotionCommander(self._scf, default_height=self.default_height).__enter__()
            time.sleep(1.0)
            print("Connected?")
        except:
            print("Error Connecting")

    def stop(self):
        self.mc.stop()

    '''
    DRONE MOVEMENT COMMANDS
    '''

    def move_right(self, distance: float, velocity: float = 0.5) -> None:
        self.mc.right(distance, velocity=velocity)

    def move_left(self, distance: float, velocity: float) -> None:
         self.mc.left(distance, velocity=velocity)

    def move_forward(self, distance: float, velocity: float) -> None:
         self.mc.forward(distance, velocity=velocity)

    def move_back(self, distance: float, velocity: float) -> None:
         self.mc.back(distance, velocity=velocity)

    def move_up(self, distance: float, velocity: float) -> None:
         self.mc.up(distance, velocity=velocity)

    def move_down(self, distance: float, velocity: float) -> None:
         self.mc.down(distance, velocity=velocity)

    def land(self) -> None:
        self.mc.land()

    def hover(self, duration: float) -> None:
        time.sleep(duration)

    '''
    CAMERA COMMANDS
    '''

    def capture_from_rc832(output_path: str = "capture.png") -> None
        if not self.cap.isOpened():
            raise RuntimeError("Could not open /dev/video0 — check capture card is connected")

        for _ in range(5):
            self.cap.read()

        ret, frame = self.cap.read()
        self.cap.release()

        cv2.imwrite(output_path, frame)
        print(f"Saved {output_path}")

    '''
    IR COMMANDS
    '''

    def ir_transmit():

