import pandas as pd

df = pd.read_csv('data_with_summary.csv')

print(df['summary'][0])