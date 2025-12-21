# computer_infrastructure_assessment_problem

## Background
This repository presents my assessment for the Computer Infrastructure module (Sep-Dec 2025).  
Notes and references are included, as per my workings, for each problem below.

## Problem 1: Data from yfinance
The function get_data() downloads hourly data from Yahoo! Finance for the previous five days for the five FAANG (Facebook [META], Apple [AAPL], Amazon [AMZN]), Netflix [NFLX], Google [GOOG]) stocks from the [yfinance](https://github.com/ranaroussi/yfinance) Python package. The downloaded stock data is saved as a date and time stamped csv file in the "data" directory in the repository. 

Notes about this: I was having a lot of trouble with getting the plot to save to the plots folder. Having re-watched the lecture, I couldn't figure it out. A long chat with [ChatGPT](https://chatgpt.com/share/693c7f21-60e4-800d-b154-feaa2fe184ef) and it turned out the code was good code; however, while I defined plot_data(), I didn't call the function. 

## Problem 2: Plotting Data
The function plot_data() opens the latest data file in the "data" folder of the repository and, on one plot, plots the Close prices for each of the five FAANG stocks. The function saves the plot into a "plots" directory in the root of the repository using a filename date and time stamped in the format YYYYMMDD-HHmmss.png. The time and date stamp reflects the time/date the plot is saved. 

## Problem 3: Script
The Python script faang.py (located in the root of the repository) contains the functions above so that the command "./faang.py" in the terminal runs the script, downloads the FAANG data and creates a plot of the Close prices for all of the five companies.

Note on this: Running ./faang.py wasn't working. Troubleshooting with [ChatGPT](https://chatgpt.com/share/693e950f-24cc-800d-8201-a5ff59f6200e), there can be no comment before the shebang line, as this must be the first line in the code. 

## Problem 4: Automation
The faang.yml GitHub Actions workflow (located in the root of my repository) runs my script above every Saturday morning, at 9.17am. Each lines of my workflow is explained in the faang.yml code.

### END