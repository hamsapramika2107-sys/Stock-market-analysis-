import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Stock symbol (Example: Apple)
stock_symbol = "AAPL"

# Download stock data
stock_data = yf.download(
    stock_symbol,
    start="2024-01-01",
    end="2025-01-01"
)

# Display first few rows
print("\nStock Data:")
print(stock_data.head())

# Calculate 50-Day Moving Average
stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()

# Plot Closing Price and Moving Average
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label='Closing Price', color='blue')
plt.plot(stock_data['MA50'], label='50-Day Moving Average', color='red')

plt.title(f'{stock_symbol} Stock Market Analysis')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)

plt.show()
