import matplotlib.pyplot as plt
import math
import numpy as np
import datetime
import matplotlib.ticker as tick


class Figure:
    """Class containing everything needed in order to create complex figures with pultiple plots.

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
    
    
    def __template_default(self) -> dict:
        template_default = dict()
        template_default["fig_size_x"] = 11
        template_default["fig_size_y"] = 8
        template_default["label_size"] = 25
        template_default["tick_size"] = 20
        template_default["legend_size"] = 20
        template_default["in_text_size"] = 20
        template_default["subplot_title_size"] = 30
        template_default["fig_title_size"] = 35
        template_default["markersize"] = 10
        template_default["tick_width_major"] = 2.25
        template_default["tick_length_major"] = 5
        template_default["tick_width_minor"] = 1.75
        template_default["tick_length_minor"] = 3        

        return template_default
    
    
    def __init__(self) -> None:
        """Create a new figure.

        Begin by calling the ``addFigure`` method in order to create the figure.
        If you want to, create a custom template by using ``addCustomTemplate`` before creating the figure.
        """
        self.graphs:dict[str, Graph]
        self.graphs = dict()

        self.templates:dict[str, dict]
        self.templates = dict()
        self.templates["default"] = self.__template_default()
        
    def addCustomTemplate(self, 
                          name:str, 
                          fig_size_x:int = 11, 
                          fig_size_y:int = 8, 
                          label_size:int = 25, 
                          tick_size:int = 20, 
                          legend_size:int = 20, 
                          in_text_size:int = 20,
                          subplot_title_size:int = 30,
                          fig_title_size:int = 35, 
                          markersize:int = 10,
                          tick_width_major:float = 2.25,
                          tick_length_major:float = 5,
                          tick_width_minor:float = 1.75,
                          tick_length_minor:float = 3,
                          ) -> None:
        """Create a custom template;

        Parameters
        ----------

        *   ``name``: name of the template.
        *   ``fig_size_x``: default x size of a figure when there is only one plot.
        *   ``fig_size_y``: default y size of a figure when there is only one plot.
        *   ``label_size``: size of the labels of the axis.
        *   ``tick_size``: size of the tick numbers of the axis.
        *   ``legend_size``: size of the text used in the legend.
        *   ``subplot_title_size``: size of the subtitles. 
        *   ``fig_title_size``: size of the title of the figure.
        *   ``markersize``: size of the marker point.
        *   ``in_text_size``: size of the texts inside the graph.
        *   ``tick_width_major``: width of the major line next to the tick label of the axis. 
        *   ``tick_length_major``: length of the major line next to the tick label of the axis. 
        *   ``tick_width_minor``: width of the minor line next to the tick label of the axis. 
        *   ``tick_length_minor``: length of the minor line next to the tick label of the axis. 
        """
    
        template_custom = dict()
        template_custom["fig_size_x"] = fig_size_x
        template_custom["fig_size_y"] = fig_size_y
        template_custom["label_size"] = label_size
        template_custom["tick_size"] = tick_size
        template_custom["legend_size"] = legend_size
        template_custom["subplot_title_size"] = subplot_title_size
        template_custom["fig_title_size"] = fig_title_size
        template_custom["markersize"] = markersize
        template_custom["in_text_size"] = in_text_size
        template_custom["tick_width_major"] = tick_width_major
        template_custom["tick_length_major"] = tick_length_major
        template_custom["tick_width_minor"] = tick_width_minor
        template_custom["tick_length_minor"] = tick_length_minor

        self.custom_templates[name] = template_custom

    def addFigure(self, template:str = "default", rows:int = 1, cols:int = 1) -> None:
        """Create a new figure.

        Parameters
        ----------

        *   ``template``: Set the template used by the figure, i.e. all the font sizes used by the different components.
        *   ``rows``: Set the horizontal size of the figure by multiplying the default size of a plot (found in the template used) by this
        value. ``rows`` should thus be equal to the maximum amount of plots that will be placed horizontally.
        *   ``cols``: Set the vertical size of the figure by multiplying the default size of a plot (found in the template used) by this
        value. ``col`` should thus be equal to the maximum amount of plots that will be placed vertically.
        """

        if(template in self.templates):
            self.template = self.templates[template]
        else:
            raise NameError("The template "+template+"does not exist.")

        x_size = self.template["fig_size_x"]*cols
        y_size = self.template["fig_size_y"]*rows
        self.fig = plt.figure(figsize = (x_size, y_size))

    def addGraph(self, name:str, row:int = 1, col:int = 1, index:int = 1):
        """Add a graph to the current figure. 

        Parameters:
        --------

        *   ``name``: name of the graph, used to recognize this specific graph
        *   ``row``: row number
        *   ``col``: column number
        *   ``index``: location of the graph

        Details:
        --------
        Explanation: specify the location and size of the graph on the figure. The row and col parameters determine the size of the grid,
        like if the figure was a table. Then, the index parameter specify in which block of the table the added graph has to go
        starting from the upper left corner and ending at the lower right. \n
        /!\ the table system doesn't actually exist, it is only there to give a position and a size to the added graph.
        """
        new_graph = Graph(self, self.fig.add_subplot(row, col, index))
        self.graphs[name] = new_graph

        return self.graphs[name]

    def setTitle(self, title:str) -> None:
        """Set the main title of the figure.

        Parameters
        ----------
        
        *   ``title``: well, obvious
        
        """
        self.fig.suptitle(title+"\n", fontsize=self.template["fig_title_size"])

    def figSave(self, name:str) -> None:
        """Save the figure to pdf format.

        Parameters
        ----------

        *   ``name``: figure saved as "name.pdf"
        
        """
        self.fig.tight_layout()
        self.fig.savefig(name+".pdf", bbox_inches='tight')
    
    def figShow(self):
        """Don't remember
        
        """
        self.fig.tight_layout()
        plt.show()

class Graph:
    """Class containing everything in order to create a complete graph on a figure.

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
    def __init__(self, fig:Figure, subPlot:plt.Axes) -> None:
        self.fig = fig
        self.plot = subPlot
        self.plot_labels = [[], []]

        self.__x_axis_params:dict[str, bool]
        self.__x_axis_params = dict()

        self.__y_axis_params:dict[str, bool]
        self.__y_axis_params = dict()

        self.__is_legend_plotted = False
        self.__mappable = None
        

    def setGrid(self):
        """Add grid lines to the graph
        """
        self.plot.grid()

    def setAxisX(self, x_min:float=None, x_max:float=None, label:str = None, color:list = ['black', False], loc:str='center'):
        """Set the labels and the interval of the X axis of the current graph.

        Parameters
        ----------

        *   ``x_min``: (OPTIONNAL) the lower bound of the axis.
        *   ``x_max``: (OPTIONNAL) upper bound of the axis.
        *   ``label``: (OPTIONNAL) name of the axis (don't forget the units !).
        *   ``color``: (OPTIONNAL) color of the label.
        *   ``loc``: (OPTIONNAL) location of the label ('left', 'center', 'right').

        """
        if label != None:
            self.plot.set_xlabel(label, color=color[0], loc=loc, fontsize=self.fig.template["label_size"])
        self.plot.tick_params(axis='x', which='major', labelsize=self.fig.template["tick_size"], width=self.fig.template["tick_width_major"], length=self.fig.template["tick_length_major"])
        self.plot.tick_params(axis='x', which='minor', width=self.fig.template["tick_width_minor"], length=self.fig.template["tick_length_minor"])
        if(color[1]):
            self.plot.tick_params(axis='x', which='major', colors=color[0])
        if(not(x_min == None and x_max == None)):
            self.plot.set_xlim([x_min, x_max])

    def setAxisXAngularScale(self, span:float = 1.0):
        """Change the x axis to a multiple of pi axis.

        Parameters
        ----------

        *   ``span``: (DEF=1) set the span between two ticks.
        """
        self.__x_axis_params["angular"] = True
        self.plot.xaxis.set_major_formatter(tick.FormatStrFormatter('%g$\pi$'))
        self.plot.xaxis.set_major_locator(tick.MultipleLocator(base=span))

    def setAxisXLogScale(self):
        """Change the x axis to a base 10 logarithm scale.
        """
        self.__x_axis_params["log"] = True

    def setAxisXTimeScale(self):
        """ Set the X axis as a time axis in hh:mm:ss.
        """
        
        self.__x_axis_params["time"] = True

        def timeTicks(xx, pos):
            d = datetime.timedelta(seconds=xx)
            return str(d)
        
        self.plot.yaxis.get_offset_text().set_fontsize(25)
        self.plot.ticklabel_format(scilimits=(0, 0))
        formatter = tick.FuncFormatter(timeTicks)
        self.plot.xaxis.set_major_formatter(formatter)

        plt.setp(self.plot.xaxis.get_majorticklabels(), rotation=-30, ha="left", rotation_mode="anchor") 

    def setAxisY(self, y_min:float=None, y_max:float=None, label:str = None, color:list = ['black', False], loc:str='center'):
        """Set the labels and the interval of the Y axis of the current graph.

        Parameters
        ----------

        *   ``x_min``: (OPTIONNAL) the lower bound of the axis.
        *   ``x_max``: (OPTIONNAL) upper bound of the axis.
        *   ``label``: (OPTIONNAL) name of the axis (don't forget the units !).
        *   ``color``: (OPTIONNAL) color of the label.
        *   ``loc``: (OPTIONNAL) location of the label ('top', 'center', 'bottom').
        
        """
        if label != None:
            self.plot.set_ylabel(label, color=color[0], loc=loc, fontsize=self.fig.template["label_size"])
        if(color[1]):
            self.plot.tick_params(axis='y', which='major', colors=color[0])
        self.plot.tick_params(axis='y', which='major', labelsize=self.fig.template["tick_size"], width=self.fig.template["tick_width_major"], length=self.fig.template["tick_length_major"])
        self.plot.tick_params(axis='y', which='minor', width=self.fig.template["tick_width_minor"], length=self.fig.template["tick_length_minor"])
        if(not(y_min == None and y_max == None)):
            self.plot.set_ylim([y_min, y_max])

    def setAxisYAngularScale(self, span:float = 1.0):
        """Change the y axis to a multiple of pi axis.

        Parameters
        ----------

        *   ``span``: (DEF=1) set the span between two ticks.
        """
        self.__y_axis_params["angular"] = True
        self.plot.yaxis.set_major_formatter(tick.FormatStrFormatter('%g$\pi$'))
        self.plot.yaxis.set_major_locator(tick.MultipleLocator(base=span))

    def setAxisYLogScale(self):
        """Change the y axis to a base 10 logarithm scale.
        """
        self.__y_axis_params["log"] = True

    def setAxisYSecondAxis(self, y_min:int=None, y_max:int=None, label:str = None, color:list = ['black', False], loc:str='center'):
        """Create and set the labels and the interval of the second Y axis of the current graph.

        Parameters
        ----------

        *   ``x_min``: (OPTIONNAL) the lower bound of the axis.
        *   ``x_max``: (OPTIONNAL) upper bound of the axis.
        *   ``label``: (OPTIONNAL) name of the axis (don't forget the units !).
        *   ``color``: (OPTIONNAL) color of the label.
        *   ``loc``: (OPTIONNAL) location of the label ('top', 'center', 'bottom').
        
        """
        self.__y_axis_params["second"] = True
        self.secondYAxis = self.plot.twinx()
        if label != None:
            self.secondYAxis.set_ylabel(label, color=color[0], loc=loc, fontsize=self.fig.template["label_size"])
        if(color[1]):
            self.secondYAxis.tick_params(axis='y', which='major', colors=color[0])
        self.secondYAxis.tick_params(axis='y', which='major', labelsize=self.fig.template["tick_size"])
        self.secondYAxis.set_ylim([y_min, y_max])

    def setTitle(self, label:str):
        """Set the title of the current graph.

        Parameters
        ----------

        *   ``label``: title of the graph
        
        """
        self.plot.set_title(label, fontsize = self.fig.template["subplot_title_size"])

    def setLegend(self, loc:str = "best"):
        """Set the legend of the current graph.

        Parameters
        ----------

        *   ``loc``: (OPTIONNAL) location of the legend (best, lower/upper/# + left/right/center)
        
        """
        self.__is_legend_plotted = True
        self.plot.legend(self.plot_labels[0], self.plot_labels[1], loc=loc, fontsize=self.fig.template["legend_size"])

    def setBorders(self, config:str = None,left:bool = True, right:bool = True, top:bool = True, bottom:bool = True):
        """Set the 4 borders of the graph.
        Set ``config`` to "upper-right" to disable the right and upper border.
        
        Parameters
        ----------

        *   ``config``: presets
        *   ``left``: enable the left border.
        *   ``right``: enable the right border.
        *   ``top``: enable the top border.
        *   ``bottom``: enable the bottom border.
        """
        if(config == "upper-right"):
            self.plot.spines['top'].set_visible(False)
            self.plot.spines['right'].set_visible(False)
        else:
            self.plot.spines['top'].set_visible(top)
            self.plot.spines['bottom'].set_visible(bottom)
            self.plot.spines['left'].set_visible(left)
            self.plot.spines['right'].set_visible(right)

    def __X_Y_formatter(self, x, y):
        if (not(len(x) == len(y))):
            raise TypeError("x and y must have the same dimensions !")
        
        if(len(self.__x_axis_params) > 1):
            raise SyntaxError("the X axis cannot have more than one formatter !")
        if(len(self.__y_axis_params) > 1):
            raise SyntaxError("the Y axis cannot have more than one formatter !")
        
        if("angular" in self.__x_axis_params):
            x /=np.pi
        
        if("angular" in self.__y_axis_params):
            y /=np.pi

        if("log" in self.__x_axis_params and "log" in self.__y_axis_params):
            print("\n \t!!! WARNING: This case in not taken into account, not sure if it will work as intended \n")

        return x, y
    
    def __axis_formatter(self, axis)->plt.Axes:
        if(not(axis == "main" or axis =="sec")):
           raise SyntaxError("The specified axis does not exist !")
        
        if self.__is_legend_plotted == True:
            print("WARNING: the legend is already plotted so anything plotted afterwards will not have its label shown.")

        plot_axis = self.plot
        if(axis =="sec"):
            plot_axis = self.secondYAxis
        return plot_axis
    
    def plotStandard(self, axis:str="main", x:list=None, y:list=None, label:str=None, color='blue', linestyle='solid', linewidth=1):
        """Plot datas with a standard "line" graph.

        Parameters
        ----------

        *   ``axis``: (DEF=main) axis on which to plot ("main" or "sec").
        *   ``x``: list of the x values.
        *   ``y``: list of the y values.
        *   ``label``: (OPTIONNAL) label of the plot, used in the legend (if needed).
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

        x, y = self.__X_Y_formatter(x, y)
        plot_axis = self.__axis_formatter(axis)

        if(label == None):
            label = "_nolegend"
        plotted = False
        if(plotted == False and ("log" in self.__x_axis_params and "log" not in self.__y_axis_params)):
            print("heeeeeee")
            line, = plot_axis.semilogx(x, y, color=color, linestyle=linestyle, linewidth=linewidth)
            plotted = True

        elif(plotted == False and ("log" in self.__y_axis_params and "log" not in self.__x_axis_params)):
            line, = plot_axis.semilogy(x, y, color=color, linestyle=linestyle, linewidth=linewidth)
            plotted = True

        if(plotted == False):
            line, = plot_axis.plot(x, y, color=color, linestyle=linestyle, linewidth=linewidth)
            plotted = True
        
        if(not (label == None)):
            self.plot_labels[0].append(line)
            self.plot_labels[1].append(label)

    def plotPointsWithText(self, axis:str="main", xs:list=None, ys:list=None, texts:list=None, marker:str = 'o', markercolor:str = "green", color:str = "black"):
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

        plot_axis = self.__axis_formatter(axis)
        if (not(x.shape == y.shape)):
            raise TypeError("x "+x.shape+" and y "+y.shape+" must have the same dimensions !")

        for (x, y, text) in zip(xs, ys, texts):
            plot_axis.text(x, y, text, fontdict={'fontsize': self.fig.template["in_text_size"]}, color=color)
            plot_axis.plot(x, y, marker=marker, markersize = self.fig.template["markersize"], color=markercolor, label='_nolegend_')

    def plotText(self, axis:str="main", x=None, y=None, text:str=None, color:str="black"):
        """Plot text on the graph.

        Parameters
        ----------

        *   ``axis``: (DEF=main) axis on which to plot ("main" or "sec").
        *   ``x``:  x at which to plot the points/texts.
        *   ``y``:  y at which to plot the points/texts.
        *   ``text``: text to plot.
        *   ``color``: (OPTIONNAL) color of the text.
        """

        plot_axis = self.__axis_formatter(axis)

        plot_axis.text(x, y, text, fontdict={'fontsize': self.fig.template["in_text_size"]}, color=color)

    def plotPcolor(self, axis:str="main", grid_span:float=1.0, C=None, vmin=None, vmax=None, cmap:str='inferno', shading:str='flat'):
        """Plot a graph where the colour indicates the greatness of the value on a 2D grid. Not easy to describe okay ??

        Parameters
        ----------

        *   ``axis``: (DEF=main) axis on which to plot ("main" or "sec").
        *   ``grid_span``:  (OPTIONNAL, DEF=1) span between each element on the x and y axis (multiply each tick by this value). 
            Default: 1, 2, 3, 4, ...
        *   ``C``: Array to plot. Must be 2D where the first dimension corresponds to the x axis and the second one to the y axis.
        The value at ij is plotted at the coordinates (x;y).
        *   ``vmin``: (OPTIONNAL) minimum value to take into account in the color scale.
        *   ``vmax``: (OPTIONNAL) maximum value to take into account in the color scale.
        *   ``cmap``: (OPTIONNAL) colors of the colorbar
        *   ``shading``: (OPTIONNAL, DEF='flat')\n
            'flat' => boxes \n
            'nearest' => boxes whose ticks are centered at the center of the boxes \n
            'gouraud' => smooth transition between colors.

        """

        if(not(C.ndim == 2)):
            raise TypeError("C must a 2D array !") 
        
        if(vmin == None):
            vmin = C.min()
        if(vmax == None):
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
        
        plot_axis = self.__axis_formatter(axis)
        self.__mappable = plot_axis.pcolormesh(X, Y, C, cmap=cmap, vmin=vmin, vmax=vmax, shading=shading)
    
    def plotCbar(self, label=None, orientation:str="vertical"):
        """
        
        Parameters
        ----------

        *   ``label``:
        *   ``orientation``:
        """

        if orientation == "horizontal":
            cbar = self.fig.fig.colorbar(mappable=self.__mappable, orientation="horizontal")
            cbar.set_label(label, rotation=0, size=self.fig.template["label_size"])
        else:
            cbar = self.fig.fig.colorbar(mappable=self.__mappable, orientation="vertical")
            cbar.set_label(label, rotation=270, labelpad=30, size=self.fig.template["label_size"])
        cbar.ax.tick_params(labelsize=self.fig.template["tick_size"])

    def setScale(self, axis:str="main", scaling:str="same"):
        """Set the scale of the x and y axes.

        Parameters
        ----------

        *   ``axis``: (DEF="main") axis on which to plot ("main" or "sec").
        *   ``scaling``: (DEF="same"): "same": same scaling for x and y.
        
        """

        plot_axis = self.__axis_formatter(axis)
        if(scaling == "same"):
            plot_axis.set_aspect('equal', 'box')
        else:
            raise ValueError('"'+scaling+'" is is not a valid scaling !')
        
    def plotVectorField(self, axis:str="main", x=None, y=None, grid_span:float=1.0, color:str="black"):
        """Plot a vector field, perfect for fluid streams.

        Parameters
        ----------

        *   ``axis``: (DEF="main") axis on which to plot ("main" or "sec").
        *   ``x``: values of the x components of the vectors.
        *   ``y``: values of the y components of the vectors.
        *   ``grid_span``: (OPTIONNAL, DEF=1) span between each element on the x and y axis (multiply each tick by this value). 
        
        """

        self.__X_Y_formatter(x, y)

        x_vec = np.arange(0, len(x[0]), 1, dtype=float)
        y_vec = np.arange(0, len(x), 1, dtype=float)
        X, Y = np.meshgrid(x_vec, y_vec)

        X = X*grid_span
        Y = Y*grid_span

        plot_axis = self.__axis_formatter(axis)
        plot_axis.streamplot(X, Y, x, y, color=color, linewidth=1, density=1)
        
if __name__ == "__main__":
    pass


