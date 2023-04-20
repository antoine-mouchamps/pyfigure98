from .._place_holder import Graph_

def setGrid(self:Graph_):
    """Add grid lines to the graph
    """
    self.plot.grid()

def setTitle(self:Graph_, label:str):
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
    self._is_legend_plotted = True
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