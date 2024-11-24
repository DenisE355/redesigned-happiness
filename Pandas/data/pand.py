import numpy as np
import pandas as pd
melb_data = pd.read_csv('C:/Users/denev/IDE/Pandas/data/melb_data.csv', sep=',')
melb_data.info()
melb_data['Car'] = melb_data['Car'].astype('int64')
melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')
mask = melb_data['Price'] > 2000000
print(mask)