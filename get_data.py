import config
import csv

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
#client = Client(config.API_KEY, config.API_SECRET_KEY)
client = Client()

#prices = client.get_all_tickers()

#candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('2020-2023.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

# for candle in candles :
#     print(candle)
#     candlestick_writer.writerow(candle)


candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2023", "3 Aug, 2023")
for candlestick in candlesticks :
    candlestick_writer.writerow(candlestick)

csvfile.close()