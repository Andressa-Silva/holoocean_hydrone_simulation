import holoocean
import numpy as np

env = holoocean.make("OpenWater-TorpedoSinglebeamSonar")

# The hovering AUV takes a command for each thruster
torques_uav = np.array([0,0,0,40])
vel_ang_uav = np.array([0,0,0,0])

torques_rov = np.array([10,10,10,10,0,0,0,0])

for _ in range(1800000):
   state = env.step(torques_rov)
   print(state)
   
   