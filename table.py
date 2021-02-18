#finding top 5, bottom 5 and highest products in each area
#Created by:Treesa Mary K J on:18-02-2021

import pandas as pd

data = pd.read_excel (r'C:\Users\Riya\OneDrive\Documents\py\sales.xlsx')
df=pd.DataFrame(data,columns=['Quantity','Product_ID'])

#finding top 5 products
sorted_descending=df.sort_values(by=['Quantity'],ascending=False)
print"*****Top 5 Products******"
print(sorted_descending.head(5))
print('\n')

#finding bottom 5 products
print"*****Bottom 5 Products******"
print(sorted_descending.tail(5))
print('\n')

#finding highest product in each area
n=pd.DataFrame(data)
#accessing product_ID,area and quantity
product_area=n[['Product_ID','Quantity','Area']]
#sorting quantity in descending order
sorted=product_area.sort_values(by=['Quantity'],ascending=False)
highest_product=sorted.groupby('Area')
print"****Highest Product in Each Area*****"
print sorted.iloc[[4,2,0]]
