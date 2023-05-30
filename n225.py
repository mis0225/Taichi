import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 日経225のデータを取得
symbol = '^N225'  # 日経225のシンボル
start_date = '2022-05-01'
end_date = '2023-05-29'

stock_data = yf.download(symbol, start=start_date, end=end_date)

# 移動平均を計算
stock_data['100MA'] = stock_data['Close'].rolling(window=100, min_periods=0).mean()
stock_data['200MA'] = stock_data['Close'].rolling(window=200, min_periods=0).mean()

# グラフのプロット
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(stock_data['Close'], color='black', lw=1, label='Close')
ax.plot(stock_data['100MA'], label='100MA')
ax.plot(stock_data['200MA'], label='200MA')

ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title('Nikkei 225 Index')
ax.legend()

plt.show()
