1. Was sind 'Magic Methods'
2. __new__ vs __init__
3. __str__ vs __repr__

1. Was sind 'Magic Methods'
---------------------------------------------------------------
-   Magic Methods sind in der Klassendefinition erkennbar durch
    doppelte Unterstriche davor und dahinter. Ein Beispiel ist 
    __init__
-   Man nennt diese Methoden auch 'Dunders'. Es gibt viel mehr
    als hier dargestellt
   
2. __new__ vs __init__
----------------------------------------------------------------
-   wir haben __init__ bisher als constructor der Klasse gesehen.
    Tatsächlich ist es aber ihr initializer. Neue Objekte der Klasse
    werden tatsächlich durch die __new__ Methode erstellt. Diese 
    wiederum ruft in sich die __init__ Methode auf.
-   Das erste Element der __new__ Methode ist 'cls'. 'cls' repräsentiert
    die Klasse selbst. Die Methode gibt eine neue Instanz der Klasse 
    zurück, die dann an die __init__ Methode übergeben wird.
-   Normalerweise braucht man __new__ nicht. Aber sie kann nützlich sein,
    wenn wir Instanzen anderer Klassen zurückgeben oder die Anzahl der
    Objekte in unserer Klasse einschränken wollen.
# Beispiel:
    Wir haben eine Klasse 'Sun' und wollen sicherstellen, das wir 
    nur ein Objekt dieser Klasse erstellen. Wir definieren eine Klassen-
    variable, welche die Nummer der Instanzen trackt, und die Erstellung
    neuer Instanzen verhindert, wenn das Limit erreicht ist.
    
    class Sun:
        n = 0
 
        def __new__(cls):
            if cls.n == 0:
                instance = object.__new__(cls)
                cls.n += 1
                return instance
    
    Wenn wir jetzt versuchen zwei Objekte zu erstellen wird beim zweiten 
    Objekt eine Fehlermeldung geworfen.
    
    sun1 = Sun()
    sun2 = Sun()
 
    print(sun1)  # <__main__.Sun object at 0x1106884a8>
    print(sun2)  # None
            
3. __str__ vs __repr__
-   Mit __str__ oder __repr__ wird der Ausdruck des Objectes möglich gemacht.
-   Dabei ist __str__  der Ausdruck für den User und __repr__ für den Developper
-   Regel ist, immer die __repr__ Methode zuerst zu definieren. Diese wird vom 
    Developper genutzt und ist ein Fallback für __str__.
    
    # Beispiel
    
    class Transaction:
        def __init__(self, number, funds):
            self.number = number
            self.funds = funds
            self.status = "active"
            
    payment = Transaction("000001", 9999.999)
    print(payment)
    # example of the output: <__main__.Transaction object at 0x11068f5f8>
                
    # Jetzt das selbe Beispiel mit __repr__ Methode
    class Transaction:
        def __init__(self, number, funds):
            self.number = number
            self.funds = funds
            self.status = "active"
 
        def __repr__(self):
            return "Transaction {}. Amount: {}. Status: {}".format(self.number,
                                                                   self.funds,
                                                                   self.status)
                                                                   
    payment = Transaction("000001", 9999.999)
    print(payment)
    # Transaction 000001. Amount: 9999.999. Status: active
    
    