# DataFrame Basic
Instroduce the dataframe provided by Pandas module in general.  
Here are the samples will be convered in this tutorial 
* Reading CSV file content into dataframe
* Index data in dataframe
* Get column by name
* Sorting data by column
* Normalize the data by column
* Sum the data in dataframe
* Add new column into dataframe

## Reading data into dataframe 
```python  
# Import pandas
import pandas

# Read in the world_alcohol.csv data from earlier.
world_alcohol = pandas.read_csv("world_alcohol.csv")
food_info = pandas.read_csv("food_info.csv")
```