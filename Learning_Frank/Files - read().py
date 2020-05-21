Gegeben ein file 'animals.txt'
    - dog
    - cat
    - rabbit
    - sea turtle
    - penguin
 
- Zum lesen kann man folgende Methoden nutzen:
    - read(size)
    - readline(size)
    - readlines()
    - standard foor loop
    
- read()
    file = open('animals.txt', 'r')
    print(file.read())
    # The output:
    # Dog
    # Cat
    # Rabbit
    # Sea turtle
    # Penguin
     
    file.close()
    
- readline(3)
    soll 3 bytes aus jeder Zeile drucken, macht er aber nicht, weil die escape 
    sequenz '\n' jeweils mitgezählt wird
        file = open('animals.txt', 'r')
        print(file.readline(3))
        print(file.readline(3))
        print(file.readline(3))
        print(file.readline(3))
        print(file.readline(3))
        print(file.readline(3))
         
        # The output:
        # Dog
        # 
        # 
        # Cat
        # 
        # 
        # Rab
        # bit
         
         
        file.close()
        
- readlines()
    - liest alle Zeilen aus der Datei und gibt diese mit '\n' zurück
    - Mann kann mit index darauf zugreifen file[1] = 'cat'
        file = open('animals.txt', 'r')
        print(file.readlines())
        # The output:
        # ['Dog\n', 'Cat\n', 'Rabbit\n', 'Sea turtle\n', 'Penguin']
         
        file.close()

- foor loop
    - der beste Weg um Daten Zeile für Zeile auszulesen
        file = open('animals.txt', 'r')
        for line in file:
            print(line)
         
        # The output:
        # Dog
        # 
        # Cat
        # 
        # Rabbit
        # 
        # Sea turtle
        # 
        # Penguin
         
        file.close()
