import yfinance as yf
import datetime as dt

def process(symbol):
    stock = yf.Ticker(symbol)
    if stock.info['logo_url'] == '':
        print("Output:")
        print("Please enter a valid symbol")
        return
    shortN = stock.info['shortName']
    regularMP = stock.info['regularMarketPrice']
    marketPC = stock.info['regularMarketPrice'] - stock.info['previousClose']
    marketPCP = marketPC / stock.info['previousClose'] * 100
    print("Output:")
    current = dt.datetime.now()
    print(current.strftime("%a %b %d %H:%M:%S PDT %Y"))
    print(f"{regularMP} {marketPC:.02f} ({marketPCP:.02f}%)")

while True:
    print("Input:")
    print("Please enter a symbol:")
    symbol = input()
    process(symbol)

