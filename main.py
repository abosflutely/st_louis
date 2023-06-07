import pandas as pd

df = pd.read_csv('/Users/averychen/Documents/st_louis/crimedata2023.csv')

data = df.dropna(subset='address')
data.to_csv('stlouis_2023')

