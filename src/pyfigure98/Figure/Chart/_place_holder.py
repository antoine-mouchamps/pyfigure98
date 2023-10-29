import matplotlib.pyplot as plt
from matplotlib.collections import QuadMesh


class Chart__():
    def __init__(self):
        self.plot_labels = [[], []]

        self._x_axis_params: dict[str, bool] = dict()

        self._y_axis_params: dict[str, bool] = dict()

        self._is_legend_plotted: bool = False
        self._mappable: QuadMesh
        
        self.secondYAxis: plt.Axes
