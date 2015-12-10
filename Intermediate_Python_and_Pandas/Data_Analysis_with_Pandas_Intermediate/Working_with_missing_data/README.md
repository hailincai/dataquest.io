# Working with missing data and advanced features
In the real world, when we load the data from csv file into dataframe, some column may have missing data. In Pandas module, it call the missing data is NaN. In this series, we will go through the thing we need to know to handle the missing data. And we also introduce some new features like pivot table, and how to call a function for all coulmns / rows. The dataset used by this series will be "Titannic" data.
## Find out missing data 
Pandas module has a static method called **```isnull```**, you can use this method to find out which row has missing data, or determine the cell has missing data or not. 
```python 
#We can use the isnull function to find which values in a column are missing
#age_null will be a vector, the value for each element will be True or False
#if the value is True, it means that row has NaN value
age_null = pd.isnull(titanic_survival["age"])
#get the first row of age column
cell_is_null = pd.isnull(titanic_survival["age"][0])
```
For Pandas module, some method will automatically filter out the NaN data when it go through all the data, for example, the **```mean```** method  
```python
#this line of code will calculate the average age for all Titanic passgengers
#and mean method take out NaN data automatically
titantic_survival["age"].mean()
```
## Drop missing value  
Pandas module provide **```dropna```** to drop the row which contains the NaN value.  
```python
import pandas as pd

#Drop all rows that have missing values
new_titanic_survival = titanic_survival.dropna()

#It looks like we have an empty dataframe now.
#This is because every row has at least one missing value.
print(new_titanic_survival)

#We can also use the axis argument to drop columns that have missing values
new_titanic_survival = titanic_survival.dropna(axis=1)
print(new_titanic_survival)

#We can use the subset argument to only drop rows if certain columns have missing values.
#This drops all rows where "age" or "sex" is missing.
new_titanic_survival = titanic_survival.dropna(subset=["age", "sex"])
print(new_titanic_survival)

new_titanic_survival = titanic_survival.dropna(subset=["age", "body", "home.dest"])
```
## Making pivot tables  
Pivot table means aggregation table based on some columns 
```python
import numpy as np

# This will compute the mean survival chance and the mean age for each passenger class
# index is the group column
# values is a aggregation column list
passenger_survival = titanic_survival.pivot_table(index="pclass", values=["age", "survived"], aggfunc=np.mean)
print(passenger_survival)
port_stats = titanic_survival.pivot_table(index="embarked", values=["age", "survived", "fare"], aggfunc=np.mean)
```
## Apply a function for all coulmns  
```python
import pandas as pd

# Let's look at a simple example.
# This function counts the number of null values in a series
def null_count(column):
    # Make a vector that contains True if null, False if not.
    column_null = pd.isnull(column)
    # Create a new vector with only values where the series is null.
    null = column[column_null == True]
    # Return the count of null values.
    return len(null)

def not_null_count(column):
    column_null = pd.isnull(column)
    not_null = column[column_null == False]
    return len(not_null)

# Compute null counts for each column
column_null_count = titanic_survival.apply(null_count)
print(column_null_count)

column_not_null_count = titanic_survival.apply(not_null_count)
```
## Apply a function for all rows  
```python
# This function will check if a row is an entry for a minor (under 18), or not.
def is_minor(row):
    if row["age"] < 18:
        return True
    else:
        return False

# This is a boolean series with the same length as the number of rows in titanic_survival
# Each entry is True if the row at the same position is a record for a minor
# The axis of 1 specifies that it will iterate over rows, not columns
minors = titanic_survival.apply(is_minor, axis=1)
import pandas as pd

def generate_age_label(row):
    age = row["age"]
    if pd.isnull(age):
        return "unknown"
    elif age < 18:
        return "minor"
    else:
        return "adult"

age_labels = titanic_survival.apply(generate_age_label, axis=1)
```