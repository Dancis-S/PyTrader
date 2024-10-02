import pandas as pd

ticker = "AAPL"
data_path = f"../data/{ticker}_historical_data.csv"

data = pd.read_csv(data_path)
data = data[['Date', 'Close', 'Volume']]
data.set_index('Date', inplace=True)

print(data.head())
