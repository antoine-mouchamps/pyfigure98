from dependencies import *
from Graph import Graph

class Figure:
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
    
    def __init__(self, template:str = "default", ptx:int = 0, pty:int = 0, rows:int = 1, cols:int = 1) -> None:
        if template == "default":
            self.template = self.__template_default()
            print(rows)
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
        else:
            self.fig = plt.figure(figsize = [ptx, pty])

        self.graphs:dict[str, Graph]
        self.graphs = dict()
        

    def addGraph(self, name:str, row:int = 1, col:int = 1, index:int = 1):
        """
        Add a graph to the current figure. 

        name : name of the graph, used to recognize this specific graph
        row : row number
        col : column number
        index : location of the graph

        Explanation: specify the location and size of the graph on the figure. The row and col parameters determine the size of the grid,
        like if the figure was a table. Then, the index parameter specify in which block of the table the added graph has to go
        starting from the upper left corner and ending at the lower right. \n
        /!\ the table system doesn't actually exist, it is only there to give a position and a size to the added graph.
        """
        new_graph = Graph(self, self.fig.add_subplot(row, col, index))
        self.graphs[name] = new_graph

    def setTitle(self, title:str):
        """
        Set the main title of the figure.

        title : well, obvious
        """
        self.fig.suptitle(title, fontsize=self.template["fig_title_size"])

    def figSave(self, name:str):
        """
        Save the figure to pdf format.

        name : figure saved as "name.pdf"
        """
        self.fig.savefig(name+".pdf", bbox_inches='tight')
    
    def figShow(self):
        """
        Don't remember
        """
        self.fig.show()

class Graph:
    def __init__(self, fig:Figure, subPlot:plt.Axes) -> None:
        self.fig = fig
        self.plot = subPlot
        self.plot_labels = []

    def setAxesX(self, x_min:int, x_max:int, label:str = None):
        """
        Set the labels and the interval of the X axis of the current graph.

        x_min : the lower bound of the axis.
        x_max : upper bound of the axis.
        label : name of the axis (don't forget the units !)
        """
        if label != None:
            self.plot.set_xlabel(label, fontsize=self.fig.template["x_label_size"])
        self.plot.tick_params(axis='x', which='major', labelsize=self.fig.template["x_tick_size"])
        self.plot.set_xlim([x_min, x_max])

    def setAxesY(self, y_min:int, y_max:int, label:str = None):
        """
        Set the labels and the interval of the Y axis of the current graph.

        x_min : the lower bound of the axis
        x_max : upper bound of the axis
        label : name of the axis (don't forget the units !)
        """
        if label != None:
            self.plot.set_ylabel(label, fontsize=self.fig.template["y_label_size"])
        self.plot.tick_params(axis='y', which='major', labelsize=self.fig.template["y_tick_size"])
        self.plot.set_ylim([y_min, y_max])

    def setTitle(self, label:str):
        """
        Set the title of the current graph.

        label : title of the graph
        """
        self.plot.set_title(label, fontsize = self.fig.template["subplot_title_size"])

    def setLegend(self, loc:str = "best"):
        """
        Set the legend of the current graph.

        loc : location of the legend (best, lower/upper/# + left/right/center)
        """
        self.plot.legend(self.plot_labels, loc=loc, fontsize=self.fig.template["legend_size"])

    def plotStandart(self, x:list, y:list, label:str = None, **kwargs):
        """
        Plot datas with a standart "line" graph.

        x : list of the x values
        y : list of the y values
        label : label of the plot, used in the legend (if needed)
        kwargs : color, linestyle (solid, dotted, dashed, dashdot, ...), linewidth

        x, y and label can be multi-dimensional if you want to plot multiple data sets. (they all need to have the same first dimension)
        """
        if (not len(x) == len(y)):
            raise TypeError("x and y must have the same dimensions !")
        self.plot.plot(x, y, color=kwargs["color"], linestyle=kwargs["linestyle"], linewidth=kwargs["linewidth"])
        
        if(label == None):
            self.plot_labels.append("")
        else:
            self.plot_labels.append(label)
        raise IndexError("x y and label need to have the same first dimension !")
    
    def plotPointCloud(self, x:list, y:list, label:str, **kwargs):
        pass

