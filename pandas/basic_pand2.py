import pandas as pd

df = pd.read_csv('python-devops/pandas/pokemon_data.csv')

# Iterating through index and rows
for index, row in df.iterrows():
    # print(index, row)
    # Printing only index with Name value
    print(index, row['Name'])

# Printing the values of Pokemon which has type1 fire
fire = df.loc[df['Type 1'] == 'Fire']
print(fire)
# Useful method to get count mean, std of each column .. etc
print(df.describe())

# Sorting values using Name so it prints value from A to z
print(df.sort_values('Name'))

# Sorting values using Name so it prints value from Z to A descending order
print(df.sort_values('Name', ascending=False))

# Adding new column with our custom requirements
df['Total'] = df['Attack'] + df['Defense'] + \
    df['HP'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

print(df.head(5))

# Droping column
df = df.drop(columns=['Total'])

print(df.head(5))

# Adding new column like before in different way : ==> All rows and 4 to 10 means from HP i.e 4 to Speed i.e 9
df['Total_new'] = df.iloc[:, 4:10].sum(axis=1)
print(df.head(4))

# Saving the file
df.to_csv('python-devops/pandas/modified.csv', index=False)
