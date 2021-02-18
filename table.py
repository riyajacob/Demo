#finding top 5, bottom 5 and highest products in each area

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
print"*****Grouped by area******"

n=pd.DataFrame(data)
#accessing product_ID,area and quantity
product_area=n[['Product_ID','Area','Quantity']]
#sorting quantity in descending order
sorted=product_area.sort_values(by=['Quantity'],ascending=False)



highest_product=sorted.groupby('Area')
for name, group in highest_product:
    print name
    print group
print('\n')
loca='Chennai','Kerala','Delhi'
print"****Highest Product in {0}*****".format('Chennai')
print sorted.iloc[[0]]
print('\n')
print"****Highest Product in Delhi*****"
print sorted.iloc[[2]]
print('\n')
print"****Highest Product in Chennai*****"
print sorted.iloc[[4]]
