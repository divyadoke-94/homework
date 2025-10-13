import pandas as pd

# Creating a Series
data = [10, 20, 30, 40]
series = pd.Series(data, index=['a', 'b', 'c', 'd'])
print("Series:\n", series)

# Creating a DataFrame
data_dict = {
    'name': ['alice', 'bob', 'charlie', 'david'],
    'age': [24, 27, 22, 32],
    'City': ['new york', 'paris', 'london', 'tokyo']
}

df = pd.DataFrame(data_dict)
print("\nDataFrame:\n", df)

# Head
print("\nHead:\n", df.head())

# Info
print("\nInfo:\n")
df.info()

# Describe
print("\nDescribe:\n", df.describe())

print("single column:\n",df['name'])
print("\nMultiple Columns:\n",df[['name','Age']])
print("\nrow by index (iloc):\n",df.iloc[1])
print("\nrow by label (loc):\n",df.loc[2])

print("\npeople older than 25:\n", df[df['age']>25])

df['salary'] = [50000,60000,55000,70000]
print("\nwith salary column:\n",df)

df2 = pd.dataframe({
    'A': [1,2,None,4],
    'B': [5, None, None , 8]
})

print("\noriginal with Nan:\n",df2)
print("\nDrop nan:\n", df2.dropna())
print("\nfill nan with 0:\n", df2.fillna(50))

print("\nsorted by age:\n",df.sort_values(by='age'))

df_extra = pd.DataFrame({
    'name': ['alice','bob'],
    'depatment': ['hr','it']
})

merged = pd.merge(df, df_extra, on='name', how='left')
print("\nmerged dataframe:\n",merged)