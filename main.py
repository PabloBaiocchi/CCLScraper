import requests
from time import localtime, sleep
from adr import adrs

def yahooFinance(symbol):
    url=f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?region=US&lang=en-US&includePrePost=false&interval=2m&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance"
    session=requests.session()
    json=session.get(url).json()
    return {
        'price':json['chart']['result'][0]['meta']['regularMarketPrice'],
        'time':localtime(json['chart']['result'][0]['meta']['regularMarketTime']),
        'symbol':json['chart']['result'][0]['meta']['symbol']
    }

def IOL(idTitulo):  
    url=f"https://www.invertironline.com/Titulo/GraficoIntradiario?idTitulo={idTitulo}&idTipo=4&idMercado=1"
    session=requests.session()
    json=session.get(url,headers={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'en-US,en;q=0.5',
        # 'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'i18n.langtag=es-AR; isMobile=0; _gcl_au=1.1.1921128629.1586143442; _ga=GA1.2.1383740554.1586143444; _fbp=fb.1.1586143444048.871101205; _hjid=49171220-f2fb-46e9-b72d-38344741ec71; intencionApertura=0; uid=709325; anonymous=true; __RequestVerificationToken=Ym49uNkNMwrA1dCkvtnjrmfrd5ITXUETrs3r58NmbHDT-0AHCXntpSfK4RvNKCnIu2dXzkgP_sFZ5wGgBYgKbRdw1IA1; isLogged=1; _gid=GA1.2.169305788.1586733546; _dc_gtm_UA-189938-1=1; __sidglobal=jhbqdzo4cjzbgpnz1nxkronq; _gat_UA-189938-1=1',
        'Host':'www.invertironline.com',
        'Referer':'https://www.invertironline.com/titulo/cotizacion/BCBA/BBAR/BBVA/',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:75.0) Gecko/20100101 Firefox/75.0',
        'X-Requested-With':'XMLHttpRequest'
    }).json()
    return json

def shuffle(array):
    newArray=array[1:].copy()
    newArray.append(array[0])
    return newArray  

def run():
    usaDump=open('./usa5.txt','w')
    argDump=open('./arg5.txt','w')
    companies=adrs
    while True:
        companies=shuffle(companies)
        for company in companies:
            print(company)
            usa=None
            try:
                usa=yahooFinance(company['symbol'])
            except:
                continue
            dumpString=f"{usa['symbol']},{usa['price']},{usa['time'][3]},{usa['time'][4]}\n"
            print(dumpString)
            usaDump.write(dumpString)
            arg=None
            try:
                arg=IOL(company['id'])[-1]
            except:
                continue
            dumpString=f"{company['symbol']},{arg['Ultima']},{localtime(arg['FechaHora'])[3]},{localtime(arg['FechaHora'])[4]}\n"
            print(dumpString)
            argDump.write(dumpString)
        sleep(5)
    usaDump.close()
    argDump.close()

def writeRatiosFile():
    ratios=open('./ratios.txt','w')
    for company in adrs:
        ratios.write(f"{company['symbol']},{company['ratio']}\n")
    ratios.close()

run()

