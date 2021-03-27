import pandas as pd
import re

df = pd.read_csv('python-devops/pandas/pokemon_data.csv')
# It prints all the Pokemon name which contains the word mega
mega = df.loc[df['Name'].str.contains('Mega')]
# It prints all the Pokemon name which does not contain the word mega
not_mega = df.loc[~df['Name'].str.contains('Mega')]
print(not_mega)

# Using regular expression re.I means Ignore case
re_fire = df.loc[df['Type 1'].str.contains(
    'fire|grass', flags=re.I, regex=True)]
print(re_fire)

name_pi = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
print(name_pi)
