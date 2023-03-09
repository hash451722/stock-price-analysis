import pandas as pd
import numpy as np

# データフレームの作成
df = pd.DataFrame({'A': [1, 2, 3, 4, -2, -1, 5, 6]})

# 符号が変化するところがマイナス値、ほかはゼロ
df['B'] = df['A'].shift(1).mul(df['A'])

df["bool"] = df["B"].apply(lambda x: x <= 0)

df["kai"] = df["bool"].where(df["A"]>0, False).shift(1)
df["uri"] = df["bool"].where(df["A"]<0, False).shift(1)

# .clip(upper=0)

# df["BB"] = df["B"].where(df['B'] < 0, np.nan)
# df["BBB"] = df["BB"].where(df['BB'] == np.nan, other=-1)

# df["C"] = df["A"].mul(df['B'])

# df["kai"] = df["C"].where(df['C'] < 0, other=0, )
# .where(df['A'] > 0, other=0)

print(df)
# print(df.dtypes)

# df2 = pd.DataFrame({'col1': [-1, 2, -3, 4, -5]})
# result = df2['col1'].apply(lambda x: x <= 0)
# print(result)

n = 0
m = 0
for index, data in df[0::].iterrows():

    if data["kai"] == True:
        print("kai")
        n += 100

        m -= data["A"]*100

    if data["uri"] == True and n > 0:
        m += data["A"]*n
        n = 0


    print(data["A"])


    df.loc[index, 'Money'] = m

    # n = data["A"]

print("----")
print(m)

print(df)