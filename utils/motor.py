from phoenix6.hardware import TalonFX
from phoenix6.controls import DutyCycleOut
from phoenix6.configs import TalonFXConfiguration, CurrentLimitsConfigs

import os
import time

class Motor:
    """ Motor class manages motor and all the enables for you. Motor needs to be enabled before it can run any command, which is
    what the feed enable signal is. The rest is pretty straightforward or explained in the code. Happy roboting! """

    IDLE = 0
    RUNNING = 1

    def __init__(
        self,
        id, 
        canivore="Main", 
        stator_current_limit=120, 
        stator_current_limit_enable=True
    ):
        # state machine management
        self._state = Motor.IDLE
        self._end_time = 0.0
        self._duty = 0.0

        # may or may not be needed. pretty sure it is
        os.environ["CTR_TARGET"] = "Hardware"

        # On our bus, the name has been set to 'Main' - not 'canivore' or whatever
        self.id = id
        self.canivore = canivore
        self.motor = TalonFX(id, canivore)
        print("Initializing motor...")
        
        # Clear any sticky faults, likely brownout or some bs that's there
        print("Clearing faults...")
        self.motor.clear_sticky_faults()
        time.sleep(0.5)
        print("Cleared.")

        # Not sure if these current limits are actually needed. but why not?
        print(f"Setting stator current limit to {stator_current_limit}...")
        lmt_cfg = CurrentLimitsConfigs()
        lmt_cfg.stator_current_limit = stator_current_limit
        lmt_cfg.stator_current_limit_enable = stator_current_limit_enable
        self.motor.configurator.apply(lmt_cfg)
        time.sleep(0.5)
        print(f"Current configurations applied.")

        # Base configs should also already be applied but better to do it explicitly
        # Note: Changes can be made here and above if the settings don't work with the bot
        print("Applying base configurations...")
        cfg = TalonFXConfiguration()
        self.motor.configurator.apply(cfg)
        time.sleep(0.5)
        print("Base configurations applied.")

        # yay
        print(f"Motor {self.id} live!")

    def move(
        self,
        duty,
        duration=1.0
    ):
        now = time.monotonic()
        
        # set the state machine, with the rest handled in the controller
        self._duty = duty
        self._end_time = now + duration
        self._state = Motor.RUNNING

        self.motor.set_control(DutyCycleOut(duty))

    def check_faults(self):
        # there are other faults. but i gotta write them all out one by one and im a bit lazy. ill do it later
        print("Current stator fault:", self.motor.get_fault_stator_curr_limit())
        print("Sticky stator fault:", self.motor.get_sticky_fault_stator_curr_limit())
        print("Current stator fault:", self.motor.get_fault_bridge_brownout())
        print("Sticky stator fault:", self.motor.get_sticky_fault_bridge_brownout())

    def stop(self):
        self._state = Motor.IDLE
        self._duty = 0.0
        self._end_time = 0.0
        self.motor.set_control(DutyCycleOut(0.0))
        
    def update(self):
        if self._state == Motor.IDLE:
            return

        if time.monotonic() >= self._end_time:
            self.motor.set_control(DutyCycleOut(0.0))
            self._state = Motor.IDLE
            self._duty = 0.0
            self._end_time = 0.0
        else:
            self.motor.set_control(DutyCycleOut(self._duty))