import os, sys, requests
from collections import deque



# Variablendeklarationen ------------------------------------------------------------------
website = ''

url = []

dirName = sys.argv[1] #liest den dir name aus den im CLI übergebenen system argumenten (tb_tabs)

tmpSite = ''# Speichert die aktuell angezeigt Seite

pages = deque()# Stapel für die Aufgerufenen Dateien


if not os.path.exists(dirName):
    os.mkdir(dirName)

# Funktionsdefinitionen ###########################################################
# Wenn der Dateiname existiert , d.h. wenn die Seite
def path_exists(dateiname): # vorher schon mal aufgerufen wurde, zeige die Datei an
    file = open(dateiname, 'r', encoding='utf-8')
    print(file.read())
    file.close()
    tmpSite = short
# ----------------------------------------------------------------------------
# Funktion zum zusammenbauen der URL
def check_https(site_input):
    global website
    if site_input.startswith('https://'):
        website = site_input
    else:
        website = 'https://'+site_input
    #print('Website für den Get = ', website)
#----------------------------------------------------------------------------
# Funktion für den get request
def get_request(website):
    #print('Website wurde übergeben an get_request', x)
    r = requests.get(website)
    print(r.text)
    file = open(dateiname, 'w', encoding='utf-8')
    file.write(r.text)


while True:
    site = input()
    if '.' in site:
        short = site[:site.rfind('.')]#kurzbezeichnung der Seite. Alles nach dem '.' wird abgeschnitten
        url.append(short)
    else:
        short = site # wenn kein '.' im Dateinamen

    if short in url:
        pages.append(tmpSite)
        tmpSite = short

    dateiname = dirName + "\\" + short + ".txt" # dateiname z.B: tb_tabs\bloomberg.txt

    if site == 'exit': #bei Eingabe von exit ist Schluss
        sys.exit()

    if site == 'back':
        print('Diese Seite steht in tmpSite :', tmpSite)
        #print('Diese Seite würde jetzt aufgerufen : ', pages.pop())
        #showVariables(pages.pop())




    elif '.' in site and short in url:
        check_https(site) # prüfung on https for der eingabe steht
        get_request(website) # ruft die seite auf

         # Nach dem die Seite angezeigt wurde,
                                                      # wird jetzt die Datei geschrieben





    elif '.' in site and short not in url:# wenn die Seite nicht in url vorhanden ist
        print('error')                    # drucke eine Fehlermeldung aus
        continue
    else:                               # wenn kein '.' im input und die Seite nicht in url
        print('error')                  # steht, drucke Fehler
        continue




