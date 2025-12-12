# This code will download hourly FAANG stock data from yFinance and will plot closing prices over
# time. The code will run
# Author: Orla Woods

# Import os for file handling
import os

# Import pandas
import pandas as pd

# Dates and times
import datetime as dt

# Import yFinance   
import yfinance as yf

# Define function to get data
def get_data():
    # Define the FAANG stocks
    faang_stocks = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']
    # Get hourly data for the last 5 days
    data = yf.download(tickers=faang_stocks, period='5d', interval='1h')
    return data

# Get the data
df = get_data()

# Current data and time
now = dt.datetime.now()

# Define filename
filename = "data/" + dt.datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"

# Save to csv
df.to_csv(filename)
