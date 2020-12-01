import pandas as pd
#read index dataframe
df = pd.read_csv('index.csv')
#third col
case1 = df.iloc[:,2]
#last 2 cols
case2 = df.iloc[:,-2]
# read first 10 rows of last 2 cols
case3 = df.iloc[-10:,-2:]
