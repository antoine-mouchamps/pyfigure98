from ._place_holder import Figure_
from .Chart import Chart
import matplotlib.pyplot as plt
# import warnings


def addFigure(self: Figure_,
              template: str = "default",
              rows: int = 1,
              cols: int = 1
              ) -> None:
    """Create a new figure.

    Parameters
    ----------

    *   ``template``: Set the template used by the figure, i.e. all the font
        sizes used by the different components.
    *   ``rows``: Set the horizontal size of the figure by multiplying the
        default size of a plot (found in the template used) by this value.
        ``rows`` should thus be equal to the maximum amount of plots that will
        be placed horizontally.
    *   ``cols``: Set the vertical size of the figure by multiplying the
        default size of a plot (found in the template used) by this value.
        ``cols`` should thus be equal to the maximum amount of plots that will
        be placed vertically.
    """

    if(template in self.templates):
        self.template = self.templates[template]
    else:
        raise NameError("The template'", template, "'does not exist.")

    x_size = self.template["fig_size_x"]*cols
    y_size = self.template["fig_size_y"]*rows
    self.fig = plt.figure(figsize=(x_size, y_size))

    # warnings.warn("New figure created")


def addChart(self: Figure_,
             name: str,
             row: int = 1,
             col: int = 1,
             index: int = 1) -> Chart:
    """Add a chart to the current figure.

    Parameters:
    --------

    *   ``name``: name of the chart, used to recognize this specific chart
    *   ``row``: row number
    *   ``col``: column number
    *   ``index``: location of the chart

    Details:
    --------
    Explanation: specify the location and size of the chart on the figure.
    The row and col parameters determine the size of the grid, like if the
    figure was a table. Then, the index parameter specify in which block of
    the table the added chart has to go starting from the upper left corner
    and ending at the lower right. \n
    /!\\ the table system doesn't actually exist, it is only there to give a
    position and a size to the added chart. It is thus possible to use
    different size for different charts. For example when using a 2x2 grid,
    plotting two charts with (2,2,1) and (2,2,2) with a third one (2,1,2) will
    gives the following structure: \n
    _______\n
    |__|__|\n
    |_____|
    """
    new_chart = Chart(self, self.fig.add_subplot(row, col, index))
    self.charts[name] = new_chart

    # warnings.warn(f'Chart "{name}" created')
    return self.charts[name]


def setTitle(self: Figure_, title: str) -> None:
    """Set the main title of the figure.

    Parameters
    ----------

    *   ``title``: well, obvious

    """
    self.fig.suptitle(title+"\n", fontsize=self.template["fig_title_size"])


def figSave(self: Figure_, name: str) -> None:
    """Save the figure to pdf format.

    Parameters
    ----------

    *   ``name``: figure saved as "name.pdf"

    """
    self.fig.tight_layout()
    self.fig.savefig(name+".pdf", bbox_inches='tight')
    # warnings.warn(f'Figure saved as "{name+".pdf"}"')


def figShow(self: Figure_):
    """Don't remember

    """
    self.fig.tight_layout()
    plt.show()


def addGraph(self: Figure_,
             name: str,
             row: int = 1,
             col: int = 1,
             index: int = 1) -> Chart:
    """Add a chart to the current figure.

    WARNING: THIS METHOD IS DEPRECATED !
    --------
    Use `addChart()` instead.
    """
    
    return addChart(self, name, row, col, index)