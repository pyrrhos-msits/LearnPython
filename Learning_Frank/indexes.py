- Index startet mit 0
- Abfrage mit eckigen Klammern

1. Letzen Index in einer Liste finden
2. Finden des Indexes eines bestimmten Wertes in einer Liste
3. Finden des Indexes eines bestimmten Wertes in einem String

1. Letzen Index in einer Liste finden
-------------------------------------------------------------------------------
- letzte Position len(list)-1
	sentence = input()
	print(sentence[len(sentence) - 1])
- Negative Indexe starten von hinten bei -1

2. Finden des Indexes eines bestimmten Wertes in einer Liste
-------------------------------------------------------------------------------
    Finden des indexes eines Wertes in einer Liste 
    list = [2, 3, 5, 7, 9]
    for index in range(len(list)):
        print('Der index ist :', index, 'Der Wert lautet :' , list[index])

    for el in range(len(newList)): # Hier wird der INDEX ausgegeben. Nicht der Wert
       print(el)

    Einfacher geht es so:
    list = [2, 3, 4, 5, 7, 9]
    end = list.index(4)
    print(list[:end])
    
3. Finden des Indexes eines bestimmten Wertes in einem String
-------------------------------------------------------------------------------
    email = 'john.andrew.smith@yougotmail.com '
    end = email.index('@')
    print(email[:end])

< Zugriff auf einzelne Elemente >
colors = ['red', 'green', 'blue']
first_elem = colors[0]   # 'red'
second_elem = colors[1]  # 'green'
third_elem = colors[2]   # 'blue'

< Zugriff auf einzelne Buchstaben eines Wortes >
colors = ['red', 'green', 'blue']
first_elem = colors[0]   # 'red'
second_elem = colors[1]  # 'green'
third_elem = colors[2]   # 'blue'

<Neuzuweisung eines strings in einer Liste ist möglich >
colors = ['red', 'green', 'blue']
colors[1] = 'white'
print(colors)  # ['red', 'white', 'blue']

<Neuzuweisung eines Buchstaben in einem String führt zu einer Fehlermeldung>
pet = "cat"
pet[0] = "b"
# TypeError: 'str' object does not support item assignment
< Beispiele für Verwendung Negativer Indexe >
colors = ['red', 'green', 'blue']
last_elem = colors[-1]    # 'blue'
second_elem = colors[-2]  # 'green'
first_elem = colors[-3]   # 'red'
 
pet = "cat"
last_char = pet[-1]    # 't'
second_char = pet[-2]  # 'a'
first_char = pet[-3]   # 'c'

<element an erster Stelle finden mit negativem index>
- verwenden von -len
name = input()
print(name[-len(name)])