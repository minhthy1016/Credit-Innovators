%md 
## Download US stocks price history and build a trading strategy performance analysis for backtesting

### Download US historical stock data and create a trading strategy:
This mini lab will show you to perform some stock trading analysis, which is focus on evaluate return and risk for backtesting. 
You can use the US historical data downloaded with yfinance.
This lab require you have some basic knowledge of Technical analysis. In the lab, we will have some trading strategy we need to analyze their return performance. The trading strategy I built for the lab involved: SMA50, SMA200, MACD, and some performance metrics such as Sharpe ratio, Sortino ratio, maximum drawdown, etc. I also have some Trading-Stop-Loss at 5% per trade , Trailing-Stop-loss at 5%, and Take-Profit at 20% per trade. 

In real trading, you will need to combine lots of strategies and tools. This lab is to help you to analyze and justify your choices so you can find out which ones are better combination, for which porfolio. 

The tickers applied in the lab is for research only. This is not a financial advice. 


### Analyze the strategy using pyfolio:

Now, you can use pyfolio to analyze the trading strategy's performance. You can compute various performance metrics such as Sharpe ratio, Sortino ratio, maximum drawdown, etc.

### what is Sharpe Ratio, Sortino ratio, maximun drawdown? 
Sharpe Ratio, Sortino Ratio, and Maximum Drawdown are all important metrics used in trading and investing to evaluate the performance and risk of a trading strategy or investment portfolio. Here's an explanation of each metric and how they are used in trading:

1. **Sharpe Ratio:**
   - The Sharpe Ratio is a measure of the risk-adjusted return of an investment or trading strategy. It quantifies the excess return (return above the risk-free rate) generated per unit of risk (typically represented by standard deviation).
   - Formula: Sharpe Ratio = (R_p - R_f) / σ_p
     - R_p: Average return of the investment or strategy.
     - R_f: Risk-free rate of return (typically a government bond yield).
     - σ_p: Standard deviation of the investment's or strategy's returns.
   - Use in Trading: A higher Sharpe Ratio indicates a better risk-adjusted return. Traders and investors use this metric to compare different strategies or portfolios and select those that offer the best trade-off between risk and return.

2. **Sortino Ratio:**
   - The Sortino Ratio is similar to the Sharpe Ratio but focuses on downside risk. It measures the excess return generated per unit of downside risk (typically represented by the standard deviation of negative returns).
   - Formula: Sortino Ratio = (R_p - R_f) / σ_d
     - R_p: Average return of the investment or strategy.
     - R_f: Risk-free rate of return.
     - σ_d: Standard deviation of negative returns.
   - Use in Trading: The Sortino Ratio is particularly useful for strategies where minimizing losses is a priority. It provides a more accurate picture of risk when there is a skewed distribution of returns.

3. **Maximum Drawdown:**
   - Maximum Drawdown represents the largest peak-to-trough decline in the value of a trading account or investment over a specified time period. It measures the worst loss experienced before a recovery in value.
   - Calculation: Maximum Drawdown = (Peak Value - Trough Value) / Peak Value
   - Use in Trading: Maximum Drawdown is a crucial risk metric. It helps traders and investors understand the potential loss they might face when using a particular strategy. Smaller maximum drawdowns are generally preferred because they indicate lower risk.

In trading, these metrics are used in various ways:

- **Performance Evaluation:** Traders and investors use these metrics to assess and compare the performance of different trading strategies, portfolios, or investment options.

- **Risk Management:** These metrics help traders and investors understand the level of risk associated with a strategy and whether it aligns with their risk tolerance.

- **Strategy Selection:** Traders can use these metrics to select strategies that offer the best risk-adjusted return. A higher Sharpe or Sortino Ratio and a smaller maximum drawdown are generally desirable.

- **Monitoring and Improvement:** Continuous monitoring of these metrics can help traders make informed decisions about whether to adjust or abandon a trading strategy based on its risk and return characteristics.
