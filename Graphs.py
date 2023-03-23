from dependencies import *
from Figure import Figure

if __name__ == "__main__":

    fig = Figure(template="default", rows=2, cols=2)
    fig.setTitle("Essai de titre principal")
    fig.addGraph("test", 2, 2, 1)
    fig.graphs["test"].setTitle("sous titre 1")
    fig.graphs["test"].setAxisX(-10, 10, r"axe des x")
    fig.graphs["test"].setAxisY(-5, 5, r"axe des y")
    x = np.arange(0, 10, 0.1)
    y = np.sin(np.arange(0, 10, 0.1))
    label = "test legende1"
    fig.graphs["test"].plotStandard(np.arange(0, 10, 0.1), y, label, linestyle="solid", linewidth=1)
    fig.graphs["test"].setLegend("best")
    
    fig.addGraph("test2", 2, 2, 2)
    fig.graphs["test2"].setTitle("sous titre 1")
    fig.graphs["test2"].setAxisX(0, 10, r"axe des x")
    fig.graphs["test2"].setAxisY(-3, 3, r"axe des y")
    fig.graphs["test2"].plotStandard(np.arange(0, 10, 0.1), np.sin(np.arange(0, 10, 0.1)), "test legende", color='red', linestyle="solid", linewidth=1)
    fig.graphs["test2"].setLegend("best")
    fig.addGraph("test3", 2, 1, 2)
    fig.graphs["test3"].setTitle("sous titre 1")
    fig.graphs["test3"].setAxisX(0, 10, r"axe des x")
    fig.graphs["test3"].setAxisY(-3, 3, r"axe des y")
    fig.graphs["test3"].plotStandard(np.arange(0, 10, 0.1), np.sin(np.arange(0, 10, 0.1)), "test legende", color='red', linestyle="solid", linewidth=1)
    fig.graphs["test3"].setLegend("best")
    
    fig.figSave("testtt")
"""
    fig1 = Figure(template="default", rows=1, cols=1)
    fig1.addGraph("test", 1, 1, 1)
    fig1.graphs["test"].setTitle("sous titre 1")
    fig1.graphs["test"].setAxisX(0, 10, r"axe des x")
    fig1.graphs["test"].setAxisY(-3, 3, r"axe des y")
    fig1.graphs["test"].plotStandard(np.arange(0, 10, 0.1), np.sin(np.arange(0, 10, 0.1)), "test legende", color='red', linestyle="solid", linewidth=1)
    fig1.graphs["test"].setLegend("best")
    fig1.figSave("testttttt")
    """

"""
def parameters(plot = None, x_span = None, y_span = None, title = None, x_label = None, y_label = None):
    plot.tick_params(axis='both', which='major', labelsize=20)
    if title:
        plot.title.set_text(title)

    # pt = taille de la police des Axis (chiffres) et des labels
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


