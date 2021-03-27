import pandas as pd

df = pd.read_csv('python-devops/pandas/pokemon_data.csv')
# Finding the mean values by coulmn Type 1
type1_value = df.groupby(['Type 1']).mean()
# Sorting by defense highest to lowest
type1_value_sort = df.groupby(['Type 1']).mean(
).sort_values('Defense', ascending=False)
# This get the values of count from all the columns
type1_count = df.groupby(['Type 1']).count()
df['count'] = 1
type1 = df.groupby(['Type 1']).count()['count']

typ1_typ2 = df.groupby(['Type 1', 'Type 2']).count()['count']
print(typ1_typ2)
