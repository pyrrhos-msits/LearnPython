from bs4 import BeautifulSoup
import requests

r = requests.get('https://docs.python.org')
soup = BeautifulSoup(r.content, 'html.parser') # Der html.parser legt den Parser fest. würde auch ohne gehen, wirft dann aber eine Fehlermeldung
elements = soup.find_all('a')









