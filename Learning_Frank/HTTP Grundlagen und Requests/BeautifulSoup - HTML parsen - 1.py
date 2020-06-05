from bs4 import BeautifulSoup
import requests

r = requests.get('https://docs.python.org')
print('Status code = ',r.status_code)
raw_Data = r.text # kann man auch gleich in den soup constructor schreiben. Siehe Teil 2
soup = BeautifulSoup(raw_Data, 'html.parser') # Der html.parser legt den Parser fest. würde auch ohne gehen, wirft dann aber eine Fehlermeldung
#print(soup.prettify()) # Druckt den html Teil der Seite sauber eingerückt aus
#title = soup.title
#title_Name = soup.title.name # Der name des Tags
#title_content = soup.title.string
#print('\nDer Titel ist : ', title)
#print('\nDer tag name des Titels ist :', title_Name)
#print('\nDer Inhalt des Titels ist :', title_content)
#print('\nDer Inhalt des ersten "p" Tags\n', soup.p) # Druckt den ersten 'p'Tag aus den er finden kann
soupChildren = list(soup.children)
print(soupChildren)


#alle_p_tags = soup.find_all('p') # Findet alle 'p' tags im Dokument
#den_gesamten_Text_ohne_tags = soup.get_text() # zeigt nur den Text an. Allerdings unformatiert

# print('\n<<<<<<<<< Es folgt der reine Text auf der Seite >>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
# for string in soup.stripped_strings:
#     print(string)
