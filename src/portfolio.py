# Portfolio class engine for a single stock

class Portfolio:
    def __init__(self, initial_cash, transaction_cost=0.001, slippage=0.001):
        self.cash = initial_cash
        self.holdings = 0
        self.portfolio_value = initial_cash
        self.transaction_cost = transaction_cost
        self.slippage = slippage

    def buy(self, price, quantity):
        effective_price = price * (1 + self.slippage)
        total_cost = effective_price * quantity
        cost_with_fee = total_cost * (1 + self.transaction_cost)

        if self.cash >= cost_with_fee:
            self.cash -= cost_with_fee
            self.holdings += quantity

    def sell(self, price, quantity):
        effective_price = price * (1 - self.slippage)
        total_revenue = effective_price * quantity
        revenue_with_fee = total_revenue * (1 - self.transaction_cost)

        if self.holdings >= quantity:
            self.cash += revenue_with_fee
            self.holdings -= quantity

    def get_value(self, price):
        total = self.cash + (self.holdings * price)
        return total
