# Portfolio class engine for a single stock

class Portfolio:
    def __init__(self, initial_cash, transaction_cost=0.001, slippage=0.001):
        self.cash = initial_cash
        self.holdings = 0
        self.transaction_cost = transaction_cost
        self.slippage = slippage
        self.last_buy_price = None
        self.trades = []

    def buy(self, price, quantity):
        effective_price = price * (1 + self.slippage)
        total_cost = effective_price * quantity
        cost_with_fee = total_cost * (1 + self.transaction_cost)

        if self.cash >= cost_with_fee:
            self.cash -= cost_with_fee
            self.holdings += quantity
            record = {
                'action': 'Buy',
                'price': price,
                'quantity': quantity,
                'total_cost': cost_with_fee,
                'remaining_cash': self.cash,
            }
            self.trades.append(record)

    def sell(self, price, quantity):
        effective_price = price * (1 - self.slippage)
        total_revenue = effective_price * quantity
        revenue_with_fee = total_revenue * (1 - self.transaction_cost)

        if self.holdings >= quantity:
            self.cash += revenue_with_fee
            self.holdings -= quantity
            record = {
                'action': 'Sell',
                'price': price,
                'quantity': quantity,
                'revenue': revenue_with_fee,
                'remaining_cash': self.cash,
            }
            self.trades.append(record)

    def get_value(self, price):
        total = self.cash + (self.holdings * price)
        return total

    def trade_summary(self):
        import pandas as pd
        return pd.DataFrame(self.trades)
