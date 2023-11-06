import yfinance as yf
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis

# Define the list of tickers
tickers_list  = ['AAPL', 'AMZN', 'GOOGL', 'META', 'NVDA', 'MSFT', 'IBM', 'INTC', 'CRM', 'CSCO', 'DELL',  'QCOM','T','STX', 'VZ', 'GM',
                 'CAT', 'LLY', 'HAL', 'SHOP', 'BMY', 'CME', 'ABBV', 'TMUS', 'BA', 'AIR.PA', 'AMAT', 'BLD','TSLA', 'NFLX', 'NOW', 'YUM', 'WMT', 'PG', 'AMGN', 'DUOL','XOM','SHEL.L', 'ROKU', 'PLTR']
benchmark_tickers = ['^GSPC', 'VOO', 'SPY']  # S&P 500, VOO, SPY

# Combine the list of stocks and benchmark tickers
all_tickers = tickers_list + benchmark_tickers

# Create an empty DataFrame to store the data
final_df = pd.DataFrame()

# Download historical data for each ticker
for ticker in all_tickers:
    ticker_data = yf.download(ticker, '2018-01-01', '2023-11-08', interval="1d")

    # Extract 'Date,' 'Adj Close,' and 'Open' prices
    # ticker_data = ticker_data[['Adj Close', 'Open']]
    ticker_data.reset_index(inplace=True)
    ticker_data['Ticker'] = ticker  # Add a 'Ticker' column for identification

    # Append data for the current ticker to the final DataFrame
    final_df = final_df.append(ticker_data)

# Rename the columns to match your desired column names
final_df.rename(columns={'Date': 'date', 'Adj Close': 'Adj Close', 'Open': 'Open price', 'Volume': 'Volume'}, inplace=True)

# Reset the index of the final DataFrame
final_df.reset_index(drop=True, inplace=True)

# Save the final DataFrame to a CSV file
final_df.to_csv('tickers_data.csv', index=False)

# Display the final DataFrame
print(final_df)
