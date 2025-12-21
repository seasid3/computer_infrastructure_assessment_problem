#!/usr/bin/env python3

# This code will download hourly FAANG stock data from yFinance and will plot closing prices over time. 
# Author: Orla Woods.

# Import os for file handling.
import os

# Import pandas.
import pandas as pd

# Import matplotlib for plotting.
import matplotlib.pyplot as plt

# Dates and times.
import datetime as dt

# Import yFinance.
import yfinance as yf

# Define function to get data.
def get_data():
    # Define the FAANG stocks.
    faang_stocks = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']
    # Get hourly data for the last 5 days.
    data = yf.download(tickers=faang_stocks, period='5d', interval='1h')
    return data

# Get the data.
df = get_data()

# Current data and time.
now = dt.datetime.now()

# Define filename.
filename = "data/" + dt.datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"

# Save to csv.
df.to_csv(filename)

# Define the plot_data() function.
def plot_data():
    # Locate the latest datafile.
    data_files = sorted(os.listdir('data/'))
    # Get the latest file.
    latest_file = "data/" + data_files[-1]
   
    # Load datafile (csv).
    df = pd.read_csv(latest_file, header=[0,1], index_col=0, parse_dates=True)
    
    # Convert index to datetime.
    df.index = pd.to_datetime(df.index)
    
    # Define the columns to plot.
    close_df = df['Close']

    # Create a plot.
    fig, ax = plt.subplots(figsize=(10, 6))
    close_df.plot(ax=ax)
    plt.xlabel('Date')
    plt.ylabel('Price (USD)') 
    ax.legend(title='Closing Stocks', loc='upper right')   
    
    # Set the plot title to current date.
    ax.set_title(dt.datetime.now().strftime("%Y-%m-%d"))
    
    # Current date and time.
    now = dt.datetime.now()
    
    filename = "plots/" + now.strftime("%Y%m%d-%H%M%S.png")

    # Save figure.
    fig.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close(fig)
    
    print(f"Saved plot to {filename}")

# Call the function to generate and save the plot.    
plot_data()


