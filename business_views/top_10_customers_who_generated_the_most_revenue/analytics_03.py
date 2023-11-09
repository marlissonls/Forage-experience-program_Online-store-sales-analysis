import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from os.path import dirname

MAIN_PROJECT_PATH = dirname(dirname(dirname(__file__)))

# Load dataset
df = pd.read_csv(f'{MAIN_PROJECT_PATH}/data_source/curated_data/curated_online_retail_data_set.csv')
df['CustomerID'] = df['CustomerID'].astype(str)

df_customers_revenue = df.groupby('CustomerID')[['Quantity', 'UnitPrice']].apply(lambda x: (x['Quantity'] * x['UnitPrice']).sum()).reset_index()
df_customers_revenue = df_customers_revenue.rename(columns={0: 'Revenue'})
df_customers_revenue = df_customers_revenue.sort_values(by='Revenue', ascending=False).reset_index(drop=True)
df_top_ten_customers_revenue = df_customers_revenue[1:11].copy()
df_top_ten_customers_revenue = df_top_ten_customers_revenue.iloc[::-1]

customer = df_top_ten_customers_revenue['CustomerID']
revenue_customer = df_top_ten_customers_revenue['Revenue']

plt.close('all')
plt.figure(figsize=(8, 5))
plt.barh(customer, revenue_customer, color='#FFD580', height=.6)
plt.title('Top 10 Custormers by Revenue')
plt.xlabel('Revenue (US$)')
plt.ylabel('Custormer')
xlabels = np.arange(0, 315000, step=50000)
new_xlabels = [f'${round(x/1000)}K' for x in xlabels]
plt.xticks(xlabels, new_xlabels, color='#606060')
plt.yticks(color='#606060')
plt.xlim(0, 315000)
plt.grid(axis='x', linestyle='--', alpha=0.6)
for i_customer, revenue_cust in enumerate(revenue_customer):
    plt.text(revenue_cust, i_customer, " $"+str(round(revenue_cust/1000))+'K', color='black', va='center', weight='regular', fontsize=9)

plt.savefig(f'{MAIN_PROJECT_PATH}/business_views/top_10_customers_who_generated_the_most_revenue/top_10_customers_who_generated_the_most_revenue.png')
plt.show()