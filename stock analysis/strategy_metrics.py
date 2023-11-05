import yfinance as yf
import pandas as pd

# Define the function to calculate strategy metrics for a given ticker
def calculate_strategy_metrics(ticker, start_date, end_date):
    # Get the data for the specified ticker
    data = yf.download(ticker, start_date, end_date)

    # Calculate 50-day and 200-day simple moving averages
    data['SMA50'] = data['Adj Close'].rolling(window=50).mean()
    data['SMA200'] = data['Adj Close'].rolling(window=200).mean()

    # Calculate RSI
    def calculate_rsi(data, window=14):
        price_diff = data['Adj Close'].diff()
        gain = price_diff.where(price_diff > 0, 0)
        loss = -price_diff.where(price_diff < 0, 0)

        avg_gain = gain.rolling(window=window, min_periods=1).mean()
        avg_loss = loss.rolling(window=window, min_periods=1).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    data['RSI'] = calculate_rsi(data, window=14)

    # Calculate MACD
    def calculate_macd(data, fastperiod=12, slowperiod=26, signalperiod=9):
        exp12 = data['Adj Close'].ewm(span=fastperiod, adjust=False).mean()
        exp26 = data['Adj Close'].ewm(span=slowperiod, adjust=False).mean()
        macd = exp12 - exp26
        signal = macd.ewm(span=signalperiod, adjust=False).mean()
        return macd, signal

    data['MACD'], data['MACD_Signal'] = calculate_macd(data, fastperiod=12, slowperiod=26, signalperiod=9)

    # Initialize trading parameters
    data['Position'] = 0  # No position
    entry_price = 0
    stop_loss_price = 0
    take_profit_price = 0
    trailing_stop_loss = 0

    # Create trading signals
    for i in range(1, len(data)):
        if data['SMA50'][i] > data['SMA200'][i] and data['RSI'][i] > 30 and data['MACD'][i] > data['MACD_Signal'][i]:
            # Buy signal
            if data['Position'][i - 1] == 0:  # No position
                entry_price = data['Adj Close'][i]
                stop_loss_price = entry_price - (entry_price * 0.05)  # 5% stop-loss
                take_profit_price = entry_price + (entry_price * 0.2)  # 20% take-profit
                trailing_stop_loss = entry_price * 0.95  # 5% trailing stop-loss
                data.at[data.index[i], 'Position'] = 1  # Long position
            elif data['Position'][i - 1] == 1:
                # Check for exit conditions
                if data['Adj Close'][i] <= stop_loss_price:
                    data.at[data.index[i], 'Position'] = 0  # Stop-loss triggered
                elif data['Adj Close'][i] >= take_profit_price:
                    data.at[data.index[i], 'Position'] = 0  # Take-profit triggered
                elif data['Adj Close'][i] >= trailing_stop_loss:
                    stop_loss_price = data['Adj Close'][i] - (data['Adj Close'][i] * 0.05)  # Adjust trailing stop-loss

    # Calculate daily returns
    data['Returns'] = data['Adj Close'].pct_change()
    data['StrategyReturns'] = data['Returns'] * data['Position'].shift(1)

    # Drop NaN values from the DataFrame
    data.dropna(inplace=True)

    # Calculate strategy metrics based on your specified risk parameters
    entry_condition = (data['SMA50'] > data['SMA200']) & (data['RSI'] > 30) & (data['MACD'] > data['MACD_Signal'])
    asset_returns = data['Returns'].fillna(0)
    strategy_returns = entry_condition * asset_returns

    # Calculate metrics manually
    num_trades = strategy_returns.sum()
    num_winners = (strategy_returns > 0).sum()
    num_losers = (strategy_returns < 0).sum()
    win_rate = num_winners / num_trades if num_trades > 0 else 0
    annual_return = num_trades * 252

    avg_daily_return = asset_returns.mean()
    td_dev_daily_return = asset_returns.std()
    # # Annual return = average daily return * 252 (assuming 252 trading days in a year)
    annual_return_2 = avg_daily_return * 252

    # Calculate the Sortino ratio
    downside_returns = asset_returns[asset_returns < 0]
    std_dev_downside = downside_returns.std()
    sortino_ratio = (annual_return - 0.03) / std_dev_downside  # Assuming a risk-free rate of 3%
    sharpe_ratio = (avg_daily_return / std_dev_daily_return) * np.sqrt(252)  # Assuming 252 trading days in a year

    #Calculate other metrics : 
    # Calculate cumulative returns
    cumulative_returns = (asset_returns + 1).cumprod() - 1
    
    # Calculate annual volatility
    annual_volatility = asset_returns.std() * np.sqrt(252)
    
    # Calculate max drawdown
    cumulative_return_max = cumulative_returns.cummax()
    drawdown = (cumulative_returns - cumulative_return_max) / (cumulative_return_max + 1)
    max_drawdown = drawdown.min()
    
    # Calculate Calmar ratio
    calmar_ratio = cumulative_returns[-1] / abs(max_drawdown)
    
    # Calculate stability
    stability = cumulative_returns.mean() / cumulative_returns.std()
    
    # Calculate Omega ratio
    omega_ratio = cumulative_returns.mean() / abs(cumulative_returns[cumulative_returns < 0].mean())
    
    # Calculate skewness
    skewness = skew(asset_returns)
    
    # Calculate kurtosis
    kurt = kurtosis(asset_returns)
    
    # Calculate tail ratio
    tail_ratio = asset_returns[asset_returns < 0].mean() / abs(asset_returns[asset_returns > 0].mean())
    
    # Calculate daily Value at Risk (VaR) at a 5% confidence level
    daily_var = asset_returns.quantile(0.05)




    # # Calculate strategy metrics based on your specified risk parameters
    # trades = entry_condition
    # num_trades = len(trades)
    # num_winners = len(trades[trades > 0])
    # num_losers = len(trades[trades < 0])
    # win_rate = num_winners / num_trades if num_trades > 0 else 0

    # Append strategy metrics to the list
    strategy_metrics = {
        "Ticker": ticker,
        "Average Daily Return": avg_daily_return,
        "Standard Deviation of Daily Return": std_dev_daily_return,
        "Annual Return 01": annual_return,
        "Annual Return 02": annual_return_2,
        "Win Rate": win_rate,
        "Num Trades": num_trades,
        "Num Winners": num_winners,
        "Num Losers": num_losers,            
        "Sortino Ratio": sortino_ratio,
        "Sharpe_ratio": sharpe_ratio, 
        "Cumulative Returns": cumulative_returns[-1],
        "Annual Volatility": annual_volatility,
        "Max Drawdown": max_drawdown,
        "Calmar Ratio": calmar_ratio,
        "Stability": stability,
        "Omega Ratio": omega_ratio,
        "Skew": skewness,
        "Kurtosis": kurt,
        "Tail Ratio": tail_ratio,
        "Daily Value at Risk (5%)": daily_var,
    }

    return strategy_metrics

# Define the list of tickers
tickers_list = ['AAPL', 'AMZN', 'GOOGL', 'META', 'NVDA', 'MSFT', 'IBM', 'INTC', 'CRM', 'CSCO', 'DELL',  'QCOM','T','STX', 'VZ', 'GM',
                 'CAT', 'LLY', 'HAL', 'SHOP', 'BMY', 'CME', 'ABBV', 'TMUS', 'BA', 'AIR.PA', 'AMAT', 'BLD','TSLA', 'NFLX', 'NOW', 'YUM', 'WMT', 'PG', 'AMGN', 'DUOL','XOM','SHEL.L', 'ROKU', 'PLTR']

benchmark_tickers = ['^GSPC', 'VOO', 'SPY']
# Combine the list of stocks and benchmark tickers
all_tickers = tickers_list + benchmark_tickers

# Initialize a list to store strategy metrics for each ticker
strategy_metrics_list = []

# Calculate strategy metrics for each ticker
for ticker in all_tickers:
    strategy_metrics = calculate_strategy_metrics(ticker, '2018-01-01', '2023-11-08')
    strategy_metrics_list.append(strategy_metrics)

# Convert the list of strategy metrics to a DataFrame
strategy_metrics_df = pd.DataFrame(strategy_metrics_list)

# save result
strategy_metrics_df.to_csv('strategy_metrics_df.csv')
