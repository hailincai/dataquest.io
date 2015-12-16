# Challenge: Cleaning data  

## Step 1 Find bad year in the data set  
```python
import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()
true_avengers = avengers[avengers['Year'] >= 1960]
```
## Step 2 Consolidating deaths  
```python
columns = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
true_avengers[columns]
def clean_deaths(row):
    num_deaths = 0
    columns = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
    
    for c in columns:
        death = row[c]
        if pd.isnull(death) or death == 'NO':
            continue
        elif death == 'YES':
            num_deaths += 1
    return num_deaths

def count_by_row(row):
    count = 0
    if (not pd.isnull(row['Death1'])) and (row['Death1'] == 'YES'):
        count += 1
    if (not pd.isnull(row['Death2'])) and (row['Death2'] == 'YES'):
        count += 1
    if (not pd.isnull(row['Death3'])) and (row['Death3'] == 'YES'):
        count += 1
    if (not pd.isnull(row['Death4'])) and (row['Death4'] == 'YES'):
        count += 1
    if (not pd.isnull(row['Death5'])) and (row['Death5'] == 'YES'):
        count += 1
    return count    

true_avengers['Deaths'] = true_avengers.apply(count_by_row, axis=1)
```  
## Step 3 Check "Years since joining" is correct  
```python
joined_accuracy_count  = int()
def loop_through_row(row):
    if (2015 - row['Year']) == row['Years since joining']:
        return True
    else:
        return False

series_ret = list(true_avengers.apply(loop_through_row, axis=1))
for ret in series_ret:
    if (ret == True):
        joined_accuracy_count += 1
```
