# Introduction to Matplotlib's internals
Matplotlib provides some lower level object by using which you can control your plot look and feel efficiently. Below is the schematic diagram for the object we will cover in this tutorial  
![Image of matplotlib object](https://docs.google.com/a/neulion.com/drawings/d/1Lnw62xhW7QGkZP7Vcc27dQbidmF-n6Is0CBExWJQvGE/pub?w=480&h=360)  
* Fig is the canvas for matplotlib, all plots are drawn in the fig. You use ``` plt.figure``` method to create the fig object  
* Plot is the place the matplotlib draw the points, you can set the axis ticks (min/max value of axis), axis label, title of plot through different method. It also has method to create different type of plot  
```python
import numpy as np

month = [1,1,2,2,4,5,5,7,8,10,10,11,12,12]
temperature = [32,15,40,35,50,55,52,80,85,60,57,45,35,105]

# using figsize parameter to specify the width and height of a figure
fig = plt.figure(figsize=(5,7))
# add_subplot is the key method to add the plot into figure, the parameter for this method are
# (nrow, ncol, plot_index), you can have nrow * ncol plots in the figure, and plot_index starts from 1, and count by row first, then column
ax = fig.add_subplot(1,1,1)
# all following methods can be set using one method
# ax.set(xlim=[0,13], ylim=[10, 110], xlabel="Month", ylabel="Temperature", title="Year Round Temperature")
ax.set_xlim([0, 13])
ax.set_ylim([10, 110])
ax.set_xlabel("Month")
ax.set_ylabel("Temperature")
ax.set_title("Year Round Temperature")

color = 'darkblue'
marker = 'o'

# run the .scatter() method, params: color, marker
# scatter method generates the scatter plot, but give us more control for the plot. Like you can specify the color and the shape for each point
ax.scatter(month, temperature, color='darkblue', marker='o')
plt.show()
```
