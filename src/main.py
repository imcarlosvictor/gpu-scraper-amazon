import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

import clean_data as cd

# CSV File(s)
gpu_csv_path = "./gpu/data/gpugpu.csv"

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

    def display_gpu_prices(self):
        df = cd.clean_data(self.orig_data)
        # Data points
        series = df['GPU Series']
        cur_prices = cd.clean_prices(df)
        cur_prices.sort()
        # Plot
        fig = px.scatter(x=series, y=cur_prices, color=series)
        fig.update_xaxes(title='GPU Series')
        fig.update_yaxes(title='Current Price')
        st.plotly_chart(fig)


if __name__ == '__main__':
    # Initialize page
    st.set_page_config(page_title='GPU Prices')
    st.header('GPU Prices')

    gpu = GPUData()