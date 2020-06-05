from bs4 import BeautifulSoup
import requests

r = requests.get('https://docs.python.org')
raw_Data = r.text
soup = BeautifulSoup(raw_Data, 'html.parser') # Der html.parser legt den Parser fest. würde auch ohne gehen, wirft dann aber eine Fehlermeldung
title = soup.title
title_Name = soup.title.name # Der name des Tags
title_content = soup.title.string
print('Der Titel ist : ', title)
print('Der tag name des Titels ist :', title_Name)
print('Der Inhalt des Titels ist :', title_content)
print(soup.p) # Druckt den ersten 'p'Tag aus den er finden kann
print(soup.find_all('li'))
print('Hier kommt jetzt der gesamte Text der Website :',
        soup.get_text())