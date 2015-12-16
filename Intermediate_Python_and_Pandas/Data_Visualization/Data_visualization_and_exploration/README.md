# Data visualization and exploration  
In this article, we will show the DataFrame function to do basic data visualization and exploration  
## Show histogram chart  
Every numeric column can be used to generate such kind of chart. You can specify the total intervals using the bins parameter. Following code bins=50, it means the value of clumn "Sample_size" will be splitted into equlation of 50 sgement, and then dataframe will count the number of records in each segment and show up
```python  
recent_grads.hist(column=["Sample_size"], bins=50)
```
## Show box plot 
box plot显示一个柱状图，这个柱状图显示的是最小值，最大值和均值。分类是根据by参数指定的column进行的
```python  
# Select just `Sample_size` & `Major_category` columns from `recent_grads` 
# Name the resulting DataFrame as `sample_size`
sample_size = recent_grads[['Sample_size', 'Major_category']]

# Run the `boxplot()` function on `sample_size` DataFrame and specify, as a parameter, 
# that we'd like a box and whisker diagram to be generated for each unique `Major_category`
sample_size.boxplot(by='Major_category')

# Format the resulting plot to make the x-axis labels (each `Major_category` value) 
# appear vertically instead of horizontally (by rotating 90 degrees)
plt.xticks(rotation=90)
```  
## Show multiple charts in one picture  
```python
plt.scatter(recent_grads['Unemployment_rate'], recent_grads['P25th'], color='red')
plt.scatter(recent_grads['ShareWomen'], recent_grads['P25th'], color='blue')
plt.show()
```