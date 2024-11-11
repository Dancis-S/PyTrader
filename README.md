# PyTrader

This project is focused on building and backtesting an **algorithmic trading bot** capable of implementing multiple trading strategies on historical stock data. The project uses a robust portfolio management and backtesting engine to evaluate each strategy's performance over time.

## Key Accomplishments

### 1. Data Collection and Preprocessing
- Collected historical stock data (both **hourly** and **daily**).
- Processed the data to handle inconsistencies and ensure it's ready for strategy testing and backtesting.

### 2. Backtesting Engine
- Developed a **Portfolio management engine** to track:
  - Trades and holdings
  - Cash balance and portfolio value
  - Transaction costs and slippage
- Provides realistic trade simulations and enables accurate tracking of strategy performance over time.

### 3. Implemented Trading Strategies
- **SMA Crossover Strategy**: A trend-following strategy that uses short- and long-term Simple Moving Averages to generate buy/sell signals.
- **Mean Reversion Strategy**: Uses **Bollinger Bands** to identify overbought and oversold conditions and generate reversal trades.
- **MACD Strategy**: A momentum-based strategy that applies the **Moving Average Convergence Divergence (MACD)** line and Signal line crossover to identify buy/sell signals, combined with **stop-loss** and **take-profit** rules for risk management.

### 4. Performance Metrics and Evaluation
- Calculated key performance metrics to evaluate strategy effectiveness:
  - **Compound Annual Growth Rate (CAGR)**
  - **Sharpe Ratio**
  - **Max Drawdown**
  - **Volatility**
- Metrics are dynamically adjusted for different timeframes (daily, hourly), providing flexibility in analysis.

### 5. Visualization
- Created visualization functions to:
  - Plot **portfolio value over time** for tracking growth and declines.
  - Mark **trade actions** (buy/sell points) on price charts for clear visibility of trade execution.

---

