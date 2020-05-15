# Sets unterstützen kein Indexing
# in Sets kommt jeder Wert nur einmal vor


# Anlegen von Sets im Unterschied zu dictionaries
empty_set = set()
print(type(empty_set))   # <class 'set'>
empty_dict = {}
print(type(empty_dict))  # <class 'dict'>

# Zerlegen eines Strings mit set. Doppelte Buchstaben werden entfernt
string = 'aabbccdd'
print('\nString zerlegen mit set() :', set(string))

# Entfernen doppelter Einträge aus einer Liste mit Set
states = ['Russia', 'USA', 'USA', 'Germany', 'Italy']
print("\nEntfernen doppelter Einträge aus einer Liste mit Set :", set(states))  # {'Russia', 'USA', 'Italy', 'Germany'}

# Hinzufügen eines Elementes zu Set mit 'add()'
nums = {1, 2, 2, 3}
nums.add(5)
print("\nHinzufügen eines Elementes zu Set mit 'add()'", nums)

# Entfernen von allen Elementen eines Wertes vom Set mit remove()
# Wenn Element nicht vorhanden 'KeyError'
nums = {1, 2, 2, 3}
nums.remove(2)
print('\nEntfernen von allen Elementen eines Wertes vom Set mit remove():', nums)  # {1, 3}
# Entfernen von allen Elementen eines Wertes vom Set mit discard()
# Wenn Element nicht vorhanden, keine Fehlermeldung
nums = {1, 2, 2, 3}
nums.discard(2)
print('\nEntfernen von allen Elementen eines Wertes vom Set mit discard():', nums)  # {1, 3}

# Zufälliges Element entfernen mit pop() Da zufällig kein Argument
nums = {1, 2, 2, 3}
nums.pop()
print('\nZufälliges Element entfernen mit pop() :', nums)  # {2, 3}

# Alle Elemente von Set entfernen mit clear()
nums = {1, 2, 2, 3}
nums.clear()
print('\nAlle Elemente von Set entfernen mit clear() :', nums)  # set()

# Hinzufügen mehrerer neuer Elemente mit update() | Doppelte Einträge werden entfernt
nums = {1, 2, 2, 3}
nums.update({5 , 8 , 9, 9})
print('\nHinzufügen mehrerer neuer Elemente mit update() :', nums)  # {1, 2, 3, 5, 8, 9}

'''Wichtig für die folgenden methoden'''
''' Die folgenden Methoden kann man sowohl als Methode als auch mit einem Operator ausführen
Hierbei ist zu beachten, das beim Ausführen mit einem Operator beide Argumente Sets sein müssen.
Wenn man die entsprechende Methode verwendet, muss nur das erste Argument ein Set sein. Das zweite
kann ein beliebiges iterierbares Objekt sein, z.B Liste oder String. In diesem Fall erzeugt die Methode
automatisch ein Set aus diesem Objekt'''

'''Union'''
# Zwei Sets zusammenfügen mit union()
china = {'Peking', 'Hanoi'}
auto = {'VW', 'Audi'}
print('\nZwei Sets zusammenfügen mit union() :' ,china.union(auto))
# Zwei Sets zusammenfügen mit '|'
print("Zwei Sets zusammenfügen mit '|' : ", china | auto)
# Zwei sets zusammenfügen mit |= und update()
ghostbusters = {'Peter', 'Raymond', 'Egon'}
soldiers = {'Winston'}
secretaries = {'Janine'}
ghostbusters |= soldiers
print("Zwei sets zusammenfügen mit |=  :", ghostbusters)
ghostbusters.update(secretaries)
print("Anschließend mit 'update() ein drittes set() hinzufügen :", ghostbusters)

'''Intersection oder '&' Operator '''
# Vergleich mehrerer Sets miteinander. Gibt die gemeinsamkeit aus
light_side = {'Obi-Wan', 'Anakin'}
dark_side = {'Palpatine', 'Anakin'}
both_sides = light_side.intersection(dark_side)
print("\nVergleich mit 'intersection()' druckt nur die Unterschiede zwischen den sets aus :", both_sides)
print("Intersection mit \b'&' Operator:", light_side & dark_side)

'''Difference  oder '-' Operator '''
# Entfernt alle Element die im anderen Set vorhanden sind
painters = {'Klimt', 'Michelangelo', 'Picasso'}
ninja_turtles = {'Michelangelo', 'Leonardo'}
print('\nEntfernung aller gleicher Elemente mit difference() :', painters.difference(ninja_turtles))
# The output is {'Klimt', 'Picasso'}
painters = {'Klimt', 'Michelangelo', 'Picasso'}
ninja_turtles = {'Michelangelo', 'Leonardo'}
print("Entfernung aller gleicher Elemente mit '-' Operator :",painters - ninja_turtles)
# The output is {'Klimt', 'Picasso'}

''' differenc_update oder '-=' Operator'''
# Entfernt alle im zweiten set vorhandenen Elemente aus dem ersten set
criminals = {'Al Capone', 'Blackbeard', 'Bonnie and Clyde', 'Frank und Sabine'}
gangsters = {'Al Capone', 'Frank und Sabine'}
pirates = {'Blackbeard'}
print('\nEntfernt alle im zweiten set vorhandenen Elemente aus dem ersten set mit difference_update(): ', pirates)

criminals.difference_update(gangsters)
criminals -= pirates
print('Entfernt alle im zweiten set vorhandenen Elemente aus dem ersten set mit "-=" Operator :', criminals)
# The output is {'Bonnie and Clyde'}

'''Sets aus einem Container auspacken mit '*' Operator'''
# sets are within a container
languages = [{'c', 'c++', 'python'}, {'python', 'javascript'}, {'python', 'java'}]
the_best = set.intersection(*languages)
print("\nSets aus einem Container auspacken mit '*' Operator :", the_best)
# The output is {'python'}