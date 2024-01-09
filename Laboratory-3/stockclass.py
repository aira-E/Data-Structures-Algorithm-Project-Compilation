class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.symbol = symbol
        self.name = name
        self.previousClosingPrice = previousClosingPrice
        self.currentPrice = currentPrice

    #Data
    def stocksname(self):
        return self.name
    def stocksymbol(self):
        return self.symbol

    #Get the Data
    def getpreviousprice(self):
        return self.previousClosingPrice
    def getcurrentprice(self):
        return self.currentPrice

    #Set the Data
    def setpreviouseprice(self, previousClosingPrice):
        self.previousClosingPrice = previousClosingPrice
    def setcurrentprice(self, currentPrice):
        self.currentPrice = currentPrice

    #Compute the Data
    def getChangePercent(self):
        return ((self.currentPrice - self.previousClosingPrice ) /self.previousClosingPrice * 100)

#Print the data
stock = Stock("INTC","Intel Corporation", 20.5, 20.35)
print (f"Price Changed Percentage of {stock.name} ({stock.symbol}): \n {stock.getChangePercent()}%")



