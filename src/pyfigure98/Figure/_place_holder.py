from .Chart._place_holder import Chart__

import matplotlib.pyplot as plt
import matplotlib.figure
import matplotlib


class Figure_:
    def __init__(self):
        self.templates: dict[str, dict]
        self.template: dict

        self.fig: matplotlib.figure.Figure

class Chart_(Chart__):
    def __init__(self, fig: Figure_, subPlot: plt.Axes):
        super().__init__()
        
        self.fig: Figure_ = fig
        self.plot: plt.Axes = subPlot
