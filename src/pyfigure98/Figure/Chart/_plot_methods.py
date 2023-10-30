from typing import Iterable, Literal
from .._place_holder import Chart_

import numpy as np
import matplotlib.pyplot as plt
import warnings
from typing import Union


def __X_Y_formatter(self: Chart_, x, y):
    if (not(len(x) == len(y))):
        raise TypeError("x and y must have the same dimensions !")

    if(len(self._x_axis_params) > 1):
        raise SyntaxError("the X axis cannot have more than one formatter !")
    if(len(self._y_axis_params) > 1):
        raise SyntaxError("the Y axis cannot have more than one formatter !")

    if("angular" in self._x_axis_params):
        x = [el/np.pi for el in x]

    if("angular" in self._y_axis_params):
        y = [el/np.pi for el in y]

    if("log" in self._x_axis_params and "log" in self._y_axis_params):
        warnings.warn("""\n \t!!! WARNING: This case in not taken into account,
                      not sure if it will work as intended \n""",
                      SyntaxWarning
                      )

    return x, y


def __axis_formatter(self: Chart_, axis) -> plt.Axes:
    if(not(axis == "main" or axis == "sec")):
        raise SyntaxError("The specified axis does not exist !")

    if self._is_legend_plotted is True:
        warnings.warn("""WARNING: the legend is already plotted so anything
                      plotted afterwards will not have its label shown.""",
                      SyntaxWarning
                      )

    plot_axis = self.plot
    if(axis == "sec"):
        plot_axis = self.secondYAxis
    return plot_axis


def plotStandard(self: Chart_, axis: str = "main",
                 x = None,
                 y = None,
                 label: Union[str, None] = None,
                 color='blue',
                 linestyle='solid', linewidth=1
                 ):
    """Plot datas with a standard "line" chart.

    Parameters
    ----------

    *   ``axis``: (DEF=main) axis on which to plot ("main" or "sec").
    *   ``x``: list of the x values.
    *   ``y``: list of the y values.
    *   ``label``: (OPTIONNAL) label of the plot, used in the legend
                    (if needed).
    *   ``color``: (OPTIONNAL) color of the plot.
    *   ``linestyle``: (OPTIONNAL) style (solid, dashed, dotted, ...).
    *   ``linewidth``: (OPTIONNAL) width of the plot.

    Possibilities
    -------------
        b : blue
        g : green
        r : red
        c : cyan
        m : magenta
        y : yellow
        k : black
        w : white
        . : point
        o : circle
        x : x-mark
        +: plus
        *: star
        s : square
        d : diamond
        ^ : triangle (up)
        v : triangle (down)
        < : triangle (left)
        > : triangle (right)
        p : pentagram
        h : hexagram
        -: solid
        -- : dashed
        : : dotted
        -. : dashdot
        (none) : no line

    """

    x, y = __X_Y_formatter(self, x, y)
    plot_axis = __axis_formatter(self, axis)

    if(label is None):
        label = "_nolegend"

    plotted = False
    if(plotted is False
       and "log" in self._x_axis_params
       and "log" not in self._y_axis_params
       ):
        line, = plot_axis.semilogx(x, y, color=color, linestyle=linestyle,
                                   linewidth=linewidth
                                   )
        plotted = True

    elif(plotted is False
         and "log" in self._y_axis_params
         and "log" not in self._x_axis_params
         ):
        line, = plot_axis.semilogy(x, y, color=color, linestyle=linestyle,
                                   linewidth=linewidth
                                   )
        plotted = True

    else:
        line, = plot_axis.plot(x, y, color=color, linestyle=linestyle,
                               linewidth=linewidth
                               )
        plotted = True

    self.plot_labels[0].append(line)
    self.plot_labels[1].append(label)


def plotPointsWithText(self: Chart_, axis: str = "main",
                       xs = None,
                       ys = None,
                       texts = None, marker: str = 'o',
                       markercolor: str = "green", color: str = "black",
                       label = None
                       ):
    """Plot a point with some text attached to it.

    Parameters
    ----------

    *   ``axis``: (DEF=main) axis on which to plot ("main" or "sec").
    *   ``xs``: list of the x at which to plot the points/texts.
    *   ``ys``: list of the y at which to plot the points/texts.
    *   ``texts``: list of the texts to plot.
    *   ``marker``: (OPTIONNAL) which marker to use.
    *   ``markercolor``: (OPTIONNAL) color of the marker.
    *   ``color``: (OPTIONNAL) color of the text.
    """

    xs, ys = __X_Y_formatter(self, xs, ys)
    plot_axis = __axis_formatter(self, axis)

    if(xs is not None and ys is not None):
        line = None
        if(texts == None):
            texts = ["" for a in xs]
        for (x, y, text) in zip(xs, ys, texts):
            plot_axis.text(x, y, text,
                        fontdict={
                            'fontsize': self.fig.template["in_text_size"]
                            },
                        color=color
                        )
            line_i, = plot_axis.plot(x, y, marker=marker,
                        markersize=self.fig.template["markersize"],
                        color=markercolor, label='_nolegend_'
                        )
            if(line is None):
                line = line_i
        if(label is None):
            label = "_nolegend"
        self.plot_labels[0].append(line)
        self.plot_labels[1].append(label)


def plotText(self: Chart_, axis: str = "main",
             x = None,
             y = None,
             text = None, color: str = "black"
             ):
    """Plot text on the chart.

    Parameters
    ----------

    *   ``axis``: (DEF=main) axis on which to plot ("main" or "sec").
    *   ``x``:  x at which to plot the points/texts.
    *   ``y``:  y at which to plot the points/texts.
    *   ``text``: text to plot.
    *   ``color``: (OPTIONNAL) color of the text.
    """

    plot_axis = __axis_formatter(self, axis)

    if(text is None):
        text = ''
    
    if(x is not None and y is not None):
        plot_axis.text(x, y, text,
                    fontdict={'fontsize': self.fig.template["in_text_size"]},
                    color=color
                    )


def plotPcolor(self: Chart_, axis: str = "main", grid_span: float = 1.0,
               C=None, vmin=None, vmax=None, cmap: str = 'inferno',
               shading: Literal['flat', 'nearest', 'gouraud', 'auto'] = 'flat'
               ):
    """Plot a chart where the colour indicates the greatness of the value on a
        2D grid. Not easy to describe okay ??

    Parameters
    ----------

    *   ``axis``: (DEF=main) axis on which to plot ("main" or "sec").
    *   ``grid_span``:  (OPTIONNAL, DEF=1) span between each element on the x
                        and y axis (multiply each tick by this value).
        Default: 1, 2, 3, 4, ...
    *   ``C``: Array to plot. Must be 2D where the first dimension corresponds
                to the x axis and the second one to the y axis.
    The value at ij is plotted at the coordinates (x;y).
    *   ``vmin``: (OPTIONNAL) minimum value to take into account in the color
                    scale.
    *   ``vmax``: (OPTIONNAL) maximum value to take into account in the color
                    scale.
    *   ``cmap``: (OPTIONNAL) colors of the colorbar
    *   ``shading``: (OPTIONNAL, DEF='flat')\n
        'flat' => boxes \n
        'nearest' => boxes whose ticks are centered at the center of
                    the boxes \n
        'gouraud' => smooth transition between colors.

    """

    if(C is not None):
        if(not(C.ndim == 2)):
            raise TypeError("C must a 2D array !")

        if(vmin is None):
            vmin = C.min()
        if(vmax is None):
            vmax = C.max()

        if shading == "flat":
            x_vec = np.arange(0, len(C[0])+1, 1, dtype=float)
            y_vec = np.arange(0, len(C)+1, 1, dtype=float)
        else:
            x_vec = np.arange(0, len(C[0]), 1, dtype=float)
            y_vec = np.arange(0, len(C), 1, dtype=float)
        X, Y = np.meshgrid(x_vec, y_vec)

        X = X*grid_span
        Y = Y*grid_span

        plot_axis = __axis_formatter(self, axis)
        self._mappable = plot_axis.pcolormesh(X, Y, C, cmap=cmap, vmin=vmin,
                                            vmax=vmax, shading=shading
                                            )


def plotCbar(self: Chart_, label: Union[str, None]=None, orientation: str = "vertical"):
    """

    Parameters
    ----------

    *   ``label``:
    *   ``orientation``:
    """

    if orientation == "horizontal":
        cbar = self.fig.fig.colorbar(mappable=self._mappable,
                                     orientation="horizontal"
                                     )
        if(label is not None):
            cbar.set_label(label, rotation=0,
                        size=self.fig.template["label_size"]
                        )
    else:
        cbar = self.fig.fig.colorbar(mappable=self._mappable,
                                     orientation="vertical"
                                     )
        if(label is not None):
            cbar.set_label(label, rotation=270, labelpad=30,
                           size=self.fig.template["label_size"]
                           )
    cbar.ax.tick_params(labelsize=self.fig.template["tick_size"])


def setScale(self: Chart_, axis: str = "main", scaling: str = "same"):
    """Set the scale of the x and y axes.

    Parameters
    ----------

    *   ``axis``: (DEF="main") axis on which to plot ("main" or "sec").
    *   ``scaling``: (DEF="same"): "same": same scaling for x and y.

    """

    plot_axis = __axis_formatter(self, axis)
    if(scaling == "same"):
        plot_axis.set_aspect('equal', 'box')
    else:
        raise ValueError('"'+scaling+'" is is not a valid scaling !')


def plotVectorField(self: Chart_, axis: str = "main",
                    x = None,
                    y = None,
                    grid_span: float = 1.0, color: str = "black"
                    ):
    """Plot a vector field, perfect for fluid streams.

    Parameters
    ----------

    *   ``axis``: (DEF="main") axis on which to plot ("main" or "sec").
    *   ``x``: values of the x components of the vectors.
    *   ``y``: values of the y components of the vectors.
    *   ``grid_span``: (OPTIONNAL, DEF=1) span between each element on the x
                and y axis (multiply each tick by this value).

    """

    __X_Y_formatter(self, x, y)
    
    if(x is not None and y is not None):
        x_vec = np.arange(0, len(x[0]), 1, dtype=float)
        y_vec = np.arange(0, len(x), 1, dtype=float)
        X, Y = np.meshgrid(x_vec, y_vec)

        X = X*grid_span
        Y = Y*grid_span

        plot_axis = __axis_formatter(self, axis)
        plot_axis.streamplot(X, Y, x, y, color=color, linewidth=1, density=1)
