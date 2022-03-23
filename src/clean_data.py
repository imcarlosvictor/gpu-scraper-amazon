import pandas as pd


def clean_data(data):
    # Remove items with no current price
    data = data[data['Current Price'].notna()]
    # GPU Series
    data['GPU Series'] = data['GPU Series'].fillna('')
    # Original Price
    data['Original Price'] = data['Original Price'].fillna('')
    # Shipping
    del data['Shipping']
    # Reviews
    data = data[data['Reviews'].str.contains('stars')]


    print(data['Product Name'])
    return data


def clean_prices(data):
    data['Current Price'] = data['Current Price'].str.replace('$','').str.replace(',','')
    data['Original Price'] = data['Current Price'].str.replace('$','').str.replace(',','')
    data['Shipping'] = data['Shipping'].str.replace('Shipping', '')
    data['Shipping'] = data['Current Price'].str.replace('$','').str.replace(',','')

    cur_prices = [float(price) for price in data['Current Price']]
    orig_prices = [float(price) for price in data['Original Price']]
    
    return cur_prices, orig_prices