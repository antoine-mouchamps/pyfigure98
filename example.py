from pyfigure98 import Figure
import numpy as np

if __name__ == "__main__":
    test = input("What test do you want to run ?\n")

    if(test == "1"):
        new_fig = Figure()
        new_fig.addFigure("default", 3, 2)
        new_fig.setTitle("Exemple des fonctionnalités")
        x = np.arange(-1000, 1000, 0.1)
        y = 0.001*x

        time = new_fig.addGraph("time_example", 3, 2, 1)
        time.plotStandard(x=x, y=y, label="bête truc temporel", color="red")
        time.setAxisX(0, 1000, r"$\mathrm{Temps\, [s]}$")
        time.setAxisXTimeScale()
        time.setAxisY(0, 1, r"$\mathrm{\sin(t)}$")
        time.setTitle("Evolution d'un sinus en fct du temps")
        time.setLegend("upper right")
        time.setBorders("upper-right")

        angular = new_fig.addGraph("angular_view", 3, 2, 2)
        x = np.arange(-3*np.pi, 3*np.pi, 0.01)
        x2 = np.arange(-3*np.pi, 3*np.pi, 0.01)
        y = np.sin(x)
        y2 = np.cos(x)*2
        angular.setAxisX(-3, 3, r"angles [rad]", color=["purple", False])
        angular.setAxisXAngularScale(1)
        angular.setAxisY(-1.5, 1.5, "sin(x)", color=["red", True], loc='top')
        angular.plotStandard(x=x, y=y, label="sin(x)", color="red",
                             linestyle="dashed"
                             )
        angular.setAxisYSecondAxis(-2.5, 2.5, "angle", color=["blue", True],
                                   loc="top"
                                   )
        angular.plotStandard(axis="sec",
                             x=x2, y=y2,
                             label="cos",
                             color="blue",
                             linestyle="dotted",
                             linewidth=3
                             )
        angular.setTitle("sinus and cosinus")
        angular.setGrid()
        angular.setBorders(top=False)
        angular.setLegend(loc="lower center")

        log = new_fig.addGraph("log", 3, 1, 2)
        x = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000,
             2010, 2017]
        y = [68, 81, 71, 244, 151, 200, 615, 809, 824, 2633, 10787,
             11577, 20656]
        log.setAxisX(1900, 2020, "x")
        log.setAxisY(10, 21000, "log(x)")
        log.setAxisYLogScale()
        log.setTitle("logarithm scale")
        log.plotText(x=x[7], y=y[3], text="waw mais que c'est beau !!!")
        label = "surtout ce point là"
        labels = []
        for i in range(len(x)):
            labels.append(label)
        log.plotPointsWithText(xs=x[0:-2], ys=y[0:-2], texts=labels[0:-2])

        log.plotStandard(x=x, y=y, label=r"$\log{x}$")
        log.setLegend()

        color = new_fig.addGraph("color", 3, 2, 5)
        x = np.zeros((10, 10))
        for i in range(len(x[0])):
            x[0][i] = (i/10)
            x[1][i] = (i/10)**2
            x[2][i] = (i/10)**3
            x[3][i] = (i/10)**4
            x[4][i] = 2.7**(i/10)
            x[5][i] = (i/10)**(1/2)

        color.plotPcolor(C=x)
        color.setTitle("test lol")
        color.setAxisX(0, 10, "test lol")
        color.setAxisY(0, 10)

        new_fig.figSave("Examples/example")
