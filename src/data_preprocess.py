import pandas as pd

ticker = "AAPL"
data_path = f"../data/{ticker}_historical_data.csv"
save_path = f"../data/{ticker}_processed_data.csv"

data = pd.read_csv(data_path)
data = data[['Date', 'Close', 'Volume']]
data.set_index('Date', inplace=True)
data.to_csv(save_path)

print(data.head())
