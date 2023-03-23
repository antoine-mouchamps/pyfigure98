from dependencies import *

class Figure:
    """Class containing everything need in order to create complex figures with pultiple plots.

    Methods:
    ========

    Add*
    ----

    *   ``addGraph``

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
        template_default["subplot_title_size"] = 30
        template_default["fig_title_size"] = 35

        return template_default
    
    def __init__(self, template:str = "default",  rows:int = 1, cols:int = 1) -> None:
        """Create a new figure.

        Parameters
        ----------

        *   ``template``: set the template used for the created figure. The template determines the font size of all the different things
        added to it.
        *   ``rows``: Set the horizontal size of the figure by multiplying the default size of a plot (found in the template used) by this
        value. ``rows`` should thus be equal to the maximum amount of plots that will be placed horizontally.
        *   ``cols``: Set the vertical size of the figure by multiplying the default size of a plot (found in the template used) by this
        value. ``col`` should thus be equal to the maximum amount of plots that will be placed vertically.
        """
        if template == "default":
            self.template = self.__template_default()
            if rows > 1:
                x_size = self.template["fig_size_x"]*cols
                print("hein ?")
            else:
                x_size = self.template["fig_size_x"]
            if cols > 1:
                y_size = self.template["fig_size_y"]*rows
            else:
                y_size = self.template["fig_size_y"]

            self.fig = plt.figure(figsize = (x_size, y_size))

        self.graphs:dict[str, Graph]
        self.graphs = dict()
    





    def addGraph(self, name:str, row:int = 1, col:int = 1, index:int = 1) -> None:
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
        self.fig.savefig(name+".pdf", bbox_inches='tight')
    
    def figShow(self):
        """Don't remember
        
        """
        self.fig.show()

class Graph:
    """Class containing everything in order to create a complete graph on a figure.

    Methods:
    ========

    Set*
    ----

        *   ``setAxisX``
        *   ``setAxisY``
        *   ``setTitle``
        *   ``setLegend``

    Plot*
    -----

        *   ``plotStandard``

    """
    def __init__(self, fig:Figure, subPlot:plt.Axes) -> None:
        self.fig = fig
        self.plot = subPlot
        self.plot_labels = []

    def setAxisX(self, x_min:int, x_max:int, label:str = None):
        """Set the labels and the interval of the X axis of the current graph.

        Parameters
        ----------

        *   ``x_min``: the lower bound of the axis.
        *   ``x_max``: upper bound of the axis.
        *   ``label``: name of the axis (don't forget the units !)
        
        """
        if label != None:
            self.plot.set_xlabel(label, fontsize=self.fig.template["x_label_size"])
        self.plot.tick_params(axis='x', which='major', labelsize=self.fig.template["x_tick_size"])
        self.plot.set_xlim([x_min, x_max])

    def setAxisY(self, y_min:int, y_max:int, label:str = None):
        """Set the labels and the interval of the Y axis of the current graph.

        Parameters
        ----------

        *   ``x_min``: the lower bound of the axis
        *   ``x_max``: upper bound of the axis
        *   ``label``: name of the axis (don't forget the units !)
        
        """
        if label != None:
            self.plot.set_ylabel(label, fontsize=self.fig.template["y_label_size"])
        self.plot.tick_params(axis='y', which='major', labelsize=self.fig.template["y_tick_size"])
        self.plot.set_ylim([y_min, y_max])

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
        self.plot.legend(self.plot_labels, loc=loc, fontsize=self.fig.template["legend_size"])

    def plotStandard(self, x:list, y:list, label:str = None, color='blue', linestyle='solid', linewidth=1):
        """Plot datas with a standard "line" graph.

        Parameters
        ----------

        *   ``x``: list of the x values
        *   ``y``: list of the y values
        *   ``label``: label of the plot, used in the legend (if needed)
        *   ``color``: color of the plot
        *   ``linestyle``: style (solid, dashed, dotted, ...)
        *   ``linewidth``: width of the plot

        """
        if (not(len(x) == len(y))):
            raise TypeError("x and y must have the same dimensions !")
        
        self.plot.plot(x, y, color=color, linestyle=linestyle, linewidth=linewidth)
        
        if(label == None):
            self.plot_labels.append("")
        else:
            self.plot_labels.append(label)