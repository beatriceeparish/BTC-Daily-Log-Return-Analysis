"""
BTC Daily Log Return Analysis


Author: Bea Parish
Date: 2025-12-21

This script analyzes Bitcoin daily prices, calculates log returns,
volatility measures, and autocorrelations, and visualizes them.
Useful as an introductory crypto quantitative project.
"""

def main(): 

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import os
    os.chdir(os.path.dirname(__file__))  #change working directory to script's directory

    df = pd.read_csv("btcusd_d.csv")

    df["date"] = pd.to_datetime(df["date"]) #pd.to_datetime converts string to datetime format
    df = df.sort_values("date")  #sort by date in ascending order
    df = df.dropna().reset_index(drop=True)  #drop rows with missing values and reset index

    #calculate log returns
    df["log_return"] = np.log(df["close"] / df["close"].shift(1))
    #.shift(1) shifts the close prices down by 1 row to align previous day's price with today's price
    #df["close"] / df["close"].shift(1) calculates ratio of today's price to yesterday's
    #np.log computes the natural logarithm of the price ratio
    print(df[["date", "close", "log_return"]].head(10)) #print first 10 rows of date, close price, and log return

    #additional calculations for analysis
    df["squared_return"] = df["log_return"] ** 2
    df["abs_return"] = df["log_return"].abs()
    df["rolling_vol_30d"] = df["log_return"].rolling(30).std() * np.sqrt(365)

    print("Mean:", df["log_return"].mean())
    print("Std:", df["log_return"].std())
    print("Skew:", df["log_return"].skew())
    print("Kurtosis:", df["log_return"].kurtosis())

    plt.ion() #turn on interactive mode for plotting

    #scatter plot of returns vs lagged returns
    fig1, ax1 = plt.subplots(figsize=(7,5))
    ax1.scatter(df["log_return"].shift(1), df["log_return"], alpha=0.3, s=5)
    ax1.set_xlabel("Lag-1 Log Return")
    ax1.set_ylabel("Log Return")
    ax1.set_title("Return vs Lag-1 Return")
    plt.show(block=False) #block=False allows the script to continue running after showing the plot

    #autocorrelation of squared returns (volatility clustering)
    df["squared_return"] = df["log_return"] ** 2
    for lag in range(1, 21):
        corr = df["squared_return"].autocorr(lag=lag)
        print(f"Lag {lag}: vol autocorr = {corr:.4f}")

    #plot squared returns to visualize volatility clustering
    fig2, ax2 = plt.subplots(figsize=(7,5))
    ax2.plot(df["date"], df["squared_return"], linewidth=0.8)
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Squared Return")
    ax2.set_title("Volatility Clustering (Squared Returns)")
    plt.show(block=False)

    #calculate and plot rolling volatility (30-day window)
    fig3, ax3 = plt.subplots(figsize=(7,5))
    ax3.plot(df["date"], df["rolling_vol_30d"], linewidth=1)
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Volatility")
    ax3.set_title("30-Day Annualized BTC Volatility")
    plt.show(block=False)

    input("Press Enter to close all plots...")
    plt.close('all')

    print("\nAutocorrelation of squared returns:")
    for lag in range(1, 21):
        print(f"Lag {lag}: {df['squared_return'].autocorr(lag):.4f}")

    print("\nAutocorrelation of absolute returns:")
    for lag in range(1, 21):
        print(f"Lag {lag}: {df['abs_return'].autocorr(lag):.4f}")


if __name__ == "__main__":
    main()