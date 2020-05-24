Kontextmanager sind nötig um eine Überlastung des Systems zu verhindern.

# Ein Kontextmanager wird durch ein withSchlüsselwort gefolgt vom Kontextmanager selbst und dem Namen der Variablen eingeführt. 
# Grundlegende Syntax:
    with statement as variable_name:
        ....

# man kann das auch verschachteln:
    with statement1 as var1:
        with statement2 as var2:
            # und so weiter
            
Am meisten wird with ... bei der Arbeit mit Dateien verwendet
Ein Datenobjekt das wir erhalten wenn wir die open() Funktion verwenden
funktioniert als Kontextmanager. Das stellt dann den 'statement' Teil des
Kontextmanagers dar.

    with open('test.txt') as f:
        #arbeite mit dem File
        ...
Innerhalb von with kann man die Datei explizit mit close() schliessen. Muss es
aber nicht.

# Beispiel schreiben der Werte aus einer Datei in eine andere
#Ursprungsdatei 'tarantino.txt' 

- Öffnen und Zeilen ausdrucken
       with open('tarantino.txt', 'r', encoding='utf-8') as f:
        for line in f:
            # we use strip() to get rid of newline symbols
            print(line.strip())

- Output:
        # Reservoir Dogs
        # Pulp Fiction
        # Jackie Brown
        # Kill Bill: Volume 1
        # Kill Bill: Volume 2
        # Grindhouse: Death Proof
        # Inglorious Basterds
        # Django Unchained
        # The Hateful Eight
        # Once Upon a Time in Hollywood
        
- Öffnen von 'tarantino.txt' umwandeln in lowercase und schreiben in 'tarantino_lowercase.txt'
    with open('tarantino.txt', 'r', encoding='utf-8') as in_file, \
         open('tarantino_lowercase.txt', 'w', encoding='utf-8') as out_file:
        for line in in_file:
            out_file.write(line.lower())
