#jupyterでもmyenvでも動かない！もう！
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

symbol = 'AAPL'
interval = '1m'

x_data = []
y_data = []

fig, ax = plt.subplots()
line, = ax.plot([], [], color='black', lw=1)

def get_realtime_data(i):
    data = yf.download(symbol, period='max', interval=interval)
    latest_data = data[-1:]
    
    x_data.append(latest_data.index[0])
    y_data.append(latest_data['Close'].values[0])
    
    ax.relim()
    ax.autoscale_view()
    
    line.set_data(x_data, y_data)
    
    ax.set_title(f'Real-time Stock Price: {symbol}')
    
    return line,

ani = FuncAnimation(fig, get_realtime_data, blit=True)

plt.show()
