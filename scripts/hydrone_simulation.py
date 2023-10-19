import holoocean
import numpy as np
import matplotlib.pyplot as plt

scenario = "SimpleUnderwater-UAV"
env = holoocean.make(scenario)
config = holoocean.packagemanager.get_scenario(scenario)
config = config['agents'][1]['sensors'][-1]["configuration"]
minR = config['RangeMin']
maxR = config['RangeMax']
binsR = config['RangeBins']

# plot graph
plt.ion()

t = np.arange(0,50)
r = np.linspace(minR, maxR, binsR)
T, R = np.meshgrid(t, r)
data = np.zeros_like(R)

plt.grid(False)
plot = plt.pcolormesh(T, R, data, cmap='gray', shading='auto', vmin=0, vmax=1)
plt.tight_layout()
plt.gca().invert_yaxis()
plt.gcf().canvas.flush_events()

#motors = env.act('auv0', np.array([0,0,0,50]))
#angles = env.act('auv0', np.array([0,0,0,0]))

torques_uav = np.array([0,0,0,40])
vel_ang_uav = np.array([0,0,0,0])
#env.act('auv1', np.array([0,0,0,50]))
#env.act('auv1', np.array([0,0,0,0]))


for i in range(300000):
    states = env.step(torques_uav)
    states_rov = env.tick()

    env.act('auv1', np.array([10,10,10,10,10,10,10,10]))

    # states is a dictionary
    #imu = states["auv0"]["IMUSensor"]
    vel = states_rov["auv1"]["DVLSensor"]

    if 'SinglebeamSonar' in states_rov:
        data = np.roll(data, 1, axis=1)
        data[:,0] = states_rov['SinglebeamSonar']

        plot.set_array(data.ravel())

        plt.draw()
        plt.gcf().canvas.flush_events()
