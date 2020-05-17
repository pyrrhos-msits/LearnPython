multi_elements_list = list('danger!') #mit runden Klammern werden die Buchstaben einzeln gedruckt
print(multi_elements_list)  # ['d', 'a', 'n', 'g', 'e', 'r', '!']
 
single_element_list = ['danger!']# mit eckigen Klammern druckt er das ganze Wort
print(single_element_list)  # ['danger!']

# leere Liste auf zwei Arten definierbar
empty_list_1 = list()
#oder
empty_list_2 = []

# Listen können duplikate enthalten so viel man will
on_off_list = ['on', 'off', 'on', 'off', 'on']
print(on_off_list)  # ['on', 'off', 'on', 'off', 'on']

# Listen können verschiedene typen von Elementen enthalten
different_objects = ['a', 1, 'b', 2]

# Länge einer Liste ermitteln
# function: len
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 5
 
empty_list = list()
print(len(empty_list))  # 0
 
single_element_list = ['danger!']
print(len(single_element_list))  # 1
 
multi_elements_list = list('danger!')
print(len(multi_elements_list))  # 7

# neues Element zu Liste hinzufügen
dragons = []
dragons.append('Kuno')
dragons.append('lisa')
print(dragons)

# liste an andere Liste anfügen
numbers = [1, 2, 3, 4, 5]
numbers.extend([10, 20, 30])
print(numbers)  # [1, 2, 3, 4, 5, 10, 20, 30]

# Liste in andere Liste einfügen
numbers = [1, 2, 3, 4, 5]
numbers.append([10, 20, 30])
print(numbers)  # [1, 2, 3, 4, 5, [10, 20, 30]]

# spezifisches element von Liste entfernen
dragons.remove('lisa')
print(dragons) #['Kuno']

# wenn das zu entfernende element mehrfach vorkommt, 
# wird nur das erste element in der Liste gelöscht
numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21]
numbers.remove(1)
print(numbers)  # [0, 1, 2, 3, 5, 8, 13, 21]

# einfügen eines Elements an einer bestimmten Stelle
# der Liste der erste wert ist der index vor dem der
# Wert eingefügt wird
years = [2016, 2018, 2019]
years.insert(1, 2017)           # [2016, 2017, 2018, 2019]
years.insert(0, 2015)           # [2015, 2016, 2017, 2018, 2019]
years.insert(len(years), 2020)  # [2015, 2016, 2017, 2018, 2019, 2020]

# list.reverse() kehrt die Order der Elemente einer List um
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# list.sort() sortiert die Liste neu. 
# Achtung, die Liste gibt nichts zurück. Sie ändert die Liste tatsächlich
numbers = [3, 2, 5, 4, 1]
numbers.sort()
print(numbers)  # [1, 2, 3, 4, 5]
# umgekehrte Sortierung
numbers = [3, 2, 5, 4, 1]
numbers.sort(reverse=True)
print(numbers)  # [5, 4, 3, 2, 1]
# strings werden in lexikarischer Order sortiert
strings = ['aa', 'b', 'aaa', 'q', 'qq']
strings.sort()
print(strings)  # ['aa', 'aaa', 'b', 'q', 'qq']

# Nested Lists >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

''' Eine Lise in Phyton kann eine andere Liste enthalten. Dies nennt man dann Nested Lists'''

# Beispiel
nested_letters  = ['a', 'b', ['c', 'd'], 'e']
nested_numbers = [[1], [2], [3]]

''' Zugriff auf Nested Lists:
Beim Zugriff wird von aussen nach innen gegangen '''
lists = [0,[1,[2,3]]]
print(lists[1][1][0]) # Result -> 2

''' Versuch auf ein nicht vorhandenes List Element zuzugreifen
wenn es die Ebene nicht gibt wirft folgenden Fehler '''

print(lists[1][1][0][1]) # TypeError: 'int' object is not subscriptable

''' Versuch auf ein Listelement zuzugreifen bei
dem die Ebene zwar vorhanden ist, aber das Element nicht existiert'''

print(lists[3])  # IndexError: list index out of range

''' Mit nested Lists kann mann gut Matrix bauen
Hier ein Beispiel'''

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('{}\n{}\n{}'.format(matrix[0], matrix[1], matrix[2]))

''' gibt eine Matrix aus (Muss in IDE getestet werden)'''
''' Zu beachten, hierbei muss die Länge aller Listen gleich sein'''

'''Wenn wir ein Element aus der Matrix extrahieren wollen, z.B. Element M[1][2] = 6, 
wählt der erste Index die Zeile aus, und der zweite Index wählt die Spalte aus.'''

# Nested Lists Iterationen >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 1. Beispiel Start: -------------------------------------------------------------------
'''Man kann über Nested Lists mit einem for Loop iterieren... '''
school = [["Mary", "Jack", "Tiffany"], 
          ["Brad", "Claire"],
          ["Molly", "Andy", "Carla"]]

student_list = []
for class_group in school:
    for student in class_group:
        student_list.append(student)
'''  oder aber mit nested list comprehensions '''
student_list = [student for class_group in school for student in class_group]

''' Das Resultat ist immer das selbe '''
print(student_list)
# result: ["Mary", "Jack", "Tiffany", "Brad", "Claire", "Molly", "Andy", "Carla"]
# 1. Beispiel Ende---------------------------------------------------------------------

#2. Beispiel Start: -------------------------------------------------------------------

matrix = [] 
  
for i in range(2): 
      
    # create empty row (a sublist inside our list)
    matrix.append([]) 
      
    for j in range(5): 
        matrix[i].append(j)

''' oder '''
matrix = [[j for j in range(5)] for i in range(2)]

'''Das Ergebnis ist auch hier in beiden Fällen das selbe '''
matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]

# 2. Beispiel Ende --------------------------------------------------------------------

my_list =  [[j for j in range(1,3)] for i in range(5)]
print(my_list)
# [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]

# next --------------------------------------------------------------------------------
country_list = [["Moscow", "Cheboksary", "Sochi"], ["Paris", "Lyon", "Nice"],
                ["New York", "Dallas", "San Francisco"]]

long_cities = []
for country in country_list:
    for city in country:
        if len(city) >= 6:
            long_cities.append(city)

print(long_cities)

long_cities = [city for country in country_list for city in country if len(city) >= 6]

print(long_cities)

#--------------------------------------------------------------------------------------

# Zeige nur die Studenten die mit Grade 'A' abgeschlossen haben

students = [["Will", "B"], ["Kate", "B"], ["Max", "A"],
            ["Elsa", "C"], ["Alex", "B"], ["Chris", "A"]]

print([grade[0] for grade in students if grade[1] == "A"])

#--------------------------------------------------------------------------------------

'''Create a list of words from the text below that are shorter than or equal to the input
 value. Print the new list.'''


text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

check = input('enter the string : >')

res = [word for sentence in text for word in sentence if len(word) <= len(check)]
print(res)

