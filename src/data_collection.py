import yfinance as yf

# Fetch data
ticker = 'AAPL'
data = yf.download(ticker, start="2020-01-01", end="2024-01-01")

data.ffill(inplace=True)  # Forward fill

data.to_csv(f"../data/{ticker}_historical_data.csv")
