# Under the url in file task2.py you will find a data set on academic salaries. Use it so solve the following subtasks:

# Find how many records this data frame has, what are the column names?
# Calculate standard deviation for all numeric columns.
# What are the mean values of the first 50 records in the dataset?
# Calculate basic statistics for the salary column
# Determine the correlation between the numeric values – is there an age effect on salary?
# Calculate the average salary by gender, rank and gender+rank
# Write a function that checks if a professor is up for tenure by checking if the time passed since obtaining the phd is at least 6 years. Apply the function to each row of the DataFrame.
# Write a more realistic function that checks if a professor is up for tenure by checking if rank is assistant and the time passed since obtaining the phd is at least 6 years. Apply the function to each row of the DataFrame.

import pandas as pd
url = 'https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv'
salaries = pd.read_csv(url)

# Find how many records this data frame has, what are the column names?
print(f"Number of records: {len(salaries)}")
print(salaries.columns.tolist())

# Calculate standard deviation for all numeric columns.
print(salaries.info())
#We see that the numeric columns are phd, service and salary
numeric_columns = ['phd', 'service', 'salary']
std_devs = salaries[numeric_columns].std()
print(std_devs)

# What are the mean values of the first 50 records in the dataset?
mean_values_of_50 = salaries['salary'].head(50).mean()
print(mean_values_of_50)

# Calculate basic statistics for the salary column
salary_stats = salaries['salary'].describe()
print(salary_stats)

# Determine the correlation between the numeric values – is there an age effect on salary?
correlation = salaries[numeric_columns].corr()
print(correlation)

# Calculate the average salary by gender, rank and gender+rank
avg_salaryG=salaries.groupby("sex")["salary"].mean()
print(avg_salaryG)
avg_salaryR=salaries.groupby("rank")["salary"].mean()
print(avg_salaryR)
avg_salaryGR=salaries.groupby(["discipline", "sex", "rank"])["salary"].mean()
print(avg_salaryGR)

#function to check tenure eligibility based on phd years
# def tenure_check(x):
#     if x["phd"]>=6:
#         return "Eligible for tenure"
#     else:
#         return "Not eligible for tenure"

# salaries["tenure_check"]=salaries.apply(tenure_check, axis=1)
# print(salaries)

# realiostic function to check tenure eligibility based on rank and phd years
def realistic_tenure_check(x):
    if x["rank"] == "Assistant" and x["phd"] >= 6:
        return "Eligible for tenure"
    elif x["rank"]== "Assistant" and x["phd"] < 6:
        return "Not eligible for tenure"
    else:
        return "Already tenured"
    
salaries["Tenure check"]=salaries.apply(realistic_tenure_check, axis=1)
print(salaries)