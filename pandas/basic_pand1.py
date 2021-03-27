import pandas as pd

df = pd.read_csv('python-devops/pandas/pokemon_data.csv')

# # To print top 3 rows
print(df.head(3))

# # To print last 3 rows
print(df.tail(3))

# Read headers
print(df.columns)

# read each column
print(df['Name'])

# Reading and printing first five columns
print(df['Name'][0:5])

# Reading multiple columns
print(df[['Name', 'Type 1', 'HP']])

# Read Each row
print(df.iloc[3])

# Reading row 1 to 5
print(df.iloc[0:5])

# Read a specific location (row,column)
print(df.iloc[2, 1])  # Prints Venusaur
