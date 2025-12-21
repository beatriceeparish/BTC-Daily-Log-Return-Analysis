# BTC-Daily-Log-Return-Analysis
This project analyzes Bitcoin (BTC) daily price data using Python, providing an introduction to crypto quantitative analysis. It demonstrates basic financial computations, statistical analysis, and visualizations using pandas, numpy, and matplotlib.

Technologies
- Python 3.x
- Pandas - data manipulation
- NumPy - numerical operations
- Matplotlib - data visualisation

Overview
The script performs the following:
- Reads and cleans historical BTC daily prices from a CSV file.
- Converts date strings to datetime objects and sorts the data.
- Calculates log returns for daily price changes.
- Computes additional metrics:
  - Squared returns (to analyze volatility clustering)
  - Absolute returns (for autocorrelation analysis)
  - 30-day rolling volatility (annualized)
- Performs basic statistical analysis:
  - Mean, standard deviation, skewness, kurtosis of log returns
- Visualizes:
  - 1. Scatter plot of log return vs lag-1 log return
  - 2. Squared returns over time to show volatility clustering
  - 3. 30-day annualized rolling volatility
- Calculates and prints autocorrelations of squared and absolute returns for multiple lags.

- Features for future improvements
  - Comapre BTC volatility with other cryptocurrencies
  - Add moving averages/more advanced technical indicators
