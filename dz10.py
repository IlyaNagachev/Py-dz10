import pandas as pd
import random

list = ['robot'] * 10 + ['human'] * 10
random.shuffle(list)
data = pd.DataFrame({'whoAmI': list})
print(list)

unique_values = data['whoAmI'].unique()

for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

data = data.drop('whoAmI', axis=1)

data.head()

print(data.head())
