import pandas as pd
import os

folders = os.listdir('data')
df_all = pd.DataFrame()
for i in range(0, len(folders)):
    if folders[i].split('.')[1] == 'csv':
        file = 'data/' + folders[i]
        df = pd.read_csv(file, encoding='utf-8')
        df_all = pd.concat([df_all, df])

df = pd.DataFrame(df_all)
df.to_csv(
    './data/all_data.csv', sep=',', encoding='utf-8', index=None
)