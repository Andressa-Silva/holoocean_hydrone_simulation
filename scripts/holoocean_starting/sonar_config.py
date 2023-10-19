import holoocean
import matplotlib.pyplot as plt
import numpy as np

class sonar():

    def __init__(self, scenario):
        self.scenario = scenario

    def sonar_config(self):

        self.config = holoocean.packagemanager.get_scenario(self.scenario)
        config      = self.config['agents'][0]['sensors'][-1]["configuration"]
        self.minR   = config['RangeMin']
        self.maxR   = config['RangeMax']
        self.binsR  = config['RangeBins']

    def plot_graph(self):
        plt.ion()

        t = np.arange(0,50)
        minR = self.minR   
        maxR = self.maxR   
        binsR = self.binsR  
        r = np.linspace(minR, maxR, binsR)
        T, R = np.meshgrid(t, r)
        data = np.zeros_like(R)

        plt.grid(False)
        plot = plt.pcolormesh(T, R, data, cmap='gray', shading='auto', vmin=0, vmax=1)
        plt.tight_layout()
        plt.gcf().canvas.flush_events()
        


        

    
