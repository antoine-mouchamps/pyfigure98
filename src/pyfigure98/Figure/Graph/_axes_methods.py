from .._place_holder import Graph_
from typing import Literal, Union

import datetime
import matplotlib.ticker as tick
import matplotlib.pyplot as plt


def setAxisX(self: Graph_, x_min: Union[int, float, None] = None,
             x_max: Union[int, float, None] = None,
             label: Union[str, None] = None, color: list = ['black', False],
             loc: Literal['center', 'right', 'left']= 'center'
             ):
    """Set the labels and the interval of the X axis of the current graph.

    Parameters
    ----------

    *   ``x_min``: (OPTIONNAL) the lower bound of the axis.
    *   ``x_max``: (OPTIONNAL) upper bound of the axis.
    *   ``label``: (OPTIONNAL) name of the axis (don't forget the units !).
    *   ``color``: (OPTIONNAL) color of the label.
    *   ``loc``: (OPTIONNAL) location of the label ('left', 'center', 'right').

    """
    if label is not None:
        self.plot.set_xlabel(label, color=color[0], loc=loc,
                             fontsize=self.fig.template["label_size"])
    self.plot.tick_params(axis='x', which='major',
                          labelsize=self.fig.template["tick_size"],
                          width=self.fig.template["tick_width_major"],
                          length=self.fig.template["tick_length_major"]
                          )
    self.plot.tick_params(axis='x', which='minor',
                          labelsize=self.fig.template["tick_size"],
                          width=self.fig.template["tick_width_minor"],
                          length=self.fig.template["tick_length_minor"]
                          )
    if(color[1]):
        self.plot.tick_params(axis='x', which='major', colors=color[0])
    if(x_min is not None and x_max is not None):
        self.plot.set_xlim(x_min, x_max)


def setAxisXAngularScale(self: Graph_, span: float = 1.0):
    """Change the x axis to a multiple of pi axis.

    Parameters
    ----------

    *   ``span``: (DEF=1) set the span between two ticks.
    """
    self._x_axis_params["angular"] = True
    self.plot.xaxis.set_major_formatter(tick.FormatStrFormatter('%g$\\pi$'))
    self.plot.xaxis.set_major_locator(tick.MultipleLocator(base=span))


def setAxisXLogScale(self: Graph_):
    """Change the x axis to a base 10 logarithm scale.
    """
    self._x_axis_params["log"] = True


def setAxisXTimeScale(self: Graph_):
    """ Set the X axis as a time axis in hh:mm:ss.
    """

    self._x_axis_params["time"] = True

    def timeTicks(xx, pos):
        d = datetime.timedelta(seconds=xx)
        return str(d)

    self.plot.yaxis.get_offset_text().set_fontsize(25)
    self.plot.ticklabel_format(scilimits=(0, 0))
    formatter = tick.FuncFormatter(timeTicks)
    self.plot.xaxis.set_major_formatter(formatter)

    plt.setp(self.plot.xaxis.get_majorticklabels(),
             rotation=-30,
             ha="left", rotation_mode="anchor"
             )


def setAxisY(self: Graph_,
             y_min: Union[int, float, None] = None,
             y_max: Union[int, float, None] = None,
             label: Union[str, None] = None,
             color: list = ['black', False],
             loc: Literal['bottom', 'center', 'top'] = 'center'
             ):
    """Set the labels and the interval of the Y axis of the current graph.

    Parameters
    ----------

    *   ``x_min``: (OPTIONNAL) the lower bound of the axis.
    *   ``x_max``: (OPTIONNAL) upper bound of the axis.
    *   ``label``: (OPTIONNAL) name of the axis (don't forget the units !).
    *   ``color``: (OPTIONNAL) color of the label.
    *   ``loc``: (OPTIONNAL) location of the label ('top', 'center', 'bottom').

    """
    if label is not None:
        self.plot.set_ylabel(label,
                             color=color[0],
                             loc=loc,
                             fontsize=self.fig.template["label_size"]
                             )
    if(color[1]):
        self.plot.tick_params(axis='y', which='major', colors=color[0])
    self.plot.tick_params(axis='y', which='major',
                          labelsize=self.fig.template["tick_size"],
                          width=self.fig.template["tick_width_major"],
                          length=self.fig.template["tick_length_major"]
                          )
    self.plot.tick_params(axis='y', which='minor',
                          labelsize=self.fig.template["tick_size"],
                          width=self.fig.template["tick_width_minor"],
                          length=self.fig.template["tick_length_minor"]
                          )
    if(y_min is not None and y_max is not None):
        self.plot.set_ylim(y_min, y_max)


def setAxisYAngularScale(self: Graph_, span: float = 1.0):
    """Change the y axis to a multiple of pi axis.

    Parameters
    ----------

    *   ``span``: (DEF = 1) set the span between two ticks.
    """
    self._y_axis_params["angular"] = True
    self.plot.yaxis.set_major_formatter(tick.FormatStrFormatter('%g$\\pi$'))
    self.plot.yaxis.set_major_locator(tick.MultipleLocator(base=span))


def setAxisYLogScale(self: Graph_):
    """Change the y axis to a base 10 logarithm scale.
    """
    self._y_axis_params["log"] = True


def setAxisYSecondAxis(self: Graph_,
                       y_min: Union[int, float, None] = None,
                       y_max: Union[int, float, None] = None,
                       label: Union[str, None] = None,
                       color: list = ['black', False],
                       loc: Literal['bottom', 'center', 'top'] = 'center'
                       ):
    """Create and set the labels and the interval of the second Y axis of the
    current graph.

    Parameters
    ----------

    *   ``x_min``: (OPTIONNAL) the lower bound of the axis.
    *   ``x_max``: (OPTIONNAL) upper bound of the axis.
    *   ``label``: (OPTIONNAL) name of the axis (don't forget the units !).
    *   ``color``: (OPTIONNAL) color of the label.
    *   ``loc``: (OPTIONNAL) location of the label ('top', 'center', 'bottom').

    """
    self._y_axis_params["second"] = True
    self.secondYAxis = self.plot.twinx()
    if label is not None:
        self.secondYAxis.set_ylabel(label, color=color[0], loc=loc,
                                    fontsize=self.fig.template["label_size"]
                                    )
    if(color[1]):
        self.secondYAxis.tick_params(axis='y', which='major',
                                     colors=color[0])
    self.secondYAxis.tick_params(axis='y', which='major',
                                 labelsize=self.fig.template["tick_size"]
                                 )
    if(y_min is not None and y_max is not None):
        self.secondYAxis.set_ylim(y_min, y_max)
