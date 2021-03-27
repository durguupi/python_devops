import pandas as pd

df = pd.read_csv('python-devops/pandas/pokemon_data.csv')
# Filtering of data with Type 1 as Grass
fil1 = df.loc[df['Type 1'] == "Grass"]
# Filtering of data with Type 1 as Grass and Type 2 as Poison
fil2 = df.loc[(df['Type 1'] == "Grass") & (df['Type 2'] == 'Poison')]
# Filtering of data with Type 1 as Grass or Type 2 as Poison
fil3 = df.loc[(df['Type 1'] == "Grass") | (df['Type 2'] == 'Poison')]
# Filtering of data with Type 1 as Grass and Type 2 as Poison and HP value > 70
fil4 = df.loc[(df['Type 1'] == "Grass") & (
    df['Type 2'] == 'Poison') & (df['HP'] > 70)]
# We can get new index values of our modified data
new_index_fil4 = fil4.reset_index(drop=True)
print(new_index_fil4)
