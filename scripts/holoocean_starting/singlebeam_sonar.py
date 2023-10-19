import holoocean
import matplotlib.pyplot as plt
import numpy as np
from sonar_config import *

'''#### GET SONAR CONFIG
scenario = "OpenWater-TorpedoSinglebeamSonar"
config = holoocean.packagemanager.get_scenario(scenario)
config = config['agents'][0]['sensors'][-1]["configuration"]
minR = config['RangeMin']
maxR = config['RangeMax']
binsR = config['RangeBins']

#### GET PLOT READY
plt.ion()

t = np.arange(0,50)
r = np.linspace(minR, maxR, binsR)
T, R = np.meshgrid(t, r)
data = np.zeros_like(R)

plt.grid(False)
plot = plt.pcolormesh(T, R, data, cmap='gray', shading='auto', vmin=0, vmax=1)
plt.tight_layout()
#plt.gca().invert_yaxis()
plt.gcf().canvas.flush_events()'''

scenario = "OpenWater-TorpedoSinglebeamSonar"
sonar_ = sonar(scenario)

#### RUN SIMULATION
command = np.array([0,0,0,0,20])
with holoocean.make('OpenWater-TorpedoSinglebeamSonar') as env:
    for i in range(1000000):
        env.act("auv0", command)
        state = env.tick()

        if 'SinglebeamSonar' in state:
            sonar_.plot_graph()

print("Finished Simulation!")
plt.ioff()
plt.show()