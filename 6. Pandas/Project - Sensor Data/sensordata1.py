import pandas as pd

df = pd.read_csv('SENSORDATA.csv')

# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# df['BATTERY_LEVEL'] = df['BATTERY_LEVEL'].str.replace('%',' ').astype(int) 
df["BATTERY_LEVEL"] = df["BATTERY_LEVEL"].str.replace('%', '').astype(float)
df = df.dropna(subset=["BATTERY_LEVEL"])
df["BATTERY_LEVEL"] = df["BATTERY_LEVEL"].astype(int)
