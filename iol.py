import requests
from time import localtime, sleep
from datetime import date

today = date.today()

iolSession = requests.session()
iolSession.headers = {
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
    }


def IOL(idTitulo):  
    url=f"https://www.invertironline.com/Titulo/GraficoIntradiario?idTitulo={idTitulo}&idTipo=4&idMercado=1"
    json=iolSession.get(url, timeout=(3,5)).json()
    return json

def parseIOL(symbol, response):
    return f"{symbol},{response['Ultima']},{localtime(response['FechaHora'])[3]},{localtime(response['FechaHora'])[4]},{today}\n"