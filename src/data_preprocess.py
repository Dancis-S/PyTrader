import pandas as pd


ticker = "AAPL"
data_path = f"../data/{ticker}_historical_hourly_data.csv"
save_path = f"../data/{ticker}_processed_hourly_data.csv"

data = pd.read_csv(data_path)
data['Datetime'] = pd.to_datetime(data['Datetime'])
data = data[['Datetime', 'Close', 'Volume']]
data.set_index('Datetime', inplace=True)
data.to_csv(save_path)

print(data.head())
