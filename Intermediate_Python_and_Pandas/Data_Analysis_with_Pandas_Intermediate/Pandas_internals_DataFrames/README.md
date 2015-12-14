# Pandas internals: DataFrames  
## Set custom index for dataframe  
You can use ```set_index()``` method to set the custom index for a dataframe  
```python
fandango = pd.read_csv('fandango_score_comparison.csv')
#Using the FILM column value as the custom index, then you can access the dataframe data using this new custom index
#inplace parameter means don't create a new dataframe object, just override the old one
#drop, if drop=True, the column used as custom index will be dropped from the dataframe
fandango_films = fandango.set_index(fandango["FILM"], inplace=False, drop=False)
```  
## Select data using custom index
[Please check](../Dataframe_basics/README.md#Index data in dataframe)  
## Apply function through DataFrame Columns  
Because dataframe represents each row / column with Series object, and Series object supports the vectoring operation, so we can use apply method to calcualte the value for each column and row, in this section, we will talk about going through columns first  
* If the function returns one value for whole column, then the apply method will return a Series object, each element in the Series represents the function return value for one column
* if the function returns a new value for each element in the column, the apply function will return a new dataframe object.  
```python
import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))
# this code will return a new dataframe object
halved_df = float_df.apply(lambda x: x/2)
```  
## Apply function through DataFrame rows  
Just like apply function to DateFrame columns, you can make the function runs over the rows, just put ```axis=1``` when you call apply method.  
```python
rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_deviations = rt_mt_user.apply(lambda x: np.std(x), axis=1)
rt_mt_means = rt_mt_user.apply(lambda x: np.mean(x), axis=1)
```