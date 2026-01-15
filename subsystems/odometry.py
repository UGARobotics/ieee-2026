from utils.odom_handler import PinpointI2C


class Odometry:
    """Subsystem for odometry tracking using PinpointI2C"""

    TICKS_PER_MM = 19.894   # Adjust if needed
    ADDRESS = 0x31          # Default I2C address for PinpointI2C
    BUS = 1                 # Default I2C bus number

    def __init__(self, bus: int = BUS, address: int = ADDRESS, ticks_per_mm: float = TICKS_PER_MM):
        self.odom = PinpointI2C(
            bus=bus,
            address=address,
            ticks_per_mm=ticks_per_mm,
            verbose=True
        )
        
        self.x = 0.0
        self.y = 0.0

    def get_position(self) -> tuple[float, float]:
        """Returns the current (x, y) position in mm"""
        return (self.x, self.y)

    def update(self):
        """Called every scheduler tick"""
        with self.odom as pp:
            pos = pp.read_bulk().pos
            if self.odom.verbose:
                print(f"Odometry Position: x={pos.x} mm, y={pos.y} mm")

            self.x = pos.x
            self.y = pos.y


    def reset(self):
        """Reset odometry position to (0,0)"""
        with self.odom as pp:
            pp.reset_position()
            if self.odom.verbose:
                print("Odometry position reset to (0, 0)")

    def stop(self):
        """Stop everything in this subsystem immediately"""
        self.reset()        
        pass