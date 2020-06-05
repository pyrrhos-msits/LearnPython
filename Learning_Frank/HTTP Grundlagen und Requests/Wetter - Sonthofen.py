import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.wetter.com/deutschland/sonthofen/DE0009973.html')
soup = BeautifulSoup(r.content, 'html.parser')

table = soup.find('table', class_="weather-overview mb mt" )

def wochentag(a):
    if a == 'Mo':
        return 'Montag'
    elif a == 'Di':
        return 'Dienstag'


tag = table.a['aria-label'] # Liest nur die Überschrift aus
wt = soup.find('span', class_="gamma line-height--normal").get_text()
wochentag = wochentag(wt)
print('1.' , tag, ' ', wochentag)
# <<<<<<<<<<<<<<<<< Auslesen der Tages zeiten >>>>>>>>>>>>>>>>>>>>>
zeit = table['td', class_="delta text--center pb-- portable-pt-- desk-pt tdbl "]






