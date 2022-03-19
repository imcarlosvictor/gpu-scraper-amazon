import pandas as pd


def clean_gpu_data():
    # Load data
    csv_file = './data/newegg_data.csv'
    data = pd.read_csv(csv_file)
    # Remove "NaN" elements
    data['Original Price'] = data['Original Price'].fillna(' ')
    # Remove unnecessary wording
    data['Shipping'] = data['Shipping'].str.replace('Shipping', '')
    # Remove dollar sign
    data['Current Price'] = data['Current Price'].str.replace('$','').str.replace(',','')

    print(data['Current Price'])
    return data

clean_gpu_data()