import pandas as pd
from pandas import DataFrame
import Portfolio


def calculate_sma(df: DataFrame, window):
    return df['Close'].rolling(window=window).mean()


# Read in the pre-processed data
ticker = "AAPL"
data_path = f"../data/{ticker}_processed_hourly_data.csv"
data = pd.read_csv(data_path)

# Parameters
short_window = 10
long_window = 100

# Calculate the short and long-term SMA's
data['SMA_short'] = calculate_sma(data, short_window)
data['SMA_long'] = calculate_sma(data, long_window)

# Filter out the rows that will be null
data = data[data['SMA_long'].notna()]

# Run the SMA strategy
portfolio = Portfolio.Portfolio(initial_cash=100000)
holding = False

stop_loss_percentage = 0.02
take_profit_percentage = 0.05

for index, row in data.iterrows():
    if row['SMA_short'] > row['SMA_long'] and not holding:
        portfolio.buy(row['Close'], 250)
        holding = True
    elif row['SMA_short'] < row['SMA_long'] and holding:
        portfolio.sell(row['Close'], 250)
        holding = False

# Get the final value at the last day of the data
final_value = portfolio.get_value(data.iloc[-1]['Close'])
print(f"Final Portfolio Value = {final_value}")
