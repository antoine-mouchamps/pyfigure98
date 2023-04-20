import matplotlib.pyplot as plt
import matplotlib

class Figure:
    def __init__(self):
        self.graphs:dict[str, Graph_]

        self.templates:dict[str, dict]

        self.fig:matplotlib.figure.Figure

class Graph_:
    def __init__(self, fig:Figure, subPlot:plt.Axes):
        self.fig:Figure
        self.plot:plt.Axes
        self.plot_labels = [[], []]

        self._x_axis_params:dict[str, bool]

        self._y_axis_params:dict[str, bool]

        self._is_legend_plotted:bool
        self._mappable:bool