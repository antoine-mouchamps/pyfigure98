import matplotlib.pyplot as plt

class Figure:
    def __init__(self):
        self.graphs:dict[str, Graph_]
        self.graphs = dict()

        self.templates:dict[str, dict]
        self.templates = dict()
        self.templates["default"] = self.__template_default()

class Graph_:
    def __init__(self, fig:Figure, subPlot:plt.Axes):
        self.fig = fig
        self.plot = subPlot
        self.plot_labels = [[], []]

        self._x_axis_params:dict[str, bool]
        self._x_axis_params = dict()

        self._y_axis_params:dict[str, bool]
        self._y_axis_params = dict()

        self._is_legend_plotted = False
        self._mappable = None