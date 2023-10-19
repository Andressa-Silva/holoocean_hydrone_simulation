import holoocean
import numpy as np

env = holoocean.make('SimpleUnderwater-UAV')
env.reset()

#motors = env.act('auv0', np.array([0,0,0,50]))
#angles = env.act('auv0', np.array([0,0,0,0]))

torques_uav = np.array([0,0,0,40])
vel_ang_uav = np.array([0,0,0,0])
#env.act('auv1', np.array([0,0,0,50]))
#env.act('auv1', np.array([0,0,0,0]))
env.act('auv1', np.array([10,10,10,10,0,0,0,0]))

for i in range(300000):
    states = env.step(torques_uav)

    # states is a dictionary
    #imu = states["auv0"]["IMUSensor"]
    vel = states["auv1"]["DVLSensor"]
