import requests
from time import localtime, sleep
import datetime
from stocks import tickers 
from main import market_close

#Scrapes live market data from yahoo finance website

today = datetime.date.today()

yahooSession = requests.session()

def yahooFinance(symbol):
    url=f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?region=US&lang=en-US&includePrePost=false&interval=2m&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance"
    json=yahooSession.get(url, timeout=(3,5)).json()
    return {
        'price':json['chart']['result'][0]['meta']['regularMarketPrice'],
        'time':localtime(json['chart']['result'][0]['meta']['regularMarketTime']),
        'symbol':json['chart']['result'][0]['meta']['symbol']
    }


def parseYahoo(response):
    return f"{response['symbol']},{response['price']},{response['time'][3]},{response['time'][4]},{today}\n"


#Open file
usa_dump=open('./usa.txt','a')

#Scrape
while datetime.datetime.now() < market_close:
    for ticker in tickers:
        usa=None
        try:
            usa_response=yahooFinance(ticker['symbol'])
        except:
            pass
        parsed=parseYahoo(usa_response)
        print(parsed)
        usa_dump.write(parsed)
        sleep(2) 

#Close files
usa_dump.close()