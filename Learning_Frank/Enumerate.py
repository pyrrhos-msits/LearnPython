'''
http://openbook.rheinwerk-verlag.de/python/19_008.html#i19_98

https://book.pythontips.com/en/latest/enumerate.html

- Enumerate ist eine Built in Function für Python
Die Funktion enumerate erzeugt ein iterierbares Objekt, das nicht allein 
über die Elemente von iterable iteriert, sondern über Tupel der Form (i, iterable[i]). 
Dabei ist i ein Schleifenzähler, der bei 0 beginnt. 
Die Schleife wird beendet, wenn i den Wert len(iterable)-1 hat

Syntax: enumerate(iterable, start)
'''


list = ['apfel', 'birne','ananas', 'kohl']

# Gibt Liste als Liste von Tupeln aus
print('Liste von Tupeln')
for el in enumerate(list):
    print(el)

# Gibt den Index und den Wert der Elemente der Liste aus
print('\nGibt den Index und den Wert aus')
for i, wert in enumerate(list):
    print('Der Index ist ', i,'Der Wert ist ', wert)

# Beispiel für das Verwenden eines optionalen Parameters
# der optionale Index setzt also den Start Index auf den Wert
# hinter dem Komma (hier 1) 
counter = enumerate(list,1) #sollte jetzt erst bei Index 1 starten

for el in counter:
    print(el)



