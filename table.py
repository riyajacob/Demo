import pandas as pd
import logging

def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s/////%(asctime)s')
    global data
    data = pd.read_excel (r'C:\Users\Riya\OneDrive\Documents\py\sales.xlsx')
    global df
    df=pd.DataFrame(data,columns=['Quantity','Product_ID'])
    #calling both functions
    top()
    highest()

def top():
    global sorted_descending
    sorted_descending=df.sort_values(by=['Quantity'],ascending=False)
    logging.info("*****TOP 5 PRODUCTS******")
    print(sorted_descending.head(5))
    print('\n')
    logging.info("*****BOTTOM 5 PRODUCTS******")
    print(sorted_descending.tail(5))
    print('\n')


def highest():
    n=pd.DataFrame(data)
    #accessing product_ID,area and quantity
    product_area=n[['Product_ID','Quantity','Area']]
    #sorting quantity in descending order
    sorted=product_area.sort_values(by=['Quantity'],ascending=False)
    highest_product=sorted.groupby('Area')
    logging.info("*****HIGHEST PRODUCT IN EACH AREA******")
    print sorted.iloc[[4,2,0]]


if __name__=='__main__':
    main()
