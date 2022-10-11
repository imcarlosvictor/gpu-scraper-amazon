import streamlit as st
import pandas as pd
import plotly.express as px
import clean_data as cd


# CSV File(s)
gpu_csv_path = "../gpu/data/gpu_data.csv"

# Load data
gpu_data = pd.read_csv(gpu_csv_path)


class GPUData():
    def __init__(self):
        self.orig_data = pd.read_csv(gpu_csv_path) 
        self.dataframe = self.clean_data()

        self.display_data_frame()
        self.display_gpu_brands()
        self.display_gpu_prices()

    def clean_data(self):
        return cd.clean_data(self.orig_data)

    def display_data_frame(self):
        # df = self.clean_data()
        st.dataframe(self.dataframe)
    
    def display_gpu_brands(self):
        # Data points
        brands = self.dataframe['Brand'].unique()
        brand_count = self.dataframe['Brand'].value_counts()
        # Plot
        fig = px.bar(
            x=brands,
            y=brand_count,
            text=brand_count,
            title="Brand Distribution",
            width=800,
            height=800,
        )
        fig.update_xaxes(title='Brands')
        fig.update_yaxes(title='Total # of Products')
        st.plotly_chart(fig)

    def display_gpu_prices(self):
        # Data points
        series = self.dataframe['GPU Series']
        prices, rating = cd.clean_prices(self.dataframe)
        # prices.sort()
        # for i in range(len(s))
        # Plot
        fig = px.scatter(
            x=rating,
            y=prices,
            color=series,
            custom_data=[self.dataframe['Brand'], self.dataframe.index],
            width=800,
            height=800,
            title='GPU Prices vs Ratings'
            )
        fig.update_xaxes(title='Ratings')
        fig.update_yaxes(title='Price')
        fig.update_traces(
            hovertemplate='Price: $%{y:.2f}'+'<br>Rating: %{x:.2f}' + '<br>Brand: %{customdata[0]}' + '<br>Index: %{customdata[1]}'
        )
        st.plotly_chart(fig)


if __name__ == '__main__':
    # Initialize page
    st.set_page_config(page_title='GPU Prices')
    st.header('GPU Prices')

    gpu = GPUData()
