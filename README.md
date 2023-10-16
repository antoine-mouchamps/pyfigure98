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
- Automated and unified font sizes, defined in [templates](https://github.com/antoine-mouchamps/pyfigure98#templates).
- And many more !

---

# Documentation

## Installation

To install this package using [pip](https://pip.pypa.io/en/stable/installation/), simply run
```sh
pip install pyfigure98
```

## Usage

In order to use this package, create a new `Figure` object, and add a new figure to it:
```py
    from pyfigure98 import Figure
    import numpy as np # Used later
    
    myNewFigure = Figure()
    myNewFigure.addFigure(template="default", rows=1, cols=1)
```

> For more informations on how to use the `template` variable and how to modify templates, see [section](https://github.com/antoine-mouchamps/pyfigure98#templates).

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

As explained before, the templates are responsible for the unified font sizes and colors (WIP) across different figures. 

### Usage
To use a template, simply specify the ``name`` of the `name.json` like in the usage example described [here](https://github.com/antoine-mouchamps/pyfigure98#usage).

### Add a custom template
Custom templates are supported as well. 
In order to create and use a custom template, proceed as follow:

```py
from pyfigure98 import Figure

myNewFigure = Figure()

myNewFigure.addCustomTemplate("custom")  
myNewFigure.addFigure(template="custom", rows=1, cols=1)
```

Here, the custom template file used is `custom.json`. This file must be located in the same directory as the python script calling that function. So in this example, the structure is as followed:

```
├── myproject
│   ├── figurewithcustomtemplate.py
│   ├── custom.json
```

### Write a custom template

The template needs to be a `.json` file with a specific structure.
<details>
<summary>
    Here you can see the default template file structure.
</summary>

```json
{
    "fig_size_x": 11,
    "fig_size_y": 8,
    "label_size": 25,
    "tick_size": 20,
    "legend_size": 20,
    "in_text_size": 20,
    "subplot_title_size": 30,
    "fig_title_size": 35,
    "markersize": 10,
    "tick_width_major": 2.25,
    "tick_length_major": 5,
    "tick_width_minor": 1.75,
    "tick_length_minor": 3   
}
```
> Code inside `default.json`.
> 
</details>

As you can see, each property has a corresponding value and represents a certain element in a plot. At the end of this section, a table will give you all the different properties and corresponding default values, as well as a description of what these values are used for.

> If a property is not specified in the custom `template.json`, its
> value will be determined by the one defined in `default.json`.
> This way, you do not need to specify every properties in your
> custom file if you only want to change a few of them.




<details>
<summary>
    Here is an overview of all the different template variables and their default value.
</summary>

| Syntax      | Default value | Description |
| :---        |    :----:   |  :---|
| `"fig_size_x"` | 11 | |
| `"fig_size_y"` | 8 | |
| `"label_size"` | 25 | |
| `"tick_size"` | 20 | |
| `"legend_size"` | 20 | |
| `"in_text_size"` | 20 | |
| `"subplot_title_size"` | 30 | |
| `"fig_title_size"` | 35 | |
| `"markersize"` | 10 | |
| `"tick_width_major"` | 2.25 | |
| `"tick_length_major"` | 5 | |
| `"tick_width_minor"` | 1.75 | |
| `"tick_length_minor"` | 3 | |

</details>

---

# Examples

---

# 


