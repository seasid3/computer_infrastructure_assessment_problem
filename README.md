# computer_infrastructure_assessment_problem  

This repository implements an automated data acquisition and visualisation workflow for hourly FAANG stock price data using Python and GitHub Actions. Expected outputs are CSV files saved in `data/` and PNG plots saved in `plots/`, both with date- and time-stamped filenames.   

## Purpose  
This work aims to demonstrate competencies in computational data acquisition, visualisation, scripting, and automation. Specifically, the repository implements a Python workflow to download hourly stock price data from Yahoo! Finance, generate and persist visualisations of closing prices, enable execution via a single command-line script, and automate scheduled execution using GitHub Actions.

## Requirements
The code was developed and tested using Python 3.12.1. The following external dependencies are required (see requirements.txt file):   
- matplotlib  
- pandas  
- yfinance  
All other modules used are part of the Python standard library.  

To install dependencies, run:  

```bash
# Install dependencies
pip install -r requirements.txt
```  

## Usage  

### 1. Running the script from the terminal  

```bash
cd computer_infrastructure_assessment_problem
chmod +x faang.py
./faang.py
```

### 2. Running the script in a Jupyter notebook (Python code cell) 

```python
from faang import get_data, plot_data

# Download stock data
df = get_data()

# Generate and save a plot
# NOTE: plot_data() must be defined to accept a DataFrame
plot_data(df)
```   

## Problem 1: Data from yfinance  
The function `get_data()` downloads hourly data from Yahoo! Finance for the previous five days for the five FAANG stocks: Facebook (META), Apple (AAPL), Amazon (AMZN), Netflix (NFLX), and Google (GOOG), using the [yfinance](https://github.com/ranaroussi/yfinance) Python package. The downloaded stock data is saved as a date- and time-stamped CSV file (local Irish time) in the `data` directory at the root of the repository. The function returns the data as a pandas `DataFrame` for use in a Jupyter notebook or script.   
Reviewing documents and sources for information and processes:  
- https://pythonfintech.com/articles/how-to-download-market-data-yfinance-python/  
- https://towardsdatascience.com/a-comprehensive-guide-to-downloading-stock-prices-in-python-2cd93ff821d4/  
- https://www.analyticsvidhya.com/blog/2021/06/download-financial-dataset-using-yahoo-finance-in-python-a-complete-guide/  

## Problem 2: Plotting Data  
The function `plot_data()` opens the latest data file in the `data` folder of the repository and plots hourly closing prices for each of the five FAANG stocks using matplotlib. The function saves the plot in the `plots` directory at the root of the repository, using a date- and time-stamped filename (local Irish time) in the format YYYYMMDD-HHmmss.png. The plot provides a visual summary of the hourly closing prices for the five stocks over the previous five days. Reviewing sources:
- https://dev.to/dm8ry/python-code-that-generates-a-stock-price-chart-for-the-last-n-days-g8a
- https://www.pyquantnews.com/the-pyquant-newsletter/quickly-make-cool-stock-price-data-visualizations

## Problem 3: Script  
The Python script `faang.py` (located at the root of the repository) contains the functions above. Running the script via the terminal command `./faang.py` downloads the FAANG stock data and generates a plot of the closing prices for all five companies. The resulting CSV and PNG files are saved with date- and time-stamped filenames. Referencing other work:   
- https://www.datacamp.com/tutorial/functions-python-tutorial
- https://www.reddit.com/r/learnpython/comments/90gubh/how_do_you_organize_your_functions_within_a_script/

## Problem 4: Automation  
The GitHub Actions workflow defined in `faang.yml` (located at the root of the repository) runs the `faang.py` script every Saturday at 09:17 UTC. At this time, UTC coincides with Irish time, so no adjustment is necessary. Each line of the workflow is explained within `faang.yml`. The workflow can also be triggered manually for testing or debugging purposes. Testing included running the workflow at regular intervals overnight. Useful references included:  
- https://stackoverflow.com/questions/70458458/how-do-i-simply-run-a-python-script-from-github-repo-with-actions
- https://mechanicalgirl.com/post/using-gitHub-actions-run-python-script/?utm_campaign=Django%2BNewsletter&utm_medium=rss&utm_source=Django_Newsletter_261
- https://towardsdatascience.com/4-levels-of-github-actions-a-guide-to-data-workflow-automation/

## Note
This README was refined with the assistance of [ChatGPT](https://chatgpt.com/share/6947e675-8fc0-800d-a101-3936b7f35c41) suggestions.
### END  