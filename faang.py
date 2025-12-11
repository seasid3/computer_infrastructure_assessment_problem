# This code will download hourly FAANG stock data from yFinance and will plot closing prices over
# time. The code will run
# Author: Orla Woods


# Import modules

# Import os for file handling
import os

# Import pandas
import pandas as pd

# Import matplotlib for plotting
import matplotlib.pyplot as plt

# Dates and times
import datetime as dt

# Import yFinance (Yahoo Finance)    
import yfinance as yf

# Get data for the five companies (multiple tickers at once), using 
# df to persist the data frame
# https://ranaroussi.github.io/yfinance/

def get_data():
    # Define the FAANG stocks
    faang_stocks = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']

    # Get hourly data for the last 5 days
    data = yf.download(tickers=faang_stocks, period='5d', interval='1h')
    
    return data

# Get the data
df = get_data()

# Print the first few rows of the dataframe
print(df.head())



