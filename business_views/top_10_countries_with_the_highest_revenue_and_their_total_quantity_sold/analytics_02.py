import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from os.path import dirname

MAIN_PROJECT_PATH = dirname(dirname(dirname(__file__)))

# Load dataset
df = pd.read_csv(f'{MAIN_PROJECT_PATH}/data_source/curated_data/curated_online_retail_data_set.csv')

# DATAFRAME COUNTRY | QUANTITY | REVENUE
df_countries_revenue = df.groupby('Country')[['Quantity', 'UnitPrice']].apply(lambda x: (x['Quantity'] * x['UnitPrice']).sum()).reset_index()
df_countries_revenue = df_countries_revenue.rename(columns={0: 'Revenue'})
df_countries_quantity = df.groupby('Country')['Quantity'].sum().reset_index()
df_countries_quantity = df_countries_quantity.rename(columns={0: 'Quantity'})

df_countries_revenue_quantity = pd.merge(df_countries_revenue, df_countries_quantity, on="Country")
df_countries_revenue_quantity = df_countries_revenue_quantity.sort_values(by='Revenue', ascending=False).reset_index(drop=True)
df_top_ten_countries_revenue_quantity = df_countries_revenue_quantity[1:11].copy()
df_top_ten_countries_revenue_quantity = df_top_ten_countries_revenue_quantity.iloc[::-1]

country = df_top_ten_countries_revenue_quantity['Country']
revenue = df_top_ten_countries_revenue_quantity['Revenue']
quantity = df_top_ten_countries_revenue_quantity['Quantity']
gray_color = '#606060'


# CHART TOP 10 COUNTRIES BY REVENUE
fig, (revenue_chart, quantity_chart) = plt.subplots(1, 2, figsize=(13, 5))
revenue_chart.barh(country, revenue, color='skyblue', height=0.7)
revenue_chart.grid(axis='x', linestyle='--', alpha=0.6)
revenue_chart.set_title('Top 10 Countries by Revenue')
revenue_chart.set_ylabel('Country')
revenue_chart.set_xlabel('Revenue Generated')
#revenue_chart.ticklabel_format(axis='x', style='sci', scilimits=(3, 3))
xticks = revenue_chart.get_xticks()
new_xticks = [f'{int(x/1000)}K' for x in xticks]
revenue_chart.set_xticks(xticks, new_xticks)
revenue_chart.set_xlim(0, 330000)
for label in revenue_chart.get_xticklabels(): label.set_color(gray_color)
for label in revenue_chart.get_yticklabels(): label.set_color(gray_color)
for i_country, revenue_value in enumerate(revenue):
    revenue_chart.text(revenue_value, i_country, ' $'+str(round(revenue_value/1000))+'K', color='black', va='center', weight='regular', fontsize=10)

# CHART QUANTITY SOLD BY EACH COUNTRY'S REVENUE
quantity_chart.barh(country, quantity, color='#FFD580', height=0.7)
quantity_chart.grid(axis='x', linestyle='--', alpha=0.6)
quantity_chart.set_title("Quantity Sold by each Country's Revenue")
quantity_chart.set_xlabel('Quantity Sold')
#quantity_chart.ticklabel_format(axis='x', style='sci', scilimits=(3, 3))
xticks = quantity_chart.get_xticks()
new_xticks = [f'{int(x/1000)}K' for x in xticks]
quantity_chart.set_xticks(xticks, new_xticks)
quantity_chart.set_xlim(0, 225000)
quantity_chart.set_yticks(quantity_chart.get_yticks(),[])
quantity_chart.tick_params(left=False)
for label in quantity_chart.get_xticklabels(): label.set_color(gray_color)
for i_country, quantity_value in enumerate(quantity):
    quantity_chart.text(quantity_value, i_country, " "+str(round(quantity_value/1000))+'K', color='black', va='center', weight='regular', fontsize=10)

# DISPLAY
plt.tight_layout()

plt.savefig(f'{MAIN_PROJECT_PATH}/business_views/top_10_countries_with_the_highest_revenue_and_their_total_quantity_sold/top_10_countries_with_the_highest_revenue_and_their_total_quantity_sold.png')
plt.show()