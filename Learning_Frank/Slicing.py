# Link zu Hyperskill
https://hyperskill.org/learn/step/6177
# funktioniert mit 'list' , 'string', 'tupels'

1. Einzelnen Wert aufrufen
2. Bereiche von Werten aufrufen
3. Alles ab bestimmten Index zurückgeben
4. Slicing mit Steps 
5. Standardwerte von slice benutzen
6. Erstellen einer unabhängigen Kopie der sequence
7. Verwenden negativer Indexe und negativer Steps

    Grundsätzliche Syntax:
    sequence[start:stop:step]
    
    sequence[:end]    # element from the 1st element to end-1
    sequence[start:]  # elements from start to the last element
    sequence[:]       # the full copy of the sequence
    sequence[::step]  # every element with a given step

1. Einzelnen Wert aufrufen
------------------------------------------------------------------------------
    fib_nums = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    print(fib_nums[0]) # 0 the first Element
    print(fib_nums[8] # 21 the last Element

2. Bereiche von Werten aufrufen
-------------------------------------------------------------------------------
    print(fib_nums[2:5] # [1, 2, 3]
    
    text = 'Python is not only a snake!'
    print(text[10:18])  # 'not only'

3. Alles ab bestimmten Index zurückgeben
-------------------------------------------------------------------------------
- wenn der Endindex höher ist als der Index des letzten Elements
    wird kein Fehler ausgelöst. Statt dessen werden alle Elemente
    bis zum Ende der Sequenz zurückgegeben
    
    text = 'Python is not only a snake!'
    print(text[10:9999])  # 'not only a snake!'
     
    words = ['Python', 'is', 'not', 'only', 'a', 'snake', '!']
    print(words[2:9999])  # ['not', 'only', 'a', 'snake', '!']
  
4. Slicing mit Steps 
-------------------------------------------------------------------------------
    Grundsätzliche Syntax:
    sequence[start:stop:step]
    Der Wert des Startindexes ist im return enthalten, der Wert des Stopindexes ist nicht
    im return enthalten.
    
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    print(planets[2:7:2])  # ['Earth', 'Jupiter', 'Uranus']
    
    Beim Rückwärtszahlen ist wichtig, das der Startindex > Stopindex ist. Auch hier gilt
    das der Wert des Stopindex nicht im return enthalten ist.
    # Elemente von Index 4 bis Index 16 in umgekehrter Reihenfolge ausdrucken. Man beachten
    # den stop Index (4 -> 3 )
    numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
           22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
    print(numbers[16:3:-1]) # [34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10]
  
5. Standardwerte von slice benutzen 
-------------------------------------------------------------------------------
- Jeder Teil von slice hat einen Standartwert. Wenn wir den Startindex nicht angeben,
    wird er als '0' angenommen. Geben wir den Endindex nicht an, wird dieser gleich der
    Länge der Sequenz genommen. Geben wir den Step nicht an, wird er standardmäßig auf 1
    gesetzt.
    
    snakes = ['python', 'cobra', 'viper']
    print(snakes[:2])  # ['python', 'cobra']
     
    degrees_of_two = [1, 2, 4, 8, 16, 32, 64, 128]
    print(degrees_of_two[4:])  # [16, 32, 64, 128]
     
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    print(colors[::3])  # ['red', 'green', 'violet']

6. Erstellen einer unabhängigen Kopie der sequence
-------------------------------------------------------------------------------
   Mit [:] kann man eine unabhängige Kopie der zu bearbeitenden Sequence erzeugen
   
   sheep = ['Dolly', 'Polly', 'Molly']
   cloned_sheep = sheep[:]  # ['Dolly', 'Polly', 'Molly']
   
   
7. Verwenden negativer Indexe
------------------------------------------------------------------------------
    Indexe können auch negativ sein. Wenn dies der Fall ist, zählt der Index von
    rechts nach links.
    Der Startindex hier ist 1
    
    pets = ['dog', 'cat', 'parrot', 'gecko']
 
    print(pets[-2:])   # ['parrot', 'gecko']
    print(pets[:-2])   # ['dog', 'cat']
    print(pets[::-1])  # ['gecko', 'parrot', 'cat', 'dog'] Umgekehrte Kopie 
    print(pets[::-2])  # ['gecko', 'cat']
    
    Bei der Verwendung negativer Steps ist zu beachten, das der Startindex größer als
    der end Index ist.
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
    print(numbers[7:2:-1])  # [8, 7, 6, 5, 4]
    print(numbers[2:7:-1])  # []