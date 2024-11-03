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


def plot_trade_points(data, stratergy_name):
    """
    
    """
    pass