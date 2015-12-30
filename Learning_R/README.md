# R Basic
## Basic things  
* assign value to a variable  
```a <- 1```  
* create vector ( vector is a list of same type, **vector index starts from 1** )  
```
vector_1 <- c(1,2,3,4)
# after this, vector_2 will be (2,4,6,8)
vector_2 <- vector_1 * 2
```  
* Find type of variable  
```class(variable)```  
## DataFrame  
* read.csv method  
using read.csv method to load the csv file into a dataframe object 
* create dataframe manually  
```
data.frame(<vector1>,<vector2>...)
```
* data frame index  
```
# this will return a new dataframe, which only include the specified column
dataframe[<columnname>] 
# this will return a new dataframe, which only include the specified row ( means 1 row )
dataframe[<rowindex>,]
#this will return a vector which includes the value of specified column
dataframe[,<columnname>] equivalent to dataframe$<columnname>
```  
* data filtering  
```
# only keep the row which has TRUE in the boolean vector
dataframe[<boolean vector>,] 
```
* translate the column value to different type ( using as.***() method)
```
new_column <- as.character(dataframe$column)
```
## Function  
* Function Definition  
```
func <- function(a,b){
    return (a + b)
}
```
* some useful functions  
  * table(<vector>) --- go through the element in the vector, and count how many times a unique value shown in the vector  
  * substr(<vector>, startIndex, endIndex) --- get the substr for each element in vector, and return a vector, endIndex is included  