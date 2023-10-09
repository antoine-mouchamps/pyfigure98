import matplotlib.pyplot as plt

from .._place_holder import Figure


class Graph:
    """Class containing everything in order to create a complete graph on a
    figure.

    Methods:
    ========

    Set*
    ----

        *   ``setAxisX``
        *   ``setAxisXTimeScale``
        *   ``setAxisXAngularScale``
        *   ``setAxisXLogScale``

        *   ``setAxisY``
        *   ``setAxisYSecondAxis``
        *   ``setAxisYAngularScale``
        *   ``setAxisYLogScale``

        *   ``setTitle``
        *   ``setLegend``
        *   ``setTitle``

    Plot*
    -----

        *   ``plotStandard``
        *   ``plotStandardSecondAxis``

    """

    def __init__(self, fig: Figure,
                 subPlot: plt.Axes) -> None:
        self.fig = fig
        self.plot = subPlot
        self.plot_labels = [[], []]

        self._x_axis_params: dict[str, bool]
        self._x_axis_params = dict()

        self._y_axis_params: dict[str, bool]
        self._y_axis_params = dict()

        self._is_legend_plotted = False
        self._mappable = None

    from ._axes_methods import (
        setAxisX,
        setAxisXAngularScale,
        setAxisXTimeScale,
        setAxisXLogScale
    )
    from ._axes_methods import (
        setAxisY,
        setAxisYAngularScale,
        setAxisYLogScale,
        setAxisYSecondAxis
    )

    from ._graph_methods import (
        setBorders, setGrid, setLegend, setTitle
    )

    from ._plot_methods import plotStandard
    from ._plot_methods import plotCbar, plotPcolor, plotVectorField
    from ._plot_methods import plotText, plotPointsWithText
