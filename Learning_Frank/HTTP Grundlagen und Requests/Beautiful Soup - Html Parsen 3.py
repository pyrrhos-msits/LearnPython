from bs4 import BeautifulSoup
import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print((page.status_code))
#print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify()) # Druckt den html Teil der Seite sauber eingerückt aus
# <<<<<<<<<<<<<< Alle Elemente auflisten >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
list = list(soup.children)
#print(list)
#<<<<<<<<<<<< Die typen aller Elemente herausbekommen>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
types = [type(el) for el in list]
print(types)
