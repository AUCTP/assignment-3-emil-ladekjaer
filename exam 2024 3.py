#main program
import pandas as pd
url="https://raw.githubusercontent.com/NikoStein/pds_data/main/sales.csv"
sales_data=pd.read_csv(url)

#Total sales per Store for the Year 2014
sales_2014=sales_data[sales_data["Date"].str.startswith("2014")].set_index("Store")
total_sales_2014=sales_2014.groupby("Store")["Sales"].sum()
print(total_sales_2014)

#Store with most consistent sales
sales_std_dev=sales_data.groupby("Store")["Sales"].std()
print(sales_std_dev)
most_consistent_store=sales_std_dev.idxmin()
print(f"Store with most consistent sales: {most_consistent_store}, and it has a standard deviation of: {sales_std_dev.min()}")

#Monthly sales trend for each store
sales_data["Month"] = sales_data["Date"].str[:7]
monthly_sales_trend = sales_data.groupby(["Store", "Month"])["Sales"].sum()
print(monthly_sales_trend)

#Sales distribution by day of the week
#not in curiculum

# Sales trend for the top 5 stores
top_5_stores=sales_data.groupby("Store")["Sales"].sum().sort_values(ascending=False).head(5)
print(top_5_stores)