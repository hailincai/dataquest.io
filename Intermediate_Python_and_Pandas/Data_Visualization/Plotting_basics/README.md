# Ploting Basic  
In this article, we will introduce the ```matplotlib``` and instroduce some basic plot operation based on the forest fire data  
## Create scatter plot 
Use method ```scatter``` to create scatter plot
```python
import matplotlib.pyplot as plt
# The forest fire data has been loaded into the forest_fires variable as a pandas dataframe.
# We can plot the X column from the dataframe against the Y column.
# This will show us the spatial positions of all the fires on a 10x10 grid.
plt.scatter(forest_fires["X"], forest_fires["Y"])
plt.show()
# first parameter is for axis x, second parameter is for axis y
plt.scatter(forest_fires["wind"], forest_fires["area"])
plt.show()
plt.scatter(forest_fires["temp"], forest_fires["area"])
plt.show()
```  
## Create a line chart  
Line plot is same as scatter plot, the difference is just line plot will connect all points to a line. Use ```plot``` method to create line chart  
```python
import matplotlib.pyplot as plt
# The above plot looks much better!
forest_fires = forest_fires.sort(["rain"])
plt.plot(forest_fires["rain"], forest_fires["area"])
plt.show()
forest_fires = forest_fires.sort(["wind"])
plt.plot(forest_fires["wind"], forest_fires["area"])
plt.show()
```  
## Set the axis label and plot title  
```python
plt.scatter(forest_fires["wind"], forest_fires["area"])
plt.xlabel("Wind speed when fire started")
plt.ylabel("Area consumed by fire")
plt.title("Wind speed vs fire area")
plt.show()
```  
## Set the slot style  
The matplotlib has a lot of predefined style we can use to beatify our chart  
```python
# Print all available styles
print(plt.style.available)

# Use the ggplot style for plotting
plt.style.use('ggplot')
```  
## Make a bar chart  
Bar chart normally makes the aggregation result  based on something  
```python
import matplotlib.pyplot as plt
import numpy
# The pivot_table method will return a new array containing a summary of the data.
# This pivot table will have the Y position of the fire as the index, and the average area of forest burned per fire as the values.
# It will return a vector, or one dimensional array.
area_by_y = forest_fires.pivot_table(index="Y", values="area", aggfunc=numpy.mean)

# This gets the index values of the vector, in this case, the sorted y positions
y_index = area_by_y.index
plt.bar(y_index, area_by_y)
plt.show()

# This makes a similar plot for the X positions.
area_by_x = forest_fires.pivot_table(index="X", values="area", aggfunc=numpy.mean)
plt.bar(area_by_x.index, area_by_x)
plt.show()
```