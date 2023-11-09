import pandas as pd
from os.path import dirname

MAIN_PROJECT_PATH = dirname(dirname(__file__))

# Load dataset
df = pd.read_excel(f'{MAIN_PROJECT_PATH}/data_source/raw_data/raw_online_retail_data_set.xlsx')

# Filtering valid quantity and valid unit price
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Setting null CustomerID's as '-1'.
df['InvoiceNo'] = df['InvoiceNo'].astype(str)
df['StockCode'] = df['StockCode'].astype(str)
df['CustomerID'] = df['CustomerID'].fillna(-1)
df['CustomerID'] = (df['CustomerID'].astype(int)).astype(str)

# Deleting duplicated data
df = df.drop_duplicates()

# Saving df to csv
df.to_csv(f'{MAIN_PROJECT_PATH}/data_source/curated_data/curated_online_retail_data_set.csv', index = False)

print(f'Dataframe saved to "curated_online_retail_data_set.csv"')