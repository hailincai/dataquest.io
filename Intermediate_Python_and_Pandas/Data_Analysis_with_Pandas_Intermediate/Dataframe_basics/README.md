# DataFrame Basic
Instroduce the dataframe provided by Pandas module in general.  
Here are the samples will be convered in this tutorial 
* Reading CSV file content into dataframe
* Index data in dataframe
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

## Index data in dataframe  
There are severals ways of indexing data in dataframe 
* Index data by row / column number  
  This is the easiest way to get the data from dataframe, to do this, you use the **```.iloc```** method. Row / Column number starts with 0 to the len(row/col) - 1. Below are the samples  
```python  
#The food_info data has been loaded in.
#Print the first element in the first row.
#iloc can accpet following types of parameters, the method loc can take the same parameter types
#    an integer
#    list of integers
#    slice object
#    Boolean array --- like filtering
print(food_info.iloc[0,0])

#Print the whole first row.
print(food_info.iloc[0,:])

second_row = food_info.iloc[1,:]
tenth_row = food_info.iloc[9,:]
  ```
* Index data by column name  
If you want to get the whole column data out, you can do this  
```python
#First we can get the names of all the columns (in order)
print(list(food_info.columns.values))

#The we can get a column by name.
print(food_info["Protein_(g)"][0:10])

#And again.
sodium_column = food_info["Sodium_(mg)"]
saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]

#we can also get the data from multiple column at one shot
selenium_and_thiamin = food_info[["Selenium_(mcg)", "Thiamin_(mg)"]]
```
* Index data by row / column index  
This is most tricky one. When the data is loaded into dataframe, each row get a index name ( **If you don't specify, it will be number from 0, if you specify, it can be a string, for example, in pivot_table call, the index name will be the column value of index parameter** ), each column get a index name ( **the csv column name** ). Even you do something like **```dropna()```** to create a new dataframe, the new dataframe will have the same row index / column index number with the old one. You can use **```reset_index(drop=True)```** to reindex the index number for a new generated dataframe. After this call, the index number for each row will start from 0 again, and because ```drop=True```, the index column in new dataframe will be removed.  
Access data by row / column index is done by **```loc```** method  
```python
food_info.loc[3,"Sodium_(mg)"]
titanic_survival.loc[3,["Sodium_(mg)", "FA_Sat_(g)"]]
```  
## Sorting data by column  
```python  
#The food at the first row will be the one with the least fat.
#If there is a tie (several foods have no fat), it will be the food with 0 fat and the least sodium.
ascending_fat_then_ascending_sodium = food_info.sort(["Lipid_Tot_(g)", "Sodium_(mg)"], ascending=[True, True])

#It's different than what we got when we just sorted on fat
print(ascending_fat_then_ascending_sodium.iloc[0,:])

#The food at the first row will be the one that has the most sodium, out of all the foods with 0 fat.
ascending_fat_then_descending_sodium = food_info.sort(["Lipid_Tot_(g)", "Sodium_(mg)"], ascending=[True, False])

#Unsurprisingly, this is table salt
print(ascending_fat_then_descending_sodium.iloc[0,:])

ascending_sugar_then_descending_zinc = food_info.sort(["Sugar_Tot_(g)", "Zinc_(mg)"], ascending=[True, False])
descending_cholesterol_then_ascending_protein = food_info.sort(["Cholestrl_(mg)", "Protein_(g)"], ascending=[False, True])
``` 
## Normalize the data by column 
The reason we need to normalize the data are
* the unit for each column is different, so the real value for each column makes no sense to compare. For example, in our tutorial data set ( the USDA nurtrition table ), the Protein unit is g, and the Vitamin unit is mg. 
* The number for each column can have big different. So column data range is 100--1000, some column data range is 0.1-----0.5. 
To normalize the data, the easist way is do this for each cell, do cell_value / max_valu_of_column, then every column will have value from 0 --- 1 
```python 
normalized_protein = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
normalized_lipid_tot = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
``` 
## Sum the data in dataframe 
When you call the ```sum``` method, you can pass in an ```axis``` parameter. If **axis=0**, it means sum based on column, if **axis=1**, it means sum based on row. So in our example, if **axis=0**, it means sum for each row ( means each food ), if **axis=1***, it means sum for the column for all rows ( means one column for all foods ) 
```python
column_list = ['Fiber_TD_(g)', 'Sugar_Tot_(g)']

#Let's sum the amount of fiber and sugar in each of the foods.
row_total = food_info[column_list].sum(axis=1)

#This gives us a sum for each row in the data
print(row_total)

#Let's sum up the total amount of fiber and sugar across all the foods.
column_total = food_info[column_list].sum(axis=0)
print(column_total)
```