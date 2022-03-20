import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

import clean_data as cd

# CSV File(s)
gpu_csv_path = "./data/newegg_data.csv"

# Load data
gpu_data = pd.read_csv(gpu_csv_path)


class GPUData():
    def __init__(self):
        self.orig_data = pd.read_csv(gpu_csv_path) 

        self.display_data_frame()
        self.display_gpu_brands()
        self.display_gpu_prices()

    def display_data_frame(self):
        df = cd.clean_data(self.orig_data)
        st.dataframe(df)
    
    def display_gpu_brands(self):
        # Data points
        brands = self.orig_data['Brand'].unique()
        brand_count = self.orig_data['Brand'].value_counts()
        # Plot
        fig = go.Figure(data=[go.Bar(
            x=brands,
            y=brand_count,
            text=brand_count,
            textposition='auto',
        )])
        st.plotly_chart(fig)

    # TODO: Create a function to clean the price data (to float)
    def display_gpu_prices(self):
        # Data points
        brands = self.orig_data['Brand']
        cur_prices, orig_price = cd.clean_prices(self.orig_data)
        cur_prices.sort()
        # Plot
        fig = px.scatter(x=brands, y=cur_prices)
        fig.update_yaxes(title='Price')
        fig.update_xaxes(title='Brand')
        st.plotly_chart(fig)


if __name__ == '__main__':
    # Initialize page
    st.set_page_config(page_title='GPU Prices')
    st.header('GPU Prices')

    gpu = GPUData()