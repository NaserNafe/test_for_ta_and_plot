import finplot as fplt
import yfinance

df = yfinance.download('ETH')
print(df)
# fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']])
# fplt.show()