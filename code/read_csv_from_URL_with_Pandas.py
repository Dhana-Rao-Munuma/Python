import pandas as pd

df_premier_23_24 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2324/E0.csv')

print(df_premier_23_24)

df_premier_23_24.rename(columns = {'FTHG':'Home_Goals', 'FTAG': 'Away_Goals'}, inplace=True)

print(df_premier_23_24)
