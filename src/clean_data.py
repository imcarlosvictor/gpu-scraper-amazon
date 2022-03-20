import pandas as pd


def clean_data(data):
    # Remove "NaN" elements
    data['Original Price'] = data['Original Price'].fillna(' ')
    # Remove unnecessary wording
    data['Product Name'].str.split(' ', 1)[1]
    data['Shipping'] = data['Shipping'].str.replace('Shipping', '')

    print(data['Product Name'])
    return data


def clean_prices(data):
    data['Current Price'] = data['Current Price'].str.replace('$','').str.replace(',','')
    data['Original Price'] = data['Current Price'].str.replace('$','').str.replace(',','')
    data['Shipping'] = data['Shipping'].str.replace('Shipping', '')
    data['Shipping'] = data['Current Price'].str.replace('$','').str.replace(',','')

    return data