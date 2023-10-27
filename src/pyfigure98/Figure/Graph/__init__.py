import matplotlib.pyplot as plt

from .._place_holder import Figure_
from .._place_holder import Graph_


class Graph(Graph_):
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

    def __init__(self, fig: Figure_,
                 subPlot: plt.Axes
                 ) -> None:
        super().__init__(fig, subPlot)


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
    from ._plot_methods import setScale, plotVectorField
