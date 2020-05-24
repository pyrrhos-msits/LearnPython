import os
import sys



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
dirName = 'tb_tabs'
# dirName = sys.argv[1]
if not os.path.exists(dirName):
    os.mkdir(dirName)


while True:
    site = input()
    if '.' in site:
        short = site[:site.rfind('.')]
    else:
        short = site
    dateiname = dirName + "\\" + short + ".txt"
    if site == 'exit':
        sys.exit()
    # Wenn der Dateiname existiert zeige die Datei an
    elif os.path.exists(dateiname):
        file = open(dateiname, 'r', encoding='utf-8')
        print(file.read())
        file.close()
        continue
    elif '.' in site and short in url:
        file = open(dateiname, 'w', encoding='utf-8')
        if short == 'bloomberg':
            file.write(bloomberg_com)
            file.close()
            continue
        elif short == 'nytimes':
            file.write(nytimes_com)
            file.close()
            continue
    elif '.' in site and short not in url:
        print('Unknown url')
        continue
    else:
        print('error')











# lst_dt_indx = site.rfind('.') # ermittelt index vom letzten dot
# shrt_input = site[:lst_dt_indx]# schneidet ab letztem dot ab


