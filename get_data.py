import config
import csv

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
#client = Client(config.API_KEY, config.API_SECRET_KEY)
client = Client()

#prices = client.get_all_tickers()

#candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('daily.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

# for candle in candles :
#     print(candle)
#     candlestick_writer.writerow(candle)


candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2023", "11 Aug, 2023")
for candlestick in candlesticks :
    candlestick[0] = candlestick[0] / 1000   # convert time with millisec
    candlestick_writer.writerow(candlestick)

csvfile.close()