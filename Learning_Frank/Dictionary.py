https://hyperskill.org/learn/step/6481

1. Creation of an dictionary
2. Zugriff auf die Elemente
3. Auswählen der keys

1. Creation of an dictionary
-------------------------------------------------------------------------------
    Syntax: dict = {key : value, key : value, key : value}
    leeres dictionary anlegen : empty_dict = {}
    Die Werte innerhalb eines dictionarys können unterschiedliche Datentypen sein
    
        birds = {"pigeon": 12, "sparrow": 5, "red crossbill": 1}
        prices = {'espresso': 5.0, 'latte': 10, 'pastry': 'various prices'}
        empty_dict = {}
         
        print(type(birds))  # <class 'dict'>
        print(type(prices))  # <class 'dict'>
        print(type(empty_dict))  # <class 'dict'>
    
    Anlegen unter Verwendung des dict Constructors
        another_empty_dict = dict()  # using the dict constructor 
        print(type(another_empty_dict))  # <class 'dict'>    

    Anlegen eines nested dictionary
        # a nested dictionary example
        my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
                   'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}
         
        # another nested dictionary example
        # note that keys of the outer dictionary are numbers
        digits = {1: {'Word': 'one', 'Roman': 'I'}, 
                  2: {'Word': 'two', 'Roman': 'II'}, 
                  3: {'Word': 'three', 'Roman': 'III'}, 
                  4: {'Word': 'four', 'Roman': 'IV'}, 
                  5: {'Word': 'five', 'Roman': 'V'}}    
                  
2. Zugriff auf die Elemente
-------------------------------------------------------------------------------
    Für lesen und schreiben ist die Syntax die selbe. square brackets mit einem
    key darin 
    
        my_pet = {}
        # add 3 keys and their values into the dictionary
        my_pet['name'] = 'Dolly'
        my_pet['animal'] = 'dog'
        my_pet['breed'] = 'collie'
        print(my_pet)  # {'name': 'Dolly', 'animal': 'dog', 'breed': 'collie'}
        # get information from the dictionary about an added item
        print(my_pet['name'])  # Dolly
        
    Zugrif auf elemente in nested dictionaries
    Man muss sich zuerst auf die richtige Ebene hangeln
        # our nested dictionary once again:
        my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
                   'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}
         
        print(my_pets['cat'])  # {'name': 'Fluffy', 'breed': 'maine coon'}
         
        print(my_pets['cat']['breed'])  # maine coon 
        
3. Auswählen der keys
-------------------------------------------------------------------------------
    keys müssen unique sein.
    Wenn ein key bereits vorhanden ist wird der Wert durch eine neuzuweisung
    überschrieben:
        trilogy = {'IV': 'Star Wars', 'V': 'The Empire Strikes Back', 'VI': 'Return of the Jedi'}
        print(trilogy['IV'])  # Star Wars
         
        trilogy['IV'] = 'A New Hope'
        print(trilogy['IV'])  # A New Hope    
        
    Ab Python 3.7 wird die Reihenfolge der keys beim Anlegen des dictionaries beibehalten
        alphabet = {}
        alphabet['alpha'] = 1
        alphabet['beta'] = 2
         
        print(alphabet)
