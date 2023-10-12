# Pyfigure98
## _A python package to create plots and figures easily_

![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/antoine-mouchamps/pyfigure98)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/m/antoine-mouchamps/pyfigure98)
![GitHub issues](https://img.shields.io/github/issues/antoine-mouchamps/pyfigure98)

![PyPI - Version](https://img.shields.io/pypi/v/pyfigure98)
![PyPI - License](https://img.shields.io/pypi/l/pyfigure98)

If you have ever tried to make figures in python, you may have faced the same issues that annoyed me: a lot of copy/pasting between projects, countless hours spent on the internet searching for _how to change the size of this or that thing again ?_ and always searching for specific things like axes formated specifficaly for angles, logarithms, times, ...

With this project, no more hurdles.

---

# Features

This project is based on `matplotlib` and contains many methods to facilitate the creation of complex figures. Here is a non-exaustive list of its functionalities:
- Hability to put multiple graphs on a single figure.
- Hability to have more than one _y-axis_.
- Hability to format the _x-axis_ to measure time, angles and logarithmic scales.
- Hability to format de _y-axis_ to measure angles and logarithmic scales.
- Automated and unified font sizes, defined in [templates](https://github.com/antoine-mouchamps/pyfigure98/tree/dev#templates).
- And many more !

---

# Documentation

## Usage

### Installation
To install this package using [pip](https://pip.pypa.io/en/stable/installation/), simply run
```sh
pip install pyfigure98
```
In order to use this package, create a new `Figure` object, and add a new figure to it:
```py
    from pyfigure98 import Figure
    import numpy as np # Used later
    
    myNewFigure = Figure()
    myNewFigure.addFigure(template="default", rows=1, cols=1)
```

> For more informations on how to use the `template` variable and how to modify templates, see [section](https://github.com/antoine-mouchamps/pyfigure98/tree/dev#templates).

Next, you can add a new graph to your newly-created figure:
```py
graphOfMyNewFigure = myNewFigure.addgraph("myGraph")
```
Modify the _x-axis_ and _y-axis_ by using these methods:
```py
graphOfMyNewFigure.setAxisX(x_min=-10, x_max=10, label="x")
graphOfMyNewFigure.setAxisY(y_min=-5, y_max=10, label="f(x)")
```
Add a plot by using:
```py
x = np.arange(-10, 10, 0.2)
y = (0.3*x)**3
graphOfMyNewFigure.plotStandard(x=x, y=y, label="example with f(x)=0.3*x^3", color="red")
```
Don't forget to add a title and a legend !
```py
myNewFigure.setTitle("My figure")
graphOfMyNewFigure.setTitle("my graph")
graphOfMyNewFigure.setLegend()
```
Finally, save you figure:
```py
myNewFigure.figSave('myfig')
```
After all these steps, you should obtain this:

<img src="https://github.com/antoine-mouchamps/pyfigure98/assets/94292445/daba562f-6ae2-40fb-b5ae-e6a3509d18a7" width="500">

> This example is, of course, trivial.
> But it illustrates the basic principles of this package.


Of course, there are many more methods available !
## Templates

---

# Examples

---

# 


