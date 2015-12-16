# Creating compelling plot with Seaborn  
Seaborn is a library in python to create the attractive plot. Seaborn is based on the matplotlib, but make a lot of enhancement to make it easy to create the attractive plots by using simple code. When the seaborn is loaded into code, it automatically update all default stylying used by matplotlib, so you will get better look and feel for all normal style.  
Below are some samples for using the Seaborn library.  
## Show historic diagram  
```python
sns.distplot(births['prglngth'], kde=True)

# set the style for seabornm and set the label for x and y
sns.set_style('dark')
sns.distplot(births['birthord'], kde=False)
sns.axlabel('Birth number', 'Frequency')
```
## boxplot  
```python
births = pd.read_csv('births.csv')
sns.boxplot(x="birthord", y="agepreg", data=births)
```  
## pairplot  
```python
# this call will generated 9 diagrams, 
# they are agepreg vs agepreg, agepreg vs prglngth, agepreg vs birthord....
sns.pairplot(data=births,vars=["agepreg", "prglngth", "birthord"])
```