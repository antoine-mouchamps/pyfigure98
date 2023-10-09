from .Graph import Graph

from ._template_handling import getAllTemplates
import matplotlib.pyplot as plt
import matplotlib


class Figure:
    """Class containing everything needed in order to create complex figures
    with pultiple plots.

    Methods:
    ========

    Add*
    ----

    *   ``addGraph``
    *   ``addCustomTemplate``
    *   ``addFigure``

    Set*
    ----

    *   ``setTitle``

    Fig*
    ----

    *   ``figSave``
    *   ``figShow``

    """

    def __init__(self) -> None:
        """Create a new figure.

        Begin by calling the ``addFigure`` method in order to create the
        figure. If you want to, create a custom template by using
        ``addCustomTemplate`` before creating the figure.
        """
        self.graphs: dict[str, Graph]
        self.graphs = dict()

        self.templates: dict[str, dict]
        self.templates = getAllTemplates()

        self.fig: matplotlib.figure.Figure

    # from ._template_handling import addCustomTemplate

    from ._set_figure import setTitle, figSave, figShow
    from ._set_figure import addFigure, addGraph
