# Generatoren brauchen weniger  Speicher

1. Generator erstellen mit Generator function
2. Generator erstellen mit expressions
3. Übungen


1. Generator erstellen mit Generator function
-------------------------------------------------------------------------------
    def multiples(a, n):
        i = 1
        result = []
        while i <= n:
            result.append(a * i)
            i += 1
        return result


    print(multiples(3, 5)) # Outputs [3, 6, 9, 12, 15]

    print(multiples(2, 3)) # Outputs [2, 4, 6]

    # Die selbe Funktion mit Generator
    # Statt 'return' benutzen wir 'yield'
    def multiple(a, n):
        i = 1
        while i <= n:
            yield a*i
            i += 1

#zum Aufruf der Funktion müssen wir explizit jeden Step mit 'next' aufrufen
    print(multiple(2,5))
    multple_of_three = multiple(3 , 9)
    print(next(multple_of_three))# 3
    print(next(multple_of_three))# 6
    # Ohne Variablenzuweisung scheint es nicht zu gehen
    # im folgenden wird immer der selbe Wert zurück gegeben
    print(next(multiple(2, 3)))# 2
    print(next(multiple(2, 3)))# 2

2. Generator erstellen mit expressions
-------------------------------------------------------------------------------
# entspricht comprehension aber anstelle von eckigen Klammern [] 
# verwendet man runde () Klammern für die definition des Generators

    numbers = [1, 2, 3]
    my_generator = (n ** 2 for n in numbers)
    next(my_generator) # 1
    next(my_generator) # 4
    next(my_generator) # 9
# Im Gegensatz dazu List comprehension
    my_list = [n ** 2 for n in numbers]
    print(my_list) # [1, 4, 9]
    
3. Übungen

    def letters(word):
    for el in word:
        yield el
        
# Nächstes Beispiel >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
https://hyperskill.org/learn/step/8275
n = int(input())

def even(num):
    ev = 0
    ct = 0
    while ct < num:
        yield ev
        ct += 1
        ev += 2

evenprt = even(n)
for _ in range(n):
    print(next(evenprt))
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<