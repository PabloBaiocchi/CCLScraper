from time import localtime, sleep
from adr import adrs
from iol import parseIOL, IOL
from yahoo import yahooFinance, parseYahoo

def shuffle(array):
    newArray=array[1:].copy()
    newArray.append(array[0])
    return newArray  

def run():
    companies=adrs
    while True:
        companies=shuffle(companies)
        for company in companies:
            print(f"--------- {company['symbol']} ---------")
            usa=None
            try:
                usa_response=yahooFinance(company['symbol'])
            except:
                pass
            dumpString=parseYahoo(usa_response)
            print(f"USA: {dumpString}")
            usaDump.write(dumpString)
            arg=None
            try:
                arg_response=IOL(company['id'])[-1]
            except:
                continue
            dumpString=parseIOL(company['symbol'], arg_response)
            print(f"Argentina: {dumpString}")
            argDump.write(dumpString)
            sleep(60/(len(companies)*2)) 

def writeRatiosFile():
    ratios=open('./ratios.txt','w')
    for company in adrs:
        ratios.write(f"{company['symbol']},{company['ratio']}\n")
    ratios.close()

#Open files
usaDump=open('./usa.txt','a')
argDump=open('./arg.txt','a')

#Scrape
run()

#Close files
usaDump.close()
argDump.close()
