import pandas as pd

data = pd.read_excel (r'C:\Users\Riya\OneDrive\Documents\py\sales.xlsx')
df=pd.DataFrame(data,columns=['Quantity','Product_ID'])
#finding top 5 products
s=df.sort_values(by=['Quantity'],ascending=False)
print"*****Top 5 Products******"
print(s.head(5))
print('\n')

#finding bottom 5 products
print"*****Bottom 5 Products******"
print(s.tail(5))


print('\n')
#finding highest product in each area
print"*****Grouped by area******"

n=pd.DataFrame(data)
pa=n[['Product_ID','Area','Quantity']]
s1=pa.sort_values(by=['Quantity'],ascending=False)



hp=s1.groupby('Area')
for name, group in hp:
    print name
    print group
print('\n')
print"****Highest Product in Kerala*****"
print(s1.iloc[[0]])
print('\n')
print"****Highest Product in Delhi*****"
print(s1.iloc[[2]])
print('\n')
print"****Highest Product in Chennai*****"
print(s1.iloc[[4]])
