import matplotlib.pyplot as plt
import math
import numpy as np
import datetime

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


if __name__ == "__main__":

    fig = Figure(template="default", rows=2, cols=2)
    fig.setTitle("Essai de titre principal")
    fig.addGraph("test", 2, 2, 1)
    fig.graphs["test"].setTitle("sous titre 1")
    fig.graphs["test"].setAxesX(-10, 10, r"axe des x")
    fig.graphs["test"].setAxesY(-5, 5, r"axe des y")
    x = [np.arange(0, 10, 0.1), np.sin(np.arange(0, 10, 0.1))]
    y = [np.sin(np.arange(0, 10, 0.1)), np.arange(0, 10, 0.1)]
    label = ["test legende1", "test legende2"]
    fig.graphs["test"].plotStandart(x, y, label, color='red', linestyle="solid", linewidth=1)
    fig.graphs["test"].setLegend("best")
    """
    fig.addGraph("test2", 2, 2, 2)
    fig.graphs["test2"].setTitle("sous titre 1")
    fig.graphs["test2"].setAxesX(0, 10, r"axe des x")
    fig.graphs["test2"].setAxesY(-3, 3, r"axe des y")
    fig.graphs["test2"].plotStandart(np.arange(0, 10, 0.1), np.sin(np.arange(0, 10, 0.1)), "test legende", color='red', linestyle="solid", linewidth=1)
    fig.graphs["test2"].setLegend("best")
    fig.addGraph("test3", 2, 1, 2)
    fig.graphs["test3"].setTitle("sous titre 1")
    fig.graphs["test3"].setAxesX(0, 10, r"axe des x")
    fig.graphs["test3"].setAxesY(-3, 3, r"axe des y")
    fig.graphs["test3"].plotStandart(np.arange(0, 10, 0.1), np.sin(np.arange(0, 10, 0.1)), "test legende", color='red', linestyle="solid", linewidth=1)
    fig.graphs["test3"].setLegend("best")
    """
    fig.figSave("testtt")
"""
    fig1 = Figure(template="default", rows=1, cols=1)
    fig1.addGraph("test", 1, 1, 1)
    fig1.graphs["test"].setTitle("sous titre 1")
    fig1.graphs["test"].setAxesX(0, 10, r"axe des x")
    fig1.graphs["test"].setAxesY(-3, 3, r"axe des y")
    fig1.graphs["test"].plotStandart(np.arange(0, 10, 0.1), np.sin(np.arange(0, 10, 0.1)), "test legende", color='red', linestyle="solid", linewidth=1)
    fig1.graphs["test"].setLegend("best")
    fig1.figSave("testttttt")
    """

"""
def parameters(plot = None, x_span = None, y_span = None, title = None, x_label = None, y_label = None):
    plot.tick_params(axis='both', which='major', labelsize=20)
    if title:
        plot.title.set_text(title)

    # pt = taille de la police des axes (chiffres) et des labels
    pt=25

    if x_label:
        plot.set_xlabel(x_label, fontsize=pt)
    if y_label:
        plot.set_ylabel(y_label, fontsize=pt)

    # enlever les bords noirs en haut et à droite
    plot.spines['top'].set_visible(False)
    plot.spines['right'].set_visible(False)

    if x_span:
        plot.set_xlim(x_span[0], x_span[1])
    if y_span:
        plot.set_ylim(y_span[0], y_span[1])


def graph_1_1(x, y):
    ptx = 11 # ptx = largueur de la figure que vous enregistrez
    pty = 8 # pty = hauteur (...)
    plt.close('all')
    plt.rcParams['figure.figsize'] = [ptx, pty]
    fig, ax = plt.subplots() # générer la figure

    parameters(ax, x_span=[0, 20], y_span=[-1.1, 1.1], x_label=r"$\mathrm{t\ [s]}$", y_label=r"$\mathrm{y(t)\ [-]}$")
    ax.plot(x, y, color = 'blue', linestyle = 'solid', linewidth = 1, label=[r'$y_1(t)$'])
    #ax.legend(loc='upper right', fontsize=20)

    index = "1_1"
    figname = "fig_"+index+".pdf" 
    plt.savefig(figname)
"""


