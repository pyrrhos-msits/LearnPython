1. write()
2. writelines()
3. an Datei anhängen nicht mit 'w' überschreiben

1. write()
-------------------------------------------------------------------------------
# zuerst muss das file natürlich geöffnet werden, Schreibparameter nicht vergessen
file = open('test_file.txt', 'w', encoding='utf-8')
file.write('This is a line in a testfile!')
file.close()
# schließen nicht vergessen

Zu beachten, die Daten werden so in das File geschrieben wie sie sind.
Wenn ich jetzt also etwas zu dieser o.g Datei hinzufüge, wird dies ohne
Leerzeichen einfach an den vorhandenen Text angehängt. Es sei denn, ich 
benutze die 'Escape-Sequencen':
- Newline : '\n', 'r', '\r\n'  http://python-ds.com/python-3-escape-sequences

# Beispiel >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Wir haben eine Liste mit Namen und möchten diese in eine Datei schreiben. Jeder
Name soll in einer neuen Zeile stehen:

names = ['Frank', 'Sabine', 'Franzi']

name_file = open('Namenliste.txt', 'w', encoding= 'utf-8')

for name in names:
    name_file.write(name + '\n')

name_file.close()

Drucken wir diese Zeichen jetzt als Liste, kommt folgendes:
['Frank\n', 'Sabine\n', 'Franzi\n']

Wenn wir alle Namen in einer Zeile haben wollen, müsste in der for schleife anstelle
des 'n' ein ' ' stehen. Dann würde hinter jedem Namen ein Leerzeichen kommen.


2. writelines()
-------------------------------------------------------------------------------
Nimmt eine iterierbare Folge von Zeichenfolgen und schreibt sie in eine Datei.
Auch hier ist wichtig, das alle Zeilenumbrüche oder Leerzeichen mitgegeben werden.

# selbe Beispiel wie oben mit writelines()

names = ['Frank\n', 'Sabine\n', 'Franzi\n']
name_file = open(Namenliste.txt', 'w', encoding='utf-8')
name_file.writelines(names)

Dieser code erzeugt dieselbe Datei. Der Unterschied ist, das hier die Trennzeichen 
bereits in der Liste 'names' vorhanden sind.

3. an Datei anhängen nicht mit 'w' überschreiben
-------------------------------------------------------------------------------
Die option 'w' in open() überschreibt ja alle vorhandenen Daten. Wenn ich also 
keine komplett neue Datei erzeugen will, sondern nur Daten anhängen will, darf
ich 'w' nicht verwenden sondern muss 'a' nehmen. Auch hier wird eine neue Datei
erzeugt, wenn keine Datei vorhanden ist.

# Beispiel:
name_file = open('names.txt', 'a', encoding='utf-8')
name_file.write('Rachel\n')
name_file.close()


