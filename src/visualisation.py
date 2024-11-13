import matplotlib.pyplot as plt


def plot_portfolio_value(data, strategy_name):
    """
    Plots the value of the portfolio over time

    """
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data['Portfolio Value'], label="Portfolio Value")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value ($)")
    plt.title(f"Portfolio Value Over time - {strategy_name}")
    plt.grid()
    plt.legend()
    plt.show()


def plot_trade_points(data, strategy_name):
    """
    Plot the stock price and the Buy/Sell points.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Stock Price', color='black')
    
    # Plot buy signals
    buys = data[data['Actions'] == 1]
    plt.plot(buys.index, buys['Close'], '^', markersize=10, color='green', label='Buy Signal')
    
    # Plot sell signals
    sells = data[data['Actions'] == -1]
    plt.plot(sells.index, sells['Close'], 'v', markersize=10, color='red', label='Sell Signal')
    
    plt.xlabel('Date')
    plt.ylabel('Stock Price ($)')
    plt.title(f'Trade Signals - {strategy_name} Strategy')

    plt.grid()
    plt.legend()
    plt.show()
    