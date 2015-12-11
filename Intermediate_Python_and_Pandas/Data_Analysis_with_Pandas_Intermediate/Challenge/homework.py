import pandas as pd

#all_age columns
#Major_code Major Major_category Total Employed Employed_full_time_year_round Unemployed Unemployment_rate Median P25th P75th
all_ages = pd.read_csv("all-ages.csv")
all_ages.head(5)

#recent_grads columns
#Rank Major_code Major Major_category Total Sample_size Mem Women ShareWomen Employed Part_time Full_time_year_round Unemployed Unemployment_rate Median P25th P75th College_jobs Non_college_jobs Low_wage_jobs
recent_grads = pd.read_csv("recent-grads.csv")

# All values for Major_category
#print(all_ages['Major_category'].value_counts().index)

all_ages_aggregation = all_ages.pivot_table(index="Major_category", values=["Total"], aggfunc=np.sum)
recent_grads_aggregation = recent_grads.pivot_table(index="Major_category", values=["Total"], aggfunc=np.sum)

print(all_ages_aggregation.index) #we will get all column value for "Major_category", this is called row name
print(type(all_ages_aggregation))

#transfer index to a list
all_ages_aggregation_rownames = list(all_ages_aggregation.index)
recent_grads_aggregation_rownames = list(recent_grads_aggregation.index)
all_ages_major_categories = dict()
recent_grads_major_categories = dict()
for idx in range(len(all_ages_aggregation.index)):
    all_ages_major_categories[all_ages_aggregation_rownames[idx]] = all_ages_aggregation.iloc[idx, 0]

for idx in range(len(recent_grads_aggregation.index)):
    recent_grads_major_categories[recent_grads_aggregation_rownames[idx]] = recent_grads_aggregation.iloc[idx, 0]

#find out the percent of recent grads working in Lower_jobs
low_wage_percent = 0.0
total_sum = recent_grads["Total"].sum(axis=0) #sum all values of this column
low_wage_sum = recent_grads["Low_wage_jobs"].sum(axis=0) #sum all values of this column
low_wage_percent = low_wage_sum / total_sum

# All majors, common to both DataFrames
majors = recent_grads['Major'].value_counts().index
#print(majors)

recent_grads_lower_emp_count = 0
all_ages_lower_emp_count = 0

# increment recent_grads_lower_emp_count if Unemployment_rate is lower for recent_grads
# increment all_ages_lower_emp_count if Unemployment_rate is lower for all_ages
# do nothing if Unemployment_rate is the same for both
sort_recent_grads = recent_grads.sort(["Major"], ascending=[False])
sort_all_ages = all_ages.sort(["Major"], ascending=[False])
print("********************************")
print(sort_recent_grads.iloc[0].loc["Unemployment_rate"])
print(sort_all_ages.iloc[0].loc["Unemployment_rate"])
print("********************************")
for idx in range(len(sort_recent_grads.index)):
    recent_grads_unemployment_rate = sort_recent_grads.iloc[idx].loc["Unemployment_rate"]
    all_ages_unemployment_rate = sort_all_ages.iloc[idx].loc["Unemployment_rate"]
    if (recent_grads_unemployment_rate < all_ages_unemployment_rate):
        recent_grads_lower_emp_count = recent_grads_lower_emp_count + 1
    else:
        if (all_ages_unemployment_rate < recent_grads_unemployment_rate):
            all_ages_lower_emp_count = all_ages_lower_emp_count + 1

