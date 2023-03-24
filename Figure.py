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
        template_default["x_label_size"] = 25
        template_default["y_label_size"] = 25
        template_default["x_tick_size"] = 20
        template_default["y_tick_size"] = 20
        template_default["legend_size"] = 20
        template_default["in_text_size"] = 15
        template_default["subplot_title_size"] = 30
        template_default["fig_title_size"] = 35
        template_default["markersize"] = 10
        template_default["x_tick_width_major"] = 2.25
        template_default["x_tick_length_major"] = 5
        template_default["x_tick_width_minor"] = 1.75
        template_default["x_tick_length_minor"] = 3
        template_default["y_tick_width_major"] = 2.25
        template_default["y_tick_length_major"] = 5
        template_default["y_tick_width_minor"] = 1.75
        template_default["y_tick_length_minor"] = 3        

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
                          x_label_size:int = 25, 
                          y_label_size:int = 25, 
                          x_tick_size:int = 20, 
                          y_tick_size:int = 20, 
                          legend_size:int = 20, 
                          in_text_size:int = 15,
                          subplot_title_size:int = 30,
                          fig_title_size:int = 35, 
                          markersize:int = 10,
                          x_tick_width_major:float = 2.25,
                          x_tick_length_major:float = 5,
                          x_tick_width_minor:float = 1.75,
                          x_tick_length_minor:float = 3,
                          y_tick_width_major:float = 2.25,
                          y_tick_length_major:float = 5,
                          y_tick_width_minor:float = 1.75,
                          y_tick_length_minor:float = 3,
                          ) -> None:
        """Create a custom template;

        Parameters
        ----------

        *   ``name``: name of the template.
        *   ``fig_size_x``: default x size of a figure when there is only one plot.
        *   ``fig_size_y``: default y size of a figure when there is only one plot.
        *   ``x_label_size``: size of the label of the x axis.
        *   ``y_label_size``: size of the label of the y axis.
        *   ``x_tick_size``: size of the tick numbers of the x axis.
        *   ``y_tick_size``: size of the tick numbers of the y axis.
        *   ``legend_size``: size of the text used in the legend.
        *   ``subplot_title_size``: size of the subtitles. 
        *   ``fig_title_size``: size of the title of the figure.
        *   ``markersize``: size of the marker point.
        *   ``in_text_size``: size of the texts inside the graph.
        *   ``x_tick_width_major``: width of the major line next to the tick label of the x axis. 
        *   ``x_tick_length_major``: length of the major line next to the tick label of the x axis. 
        *   ``x_tick_width_minor``: width of the minor line next to the tick label of the x axis. 
        *   ``x_tick_length_minor``: length of the minor line next to the tick label of the x axis. 
        *   ``y_tick_width_major``: width of the major line next to the tick label of the y axis.
        *   ``y_tick_length_major``: length of the major line next to the tick label of the y axis.
        *   ``y_tick_width_minor``: width of the minor line next to the tick label of the y axis.
        *   ``y_tick_length_minor``: length of the minor line next to the tick label of the y axis.
        """
    
        template_custom = dict()
        template_custom["fig_size_x"] = fig_size_x
        template_custom["fig_size_y"] = fig_size_y
        template_custom["x_label_size"] = x_label_size
        template_custom["y_label_size"] = y_label_size
        template_custom["x_tick_size"] = x_tick_size
        template_custom["y_tick_size"] = y_tick_size
        template_custom["legend_size"] = legend_size
        template_custom["subplot_title_size"] = subplot_title_size
        template_custom["fig_title_size"] = fig_title_size
        template_custom["markersize"] = markersize
        template_custom["in_text_size"] = in_text_size
        template_custom["x_tick_width_major"] = x_tick_width_major
        template_custom["x_tick_length_major"] = x_tick_length_major
        template_custom["x_tick_width_minor"] = x_tick_width_minor
        template_custom["x_tick_length_minor"] = x_tick_length_minor
        template_custom["y_tick_width_major"] = y_tick_width_major
        template_custom["y_tick_length_major"] = y_tick_length_major
        template_custom["y_tick_width_minor"] = y_tick_width_minor
        template_custom["y_tick_length_minor"] = y_tick_length_minor

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

        if rows > 1:
                x_size = self.template["fig_size_x"]*cols
        else:
            x_size = self.template["fig_size_x"]
        if cols > 1:
            y_size = self.template["fig_size_y"]*rows
        else:
            y_size = self.template["fig_size_y"]

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
        self.fig.suptitle(title, fontsize=self.template["fig_title_size"])

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
        

    def setGrid(self):
        """Add grid lines to the graph
        """
        self.plot.grid()

    def setAxisX(self, x_min:float, x_max:float, label:str = None, color:list = ['black', False], loc:str='center'):
        """Set the labels and the interval of the X axis of the current graph.

        Parameters
        ----------

        *   ``x_min``: the lower bound of the axis.
        *   ``x_max``: upper bound of the axis.
        *   ``label``: name of the axis (don't forget the units !).
        *   ```tick_each``: interval between each tick.
        *   ``color``: color of the label.
        *   ``loc``: location of the label ('left', 'center', 'right').

        """
        if label != None:
            self.plot.set_xlabel(label, color=color[0], loc=loc, fontsize=self.fig.template["x_label_size"])
        self.plot.tick_params(axis='x', which='major', labelsize=self.fig.template["x_tick_size"], width=self.fig.template["x_tick_width_major"], length=self.fig.template["x_tick_length_major"])
        self.plot.tick_params(axis='x', which='minor', width=self.fig.template["x_tick_width_minor"], length=self.fig.template["x_tick_length_minor"])
        if(color[1]):
            self.plot.tick_params(axis='x', which='major', colors=color[0])
        self.plot.set_xlim([x_min, x_max])

    def setAxisXAngularScale(self, span:float = 1.0):
        """Change the x axis to a multiple of pi axis.

        Parameters
        ----------

        *   ``span``: set the span between two ticks.
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

    def setAxisY(self, y_min:int, y_max:int, label:str = None, color:list = ['black', False], loc:str='center'):
        """Set the labels and the interval of the Y axis of the current graph.

        Parameters
        ----------

        *   ``x_min``: the lower bound of the axis.
        *   ``x_max``: upper bound of the axis.
        *   ``label``: name of the axis (don't forget the units !).
        *   ``color``: color of the label.
        *   ``loc``: location of the label ('top', 'center', 'bottom').
        
        """
        if label != None:
            self.plot.set_ylabel(label, color=color[0], loc=loc, fontsize=self.fig.template["y_label_size"])
        if(color[1]):
            self.plot.tick_params(axis='y', which='major', colors=color[0])
        self.plot.tick_params(axis='y', which='major', labelsize=self.fig.template["y_tick_size"], width=self.fig.template["y_tick_width_major"], length=self.fig.template["y_tick_length_major"])
        self.plot.tick_params(axis='y', which='minor', width=self.fig.template["y_tick_width_minor"], length=self.fig.template["y_tick_length_minor"])
        self.plot.set_ylim([y_min, y_max])

    def setAxisYAngularScale(self, span:float = 1.0):
        """Change the y axis to a multiple of pi axis.

        Parameters
        ----------

        *   ``span``: set the span between two ticks.
        """
        self.__y_axis_params["angular"] = True
        self.plot.yaxis.set_major_formatter(tick.FormatStrFormatter('%g$\pi$'))
        self.plot.yaxis.set_major_locator(tick.MultipleLocator(base=span))

    def setAxisYLogScale(self):
        """Change the y axis to a base 10 logarithm scale.
        """
        self.__y_axis_params["log"] = True

    def setAxisYSecondAxis(self, y_min:int, y_max:int, label:str = None, color:list = ['black', False], loc:str='center'):
        """Create and set the labels and the interval of the second Y axis of the current graph.

        Parameters
        ----------

        *   ``x_min``: the lower bound of the axis
        *   ``x_max``: upper bound of the axis
        *   ``label``: name of the axis (don't forget the units !)
        *   ``color``: color of the label.
        *   ``loc``: location of the label ('top', 'center', 'bottom').
        
        """
        self.__y_axis_params["second"] = True
        self.secondYAxis = self.plot.twinx()
        if label != None:
            self.secondYAxis.set_ylabel(label, color=color[0], loc=loc, fontsize=self.fig.template["y_label_size"])
        if(color[1]):
            self.secondYAxis.tick_params(axis='y', which='major', colors=color[0])
        self.secondYAxis.tick_params(axis='y', which='major', labelsize=self.fig.template["y_tick_size"])
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

        *   ``loc``: location of the legend (best, lower/upper/# + left/right/center)
        
        """
        
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
        
        plot_axis = self.plot
        if(axis =="sec"):
            plot_axis = self.secondYAxis
        return plot_axis
    
    def plotStandard(self, x:list, y:list, label:str = None, axis:str="main", color='blue', linestyle='solid', linewidth=1):
        """Plot datas with a standard "line" graph.

        Parameters
        ----------

        *   ``x``: list of the x values.
        *   ``y``: list of the y values.
        *   ``label``: label of the plot, used in the legend (if needed).
        *   ``color``: color of the plot.
        *   ``linestyle``: style (solid, dashed, dotted, ...).
        *   ``linewidth``: width of the plot.

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

    def plotPointsWithText(self, xs:list, ys:list, texts:list, axis:str="main", marker:str = 'o', color:str = "green"):

        plot_axis = self.__axis_formatter(axis)
        if (not(len(xs) == len(ys) and len(texts) == len(xs))):
            raise TypeError("xs and ys must have the same dimensions !")

        for (x, y, text) in zip(xs, ys, texts):
            plot_axis.text(x, y, text, fontdict={'fontsize': self.fig.template["in_text_size"]})
            plot_axis.plot(x, y, marker=marker, markersize = self.fig.template["markersize"], color=color, label='_nolegend_')
