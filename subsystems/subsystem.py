"""Every subsystem model should implement this interface so that the scheduler can call them all uniformly."""

class Subsystem:
    def update(self):
        """Called every scheduler tick"""
        pass

    def stop(self):
        """Stop everything in this subsystem immediately"""
        pass