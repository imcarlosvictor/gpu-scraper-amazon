# %%
import pandas as pd

csv_file = '../data/newegg_data.csv'
data = pd.read_csv(csv_file)
data.head()

data

# Find missing data
data.isnull()
# df.isnull().count()

print('Original Price with null: ', data['Original Price'].isnull().sum())

data['Original Price'] = data['Original Price'].fillna(' ')
data

# Remove unnecessary wording
data['Shipping'] = data['Shipping'].str.replace('Shipping', '')
data
