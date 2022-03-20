import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

import clean_data


class CleanData():
    pass


class GpuData():
    def __init__(self, data):
        self.data = data
    
    def display_data_frame(self):
        """Displays the scraped data in tabular form."""

        st.dataframe(self.data)

    def display_gpu_brands(self):
        """Displays the total count for each brand in a bar chart."""

        # Data points
        brands = self.data['Brand'].unique()
        brand_count = self.data['Brand'].value_counts()
        # Display as bar graph
        fig, ax = plt.subplots()
        ax.bar(brands, brand_count)
        st.pyplot(fig)


    def display_gpu_prices(self):
        """Displays all prices for each GPU in the file."""

        # Data points
        gpu_brands = self.data['Brand']
        gpu_prices = [float(price) for price in self.data['Current Price']]
        # Display as stripplot graph
        fig, ax = plt.subplots(figsize=(12,10), dpi=90)
        sns.stripplot(gpu_brands, gpu_prices, jitter=0.25, size=8, ax=ax, linewidth=.5)
        st.pyplot(fig)


class GPUData():
    def __init__(self, data):
        self.data = data

    def display_data_frame(self):
        st.dataframe(self.data)
    
    def display_gpu_brands(self):
        # Data points
        brands = self.data['Brand'].unique()
        brand_count = self.data['Brand'].value_counts()
        fig = go.Figure(data=[go.Bar(
            x=brands,
            y=brand_count,
            text=brand_count,
            textposition='auto',
        )])
        st.plotly_chart(fig)

    def display_gpu_prices(self):
        # Data points
        brands = self.data['Brand']
        prices = [float(price) for price in self.data['Current Price']]
        prices.sort()
        fig = px.scatter(x=brands, y=prices)
        fig.update_yaxes(title='Price')
        fig.update_xaxes(title='Brand')
        st.plotly_chart(fig)


if __name__ == '__main__':
    # Initialize page
    st.set_page_config(page_title='GPU Prices')
    st.header('GPU Prices')

    # Import data
    data = clean_data.clean_gpu_data()

    gpu = GPUData(data)
    gpu.display_data_frame()
    gpu.display_gpu_brands()
    gpu.display_gpu_prices()