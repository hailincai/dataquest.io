# Pandas internal Series  
In this section, we will go through the Pandas internal data structure called Series. Series is derieved from Numpy array object, so you can do index slicing, filtering, vectorized operation on the series. In Pandas' world, the dataframe column is a Series object.  
## Index for Series  
* Eeach series always has an integer based index ( start from 0 to n-1 ), so you can always slicing the series data by using slicing operation.  
```python
import pandas
fandango = pd.read_csv('fandango_score_comparison.csv')

#when you access the datafram column, returns is a series. By default, series always has integer index to access individual , but you can put other type of index for it
series_film = fandango["FILM"]
series_rt = fandango["RottenTomatoes"]

top5_in_series_file = series_file[0:6]
```  
* You can apply the customized index to a Series object when you creating it by setting index parameter 
```python
from pandas import Series

#the underlying code create a new Series object, the data is the RottenTomatoes Critics, and index now is the film name
series_custom = Series(data=series_rt, index=series_file)
#so we can use film name to access the record now
#following code is slicing using customized index
series_custom[['Minions (2015)', 'Leviathan (2014)']] 
#following code is access the value of one film
series_custom['Minions (2015)']
``` 
## Sorting the Series 
* Sorting the Series by the index 
```python
new_series = custom_series.sort_index()
```
* Sorting the Series by the value 
```python
new_series = custom-series.sort_values()
```  
* Reset the index  
```python
#when following code is running, the new_series will include
#if value in <new list> exists in custom_series, then the value will be copied
#otherwise, the value will be NaN
new_series = custom_series.reindex(<new list>)
```  
## Vectoring operation and Filtering  
* Vectoring operation means you can apply operations like "+/-/*" to the whole Series value just like Series * 7  
* And because you can do vectoring operation, so you can create the filter condition very easy  
```python
# Display
criteria_one = series_custom > 50
criteria_two = series_custom < 75
both_criteria = series_custom[criteria_one & criteria_two]
```