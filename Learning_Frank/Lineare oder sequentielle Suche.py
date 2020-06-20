'''
Lineare Suche mit Enumerate möglich.
Hier wird der Index des Eintrages gefunden
'''

names = ["Alice", "Bob", "Mike", "Kate", "John", "Bill", "Andrew", "David"]

def search(elements, target):
    index = -1

    for i, elem in enumerate(elements):
        if elem == target:
            index = i
            break

    return index

print(search(names, "Alice"))  # 0
print(search(names, "Bob"))  # 1
print(search(names, "Andrew"))  # 6
print(search(names, "Tomas"))  # -1
print(search(names, "Ann"))  # -1
print(search(names, "Oliver"))  # -1

'''
Man kann auch mit dem 'in' Operator prüfen, ob ein Element
in einer Liste vorhanden ist. Hierbei wird boolean 'True'
oder 'False' ausgegeben.
'''
names = ["Alice", "Bob", "Mike", "Kate", "John", "Bill", "Andrew", "David"]
print("Alice" in names)  # True
print("Bob" in names)  # True
print("Andrew" in names)  # True
print("Tomas" in names)  # False
print("Ann" in names)  # False
print("Oliver" in names)  # False

'''
Suche nach Werten in sortierten Listen:
Funktioniert genauso wie mit enummerate im Beispiel 1. Aber
hier wird noch eine zusätzliche Kondition eingefügt die prüft
ob das aktuelle Element größer ist als Target. Wenn dies der 
Fall ist bricht er sofort ab. 
'''


def search(elements, target):
    index = -1

    for i, elem in enumerate(elements):
        if elem == target:
            index = i
            break

        if elem > target:
            break

    return index