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

config_uav = config['agents'][0]['sensors'][-1]['configuration']
laser_max = config_uav['LaserMaxDistance']
laser_count = config_uav['LaserCount']

r_auv = np.linspace(laser_max, laser_count)
T_uav, R_uav = np.meshgrid(t,r_auv)
data_uav = np.zero_like(R_uav)
plot_laser = plt.pcolormesh(T_uav, R_uav, data_uav, cmap='blue', shading='auto', vmin=0, vmax=1)


torques_uav = np.array([0,0,0,40])
vel_ang_uav = np.array([0,0,0,0])
#env.act('auv1', np.array([0,0,0,50]))
#env.act('auv1', np.array([0,0,0,0]))


for i in range(300000):
    states = env.step(torques_uav)

    env.act('auv1', np.array([10,10,10,10,10,10,10,10]))

    # states is a dictionary
    #imu = states["auv0"]["IMUSensor"]
    vel = states["auv1"]["DVLSensor"]
 
    """ if 'SinglebeamSonar' in states["auv1"]:
        data = np.roll(data, 1, axis=1)
        print(data)
        data[:,0] = states["auv1"]['SinglebeamSonar']

        plot.set_array(data.ravel())

        plt.draw()
        plt.gcf().canvas.flush_events() """

    if 'RangeFinderSensor' in states["auv0"]:
        data_uav = np.roll(data_uav, 1, axis=1)
        #print(data)
        #data[:] = states["auv0"]['RangeFinderSensor']

        plot.set_array(data_uav.ravel())

        plt.draw()
        plt.gcf().canvas.flush_events()