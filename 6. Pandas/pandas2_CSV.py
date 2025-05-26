import pandas as pd

df = pd.read_csv('people.csv')

# print(df)
# print(df.head()) #Top 5 rows
# print(df.tail()) #Last 5 rows
# print(df.info()) # RangeIndex starting from 0, Data columns(Total), Structure: columns, datatypes, non-null counts, memory usage
# print(df.describe()) # Stats for numeric columns
# print(df['City'])
# print(df[df['Age']>30])
# print(df[df['City'] == 'London'])


# print(df.sort_values('Age'))
# print(df.sort_values('Age', ascending=False))
# print(df.sort_values('Age', ascending=True))
df['AgeInMonths'] = df['Age'] * 12 #Adding a new column
# df.rename(columns = {'City' : 'Location'},inplace = True)
#inplace=True — Means the change happens directly in df.
#Without this, you'd have to assign the result to a new DataFrame (df = df.rename(...)).
# df.drop(columns = ['AgeInMonths'], inplace = True) #Drop the column. Works only if line 18 is uncommented
df.to_csv('people_updated.csv', index = False)