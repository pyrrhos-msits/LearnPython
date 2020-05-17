https://docs.python.org/3/library/random.html

# zuerst Modul importieren
import random
# Pseudozufallszahl zwischen 0 und 1
print(random.random()# 0.5557276751294531

# manuelle Angabe des Seeds | Man kann einen eigenen Wert angeben
# oder die Klammer leer lassen. Im Falle der leeren Klammer wird
# standardmäßig die aktuelle Systemzeit genommen
random.seed()
print(random.random()) # z.B.: 0.956177930864557

# Random Basic Functions
random.uniform(a,b) # gibt eine random floatnummer im Bereich zwischen a und b zurück
print(random.uniform(3, 100))# 35.94079523197162

random.randint(a,b)# gibt random Integer im Bereich zwischen a und b zurück
print(random.randint(35, 53)) # 52

# random.choice
random.choice(seq) # gibt eine zufälligen Buchstaben aus dem String zurück
print(random.choice('Voldemort')) # m

wordlist = ['python', 'java', 'kotlin', 'javascript']
current_word = random.choice(wordlist) # hier das zufällige Wort aus der Wortliste
print(current_word)

random.randrange(a, b, c)# gibt einen Nummer im Bereich zwischen a und b zurück mit step c 
print(random.randrange(3, 100, 5)) # 18 

random.shuffle(seq, [random]) # durmischt eine sequenz. ACHTUNG funktioniert nicht mit unveränderlichen Datentypen
tiny_list = ['a', 'apple', 'b', 'banana', 'c', 'cat']
random.shuffle(tiny_list)
print(tiny_list) # ['apple', 'banana', 'a', 'cat', 'b', 'c']

random.sample(population, k) # gibt eine Zufallsliste aus k elementen der population zurück. 
print(random.sample(range(100), 3)) # [24, 33, 91]
