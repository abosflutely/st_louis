import pandas as pd

df = pd.read_csv('/Users/averychen/Downloads/Police_Incidents.csv')
data = df.dropna(subset = 'Incident Address')

# data = df.dropna(subset='Beat')
data.to_csv('dallas')

