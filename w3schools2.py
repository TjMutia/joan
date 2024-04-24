

df = pd.read_csv('data.csv')

print(df.to_string()) 
import pandas as pd
df=pd.read_csv('data.csv')
print(df.to_string())
import pandas as pd
df=pd.read_csv('data.csv')
new_df=df.dropna()
print(new_df.to_string())
import pandas as pd
df=pd.read_csv('data.csv')
df.dropna(inplace=True)
print(df.to_string())
import pandas as pd
df=pd.read_csv('data.csv')
df.fillna(130,inplace=True)
import pandas as pd
df=pd.read_csv('data.csv')
df["Calories"].fillna(130,inplace=False)
import pandas as pd
df=pd.read_csv('data.csv')
x=df["Calories"].mean()
df["Calories"].fillna(x, inplace =False)
import pandas as pd
df=pd.read_csv('data.csv')
print('kenya')
x=df["Calories"].mean()
df["Calories"].fillna(x,inplace=False)
import pandas as pd
df=pd.read_csv('data.csv')
x=df["Calories"].mean()
df["Calories"].fillna(x, inplace = False)
import pandas as pd
df=pd.read_csv('data.csv')
import pandas as pd
df=pd.read_csv('data.csv')
x=df["Calories"].mean()
y=df["Calories"].fillna(x,inplace=False)
print(y)
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())
import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = False)
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string()) 

import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = False)
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())

#df.dropna(subset=['Date'], inplace =False)
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())
'''
df.dropna(subset=['Date'], inplace =False)
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string()) 
import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

#print(df.to_string())
print(y)'''
'''import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())'''

