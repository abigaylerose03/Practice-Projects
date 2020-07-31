import pandas as pd 

# reads the csv file of pokemon
df = pd.read_csv('letsgo_pokemon.csv')

# get the count of pokemon per type 
print('Number of Pokemon of each Type')
print(df.groupby('Type').agg('count')['Name'])

# caclulate the median of each stat
print('Median Stats for each Type')
print(df.groupby('Name').agg('median')[['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']])
