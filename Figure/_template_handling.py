from ._place_holder import Figure

def template_default() -> dict:
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
