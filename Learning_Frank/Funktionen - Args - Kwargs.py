# Wenn man sich nicht sicher ist wie viele Argumente
# einer Funktion übergeben werden sollen
# Die zusätzlichen Argumente werden als Tupel gespeichert
# Syntax: *args (Jeder Name ist erlaubt solange ein Sternchen davor ist)
def add(a, b, *args):
    total = a + b
    for el in args:
        total += el
    print('Die Länge von "args" ist: ', len(args))
    print('Das Ergebnis ist :', total)

add(4, 5, 2, 5, 7) # 3 args
add(4, 5) # 0 args

# Reihenfolge der Argumente in der Funktion
def function(positional_args, default, *args):
    pass

# Sobald alle erforderlichen Argumente übergeben wurden,
# werden die verbleibenden Argumente in ein Tupel gepackt

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# die Parameter die nach *args kommen, sind nur Schlüsselwörter
# das bedeutet sie können nur als Schlüsselwörter und nicht als
# Positionsargumente verwendet werden.
def recipe(*args, sep=" or "):
    return sep.join(args)

print(recipe("meat", "fish", "Fleisch"))  # meat or fish or Fleisch
print(recipe("meat", "fish", "Fleisch", sep=" and "))  # meat and fish and Fleisch

'''Auspacken in Funktionsaufrufen'''
# Ein Sternchenoperator packt ein Iterable aus
print('fun')
print([5, 4, 3])
print(*'fun')
print(*[5, 4, 3])
# Das * ersetzt die einzel Schreibweise wie z.B.: print('f','u','n')

def add(*args):
    total = 0
    for el in args:
        total += el
    print('Total =',total)

add(7,8,9,3)
# ist das selbe wie:
my_number = [7, 8, 9, 3]
large_number = [444, 555, 999]
add(*my_number)# oder
add(*large_number)

# **kwargs wenn unbekannte Anzahl Keywordarguments übergeben werden soll
# speichert alle Werte in einem Dictionary
# **kwargs erwartet Schlüsselwörter

def capital(**kwargs):
    for key, value in kwargs.items():
        print(value, 'ist die Hauptstadt von', key)

capital(Canada="Ottawa", Estonia="Tallinn", Venezuela="Caracas", Finland="Helsinki")
# WICHTIG die Syntax key = value

# Kombination von *args und *kwargs ist möglich
def func(positional_args, defaults, *args, **kwargs):
    pass
# WICHTIG Die Reihenfolge

'''Funktionsaufrufe auspacken'''
# In Python gibt es zwei Entpackungsoperatoren
# * für iterierbare Objekte
# ** für Dictionaries
a = ['Frank', 'Sabine', 'Fred']
print(*a)


def say_bye(**names):
    for name in names:
        print("Au revoir,", name)

humans = {"Laura": {"age": 34, "fave_color": "purple"},
          "Robin": {"age": 28, "fave_color": "turquoise"}}

say_bye(**humans)
