# computer_infrastructure_assessment_problem
This repository presents my assessment for the Computer Infrastructure module (Sep-Dec 2025)

Using yfincance to source market data, this assessment aims to evaluate my learnings from this module. 

The assessment is broken down into four problems. Notes and references are included, as per my workings, for each problem.

## Problem 1: Data from yfinance

Download all hourly data for the previous five days for the five FAANG (Facebook [META], Apple [AAPL], Amazon [AMZN]), Netflix [NFLX], Google [GOOG]) stocks from the [yfinance](https://github.com/ranaroussi/yfinance) Python package. 

get_data() function used to save stock data into a date and time stampted csv file in the "data" folder in the repository. 




I was having a lot of trouble with getting the plot to save to the plots folder. rewatched the lecture. couldnt figure it out. had a very very (hours long) chat with chatgpt and
it turned out i was actually running good code but didnt call it at teh end. defined plot_data() but didnt call the function. chat gpt conversation: 
https://chatgpt.com/share/693c7f21-60e4-800d-b154-feaa2fe184ef