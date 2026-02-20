from phoenix6.hardware import TalonFX
from phoenix6.controls import DutyCycleOut, DifferentialVelocityDutyCycle
from phoenix6.configs import TalonFXConfiguration, CurrentLimitsConfigs, Slot0Configs
from phoenix6.unmanaged import feed_enable

import os
import time

os.environ["CTR_TARGET"] = "Hardware"

canivore="Main" 
stator_current_limit=120 
stator_current_limit_enable=True
motor0 = TalonFX(1, canivore)
print("Initializing motor...")

print("Clearing faults...")
motor0.clear_sticky_faults()
time.sleep(0.5)
print("Cleared.")

# Not sure if these current limits are actually needed. but why not?
print(f"Setting stator current limit to {stator_current_limit}...")
lmt_cfg0 = CurrentLimitsConfigs()
lmt_cfg0.stator_current_limit = stator_current_limit
lmt_cfg0.stator_current_limit_enable = stator_current_limit_enable
motor0.configurator.apply(lmt_cfg0)
time.sleep(0.5)
print(f"Current configurations applied.")

# Base configs should also already be applied but better to do it explicitly
# Note: Changes can be made here and above if the settings don't work with the bot
print("Applying base configurations...")
cfg0 = TalonFXConfiguration()
motor0.configurator.apply(cfg0)
time.sleep(0.5)
print("Base configurations applied.")


print("Setting the slot 0 PID configs...")
pid_conf0 = Slot0Configs()

pid_conf0.k_p = 0.012
pid_conf0.k_i = 0.008

motor0.configurator.apply(pid_conf0)
time.sleep(0.5)
print("PID configurations applied.")

time.sleep(2)
# yay
feed_enable(20) 
# motor.set_control(DutyCycleOut(duty))
#motor0.set_control(DifferentialVelocityDutyCycle(target_velocity=2, differential_slot=0, differential_position=0))
#motor0.set_control(DifferentialVelocityDutyCycle(target_velocity=5, differential_slot=0, differential_position=0))
#motor0.set_control(DifferentialVelocityDutyCycle(target_velocity=7, differential_slot=0, differential_position=0))
motor0.set_control(DifferentialVelocityDutyCycle(target_velocity=50, differential_slot=0, differential_position=0)

#time.sleep(1)
#motor1.set_control(DifferentialVelocityDutyCycle(target_velocity=2, differential_slot=0, differential_position=0))
#motor1.set_control(DifferentialVelocityDutyCycle(target_velocity=5, differential_slot=0, differential_position=0))
#motor1.set_control(DifferentialVelocityDutyCycle(target_velocity=7, differential_slot=0, differential_position=0))


#time.sleep(1)
#motor2.set_control(DifferentialVelocityDutyCycle(target_velocity=2, differential_slot=0, differential_position=0))
#motor2.set_control(DifferentialVelocityDutyCycle(target_velocity=5, differential_slot=0, differential_position=0))
#motor2.set_control(DifferentialVelocityDutyCycle(target_velocity=7, differential_slot=0, differential_position=0))


#time.sleep(1)
#motor3.set_control(DifferentialVelocityDutyCycle(target_velocity=2, differential_slot=0, differential_position=0))
#motor3.set_control(DifferentialVelocityDutyCycle(target_velocity=5, differential_slot=0, differential_position=0))
#motor3.set_control(DifferentialVelocityDutyCycle(target_velocity=7, differential_slot=0, differential_position=0))

time.sleep(10)

print("Current stator fault:", motor0.get_fault_stator_curr_limit())
print("Sticky stator fault:", motor0.get_sticky_fault_stator_curr_limit())
print("Current stator fault:", motor0.get_fault_bridge_brownout())
print("Sticky stator fault:", motor0.get_sticky_fault_bridge_brownout())

