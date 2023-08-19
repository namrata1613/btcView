import backtrader as bt

class RSIStrategy(bt.Strategy):

    def __init__(self) :
        
        self.rsi = bt.talib.RSI(self.data.close,period=14)

    
    def next(self) :
        
        if self.rsi < 30 and not self.position:
            self.buy(size=1)
            #print("Oversold")
        
        if self.rsi > 70 and self.position:
            self.close()
            #print("Overbought")


class SMAStrategy(bt.Strategy) :

    def __init__(self) :
        self.short_sma = bt.talib.SMA(self.data.close,timeperiod=20)
        self.long_sma = bt.talib.SMA(self.data.close,timeperiod=50)
        self.flag =0

    def next(self) :
        if self.order : 
            return 
        
        current_position = self.getposition().size

        if current_position>0 : 
            if self.short_sma < self.long_sma :
                self.order = self.sell(size=1)
                print("sell")

        if current_position < 0:
            if self.short_sma > self.long_sma and not self.position.size==0 :
                self.order = self.buy(size=1)
                print("buy")

        print(current_position)
        
        
            
            
        

cerebro = bt.Cerebro()

data = bt.feeds.GenericCSVData(dataname='daily.csv',dtformat=2)

cerebro.adddata(data)

#cerebro.addstrategy(RSIStrategy)
cerebro.addstrategy(SMAStrategy)

cerebro.run()

cerebro.plot()

