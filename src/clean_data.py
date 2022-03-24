import pandas as pd


def clean_data(data):
    # Remove columns 
    del data['Shipping']
    # Drop product with no price
    data = data[data['Current Price'].notna()]
    # Fill NA with empty space
    data['Brand'] = data['Brand'].fillna('')
    data['GPU Series'] = data['GPU Series'].fillna('')
    data['Original Price'] = data['Original Price'].fillna('')
    data['Reviews'] = data['Reviews'].fillna('')
    # Reviews
    data = data[data['Reviews'].str.contains('stars')]

    # Reset index after changes
    data = data.reset_index(drop=True)
    
    return data


def clean_prices(data):
    data['Current Price'] = data['Current Price'].str.replace('$','').str.replace(',','')
    data['Original Price'] = data['Current Price'].str.replace('$','').str.replace(',','')
    # data['Shipping'] = data['Shipping'].str.replace('Shipping', '')
    # data['Shipping'] = data['Current Price'].str.replace('$','').str.replace(',','')

    cur_prices = [float(price) for price in data['Current Price'] if price != '']
    words = data['Reviews'].str.split(' ')
    ratings = [float(words[i][0]) for i in range(len(words))]
    
    return cur_prices, ratings