# Generatoren brauchen weniger  Speicher

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