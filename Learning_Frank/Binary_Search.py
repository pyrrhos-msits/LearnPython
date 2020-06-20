
#1. Iterative Implementierung
#2. Rekursive Implementierung

''' 
- Funktioniert nur in sortierten Arrays
- Das Array wird bei jeder Iteration in 2 Subarrays aufgeteilt
- dann wird geschaut ob der Wert kleiner oder größer ist al s die Mitte
- dann wird das Subarray wieder aufgeteilt
-  Der Vorgang wird fortgesetzt, bis entweder das mittlere und das Zielelement 
    gleich sind oder die aktuelle Liste leer ist. 
    Im letzten Fall gibt der Algorithmus -1 zurück. 
    Dies zeigt an, dass der Zielwert nicht gefunden wurde.
'''


#1. Iterative Implementierung

    #Syntax:
    def binary_search(elements, target):
    left, right = 0, len(elements) - 1
 
    while left <= right:
        middle = (left + right) // 2
 
        if elements[middle] == target:
            return middle
        elif target < elements[middle]:
            right = middle - 1
        else:
            left = middle + 1
 
    return -1

''' binary_search verwendet eine sortierte Liste 'elements' und einen Wert 'target'
Als Rückgabewert kommt entweder der Index oder aber wenn er nicht gefunden wurde '-1'
- wir erstellen zuerst 2 Variablen ('left', 'right'). Diese speichern jeweils den
    start und zielindex der Suche
- Bei jedem Schritt der 'while' Schleife vergleichen wir das mittlere Element des 
    aktuellen Bereichs mit dem Zielwert. Ist value element == value 'target', wird
    der Index zurückgegeben
    Wenn target < als element[middle] wird der neue Endwert gesetzt. Wenn nicht wird 
    der Startwert neu gesetzt
- Wenn der Zielwert nicht gefunden wurde, wird '-1' zurück gegeben
'''
    #Beispiel
    elements = [10, 13, 15, 20, 21, 25]
 
    indexof_10 = binary_search(elements, 10)  # 0
    indexof_13 = binary_search(elements, 13)  # 1
    indexof_15 = binary_search(elements, 15)  # 2
    indexof_20 = binary_search(elements, 20)  # 3
    indexof_21 = binary_search(elements, 21)  # 4
    indexof_25 = binary_search(elements, 25)  # 5
    
    indexof_19 = binary_search(elements, 19)  # -1
    indexof_23 = binary_search(elements, 23)  # -1
    indexof_42 = binary_search(elements, 42)  # -1

#2. Rekursive Implementierung

    #Syntax
    def binary_search(elements, target, left, right):
    if left > right:
        return -1
 
    middle = (left + right) // 2
 
    if elements[middle] == target:
        return middle
    elif target < elements[middle]:
        return binary_search(elements, target, left, middle - 1)
    else:
        return binary_search(elements, target, middle + 1, right)

'''
Hierbei übergeen wir die Grenzen des aktuellen Bereichs als Funktionsargumente
    - Zuerst prüfen wir ob der aktuelle Bereich leer ist. Wenn ja 'return -1'
    - Ist dies nicht der Fall
'''  
