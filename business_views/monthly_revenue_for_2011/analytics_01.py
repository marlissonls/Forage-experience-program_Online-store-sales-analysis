import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from os.path import dirname

MAIN_PROJECT_PATH = dirname(dirname(dirname(__file__)))

# Load dataset
df = pd.read_csv(f'{MAIN_PROJECT_PATH}/data_source/curated_data/curated_online_retail_data_set.csv')

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df_2011 = df[df['InvoiceDate'].dt.year == 2011]

monthly_revenue = df_2011.groupby(df_2011['InvoiceDate'].dt.to_period('M')).apply(lambda x: (x['Quantity'] * x['UnitPrice']).sum())

monthly_revenue.index = monthly_revenue.index.to_timestamp()

month_labels = monthly_revenue.index.strftime('%b') # '%B' for full month names

plt.figure(figsize=(8, 5))
plt.plot(monthly_revenue.index, monthly_revenue.values, linestyle=':', marker='o', )
plt.title('Store Monthly Revenue in 2011')
plt.ylabel('Revenue (US$)')
ylabels = np.arange(500000, 1800000, step=200000)
new_ylabels = [f'${round(y/1000000, 1)}M' for y in ylabels]
plt.yticks(ylabels, new_ylabels, color='#606060')
plt.xticks(monthly_revenue.index, month_labels, rotation=0, color='#606060')
plt.grid(True, linestyle='--', linewidth=.7)
for i, value in enumerate(monthly_revenue.values):
    plt.annotate(f'{round(value/1000000, 2)}', (monthly_revenue.index[i], value), textcoords="offset points", xytext=(0, 17), ha='center')

plt.savefig(f'{MAIN_PROJECT_PATH}/business_views/monthly_revenue_for_2011/monthly_revenue_for_2011.png')
plt.show()