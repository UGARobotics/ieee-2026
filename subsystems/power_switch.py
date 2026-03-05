
class StartupSystem:
    """Subsystem for the startup system"""
    def __init__(self, pin=-1):
        self.pin = pin
    
    # when switch is on, bot should boot. when switch is off, bot should shut down.
    # when on, we have to wait for light sensor to detect light before we can start the bot. 
