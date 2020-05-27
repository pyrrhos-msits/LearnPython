import os
import sys
from collections import deque



nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.
'''
bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
of Apollo 11, and Neil Armstrong -- the first man to walk
on the moon. It was the height of the Cold War, and the charts
were filled with David Bowie's Space Oddity, and Creedence's
Bad Moon Rising. The world is a very different place than
it was 5 decades ago. But how has the space race changed since
the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey
addressed Apple Inc. employees at the iPhone maker’s headquarters
Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''
url = ['bloomberg', 'nytimes']
#dirName = 'tb_tabs'
dirName = sys.argv[1]
#print(dirName)
if not os.path.exists(dirName):
    os.mkdir(dirName)

# Funktionsdefinitionen --------------------------------------------------------------------------


pages = deque()# Stapel für die Aufgerufenen Dateien

while True:
    site = input()
    if '.' in site:
        short = site[:site.rfind('.')]#kurzbezeichnung der Seite. Alles nach dem '.'
                                      #wird abgeschnitten
    else:
        short = site # wenn kein '.' im Dateinamen

    dateiname = dirName + "\\" + short + ".txt" # dateiname z.B: tb_tabs\bloomberg.txt

    if site == 'exit': #bei Eingabe von exit ist Schluss
        sys.exit()

    if site == 'back':
        pass
    # function path_exists
    elif os.path.exists(dateiname): # Wenn der Dateiname existiert , d.h. wenn die Seite
                                    # vorher schon mal aufgerufen wurde, zeige die Datei an
        file = open(dateiname, 'r', encoding='utf-8')
        print(file.read())
        file.close()
        continue

    elif '.' in site and short in url: # wenn der Dateiname nicht existiert aber ein '.'
                                        # im input vorhanden ist, sieh in der Liste url nach
                                       #  ob die Seite dort existiert
        if short == 'bloomberg':       # wenn die Seite existiert zeige sie an
            print(bloomberg_com)
        if short == 'nytimes':
            print(nytimes_com)

        file = open(dateiname, 'w', encoding='utf-8') # Nach dem die Seite angezeigt wurde,
                                                      # wird jetzt die Datei geschrieben
        if short == 'bloomberg':
            file.write(bloomberg_com)
            file.close()
            continue
        elif short == 'nytimes':
            file.write(nytimes_com)
            file.close()
            continue

    elif '.' in site and short not in url:# wenn die Seite nicht in url vorhanden ist
        print('error')                    # drucke eine Fehlermeldung aus
        continue
    else:                               # wenn kein '.' im input und die Seite nicht in url
        print('error')                  # steht, drucke Fehler
        continue




