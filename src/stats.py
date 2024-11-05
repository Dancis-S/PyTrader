import numpy as np


def calculate_compound_annual_growth_rate(beginning_value, final_value, years):
    """
        Calculates the mean annual growth rate of an investment over a period
        longer than one year. (a.k.a CAGR)
    """
    return ((final_value / beginning_value) ** (1 / years)) - 1


def calculate_sharpe_ratio(daily_returns, periods_per_year, risk_free_rate = 0.02):
    """
        A measure of an investment risk-adjusted performance, calculate by 
        comparing its return to that of a risk-free asset
    """
    excess_returns = daily_returns - (risk_free_rate / periods_per_year)
    sharpe_ratio = np.mean(excess_returns) / np.std(excess_returns) * np.sqrt(periods_per_year)
    return sharpe_ratio


def calculate_max_drawdown(portfolio_values):
    """
        Max drawdown measures the largest peak-to-trough decline in the portfolio
        value over a specified period.
    """
    largest_drawdown = 0
    peak = portfolio_values[0]

    for value in portfolio_values:
        if value > peak:
            peak = value
        drawdown = (peak - value) / peak
        if drawdown > largest_drawdown:
            largest_drawdown = drawdown

    return largest_drawdown


def calculate_volatility(daily_returns, periods_per_year):
    """
        Volatility measures the degree of variation in your portfolio returns over
        time, often represented as the standard deviation of daily returns.
    """
    return np.std(daily_returns) * np.sqrt(periods_per_year)
