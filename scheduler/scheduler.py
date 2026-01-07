import time
from phoenix6.unmanaged import feed_enable

class Scheduler:
    def __init__(self, tick_hz=50):
        """Scheduler to manage all subsystems uniformly."""
        self.subsystems = []
        self.dt = 1.0 / tick_hz

    def add_subsystem(self, subsystem):
        """Add individual subsystems like odometry, drivetrain, etc."""
        self.subsystems.append(subsystem)

    def update(self):
        """Update all the subsystems and feed the enable signal"""
        for s in self.subsystems:
            s.update()
        feed_enable(0.1)  # feed the enable signal

    def stop_all(self):
        """Stop all subsystems immediately"""
        for s in self.subsystems:
            s.stop()

    def run_routine(self, routine):
        """Autonomous main loop. While condition is true, keep updating subsystems."""
        try:
            while True:
                self.update()  # tick all subsystems
                try:
                    # advance the routine only if it’s ready
                    next(routine)
                except StopIteration:
                    break
                time.sleep(self.dt)
        finally:
            self.stop_all()