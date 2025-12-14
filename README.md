# computer_infrastructure_assessment_problem

## Background
This repository presents my assessment for the Computer Infrastructure module (Sep-Dec 2025). Using yfincance sourced market data, I will show my learnings from this module. 
The assessment is broken down into four problems. Notes and references are included, as per my workings, for each problem below.
The repository is [here]()


## Problem 1: Data from yfinance
The function get_data() downloads hourly data for the previous five days for the five FAANG (Facebook [META], Apple [AAPL], Amazon [AMZN]), Netflix [NFLX], Google [GOOG]) stocks from the [yfinance](https://github.com/ranaroussi/yfinance) Python package. The downloaded stock data is saved as a date and time stamped csv file in the "data" folder in the repository. 



I was having a lot of trouble with getting the plot to save to the plots folder. rewatched the lecture. couldnt figure it out. had a very very (hours long) chat with chatgpt and
it turned out i was actually running good code but didnt call it at teh end. defined plot_data() but didnt call the function. chat gpt conversation: 
https://chatgpt.com/share/693c7f21-60e4-800d-b154-feaa2fe184ef


## Problem 2: Plotting Data
The function plot_data() opens the latest data file in the "data" folder of the repository and, on one plot, plots the Close prices for each of the five stocks. The function saves the plot into a "plots" folder in the root of the repository using a filename date and time stamped SHOULD THIS BE DATE AND TIME STAMPED FOR PLOT TIME OR JUST DATA TIM in the format YYYYMMDD-HHmmss.png. 

## Problem 3: Script
The Python script faang.py (located in the root of the repository) contains the functions above so that the command "./faang.py" in the terminal  runs the script, downloads the data and CREAES A PLOT.

I was running ./faang.py but it wasnt working. used chatgpt to help trouble shoot (https://chatgpt.com/share/693e950f-24cc-800d-8201-a5ff59f6200e). Turns out there can be no comment before the shebang line, this must be the first line in the code. Really good lesson learned!

## Problem 4: Automation

Create a GitHub Actions workflow to run your script every Saturday morning. The script should be called faang.yml in a .github/workflows/ folder in the root of your repository. In your notebook, explain each of the individual lines in your workflow.

### END