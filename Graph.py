from dependencies import *

class Figure:
    
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
