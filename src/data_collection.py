import yfinance as yf

# Fetch data
ticker = 'AAPL'
data = yf.download(ticker, start="2014-10-10", end="2024-10-10")

data.ffill(inplace=True)  # Forward fill

data.to_csv(f"../data/{ticker}_historical_daily_data.csv")

