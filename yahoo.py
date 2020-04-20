import requests
from time import localtime, sleep
from datetime import date

today = date.today()

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