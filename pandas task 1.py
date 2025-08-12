# Use the movie data stores in the file Data/movies.csv to solve the following subtasks:

# Load the data and set the column title as index
# Change the column names to avoid capital letters, white spaces and brackets
# Replace the missing values in all rows with the median of the respective column
# Find all movies that were released between 2005 and 2010
# Find all movies that have a rating above 8.0
# Find all movies that made below the 25th percentile in revenue
import pandas as pd

movies = pd.read_csv('Data/movies.csv')
movies.set_index("Title", inplace=True)

movies.columns = [col.lower().replace("(", "").replace(")", "").replace(" ", "_") for col in movies.columns]

revenue=movies["revenue_millions"]
movies["revenue_millions"].fillna(revenue.median(), inplace=True)
score=movies["metascore"]
movies["metascore"].fillna(score.median(), inplace=True)

selector1=movies["year"]>=2005
selector2=movies["year"]<=2010
print(movies[selector1 & selector2])

selector3=movies["rating"]>8
print(movies[selector3])

selector4=movies["revenue_millions"]<movies["revenue_millions"].quantile(0.25)
print(movies[selector4])
# print(movies)
# movies.rename(columns={
#     ""
# })