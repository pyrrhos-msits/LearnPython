1. Syntax
2. Übergabe eines Arguments an eine Methode
3. Erstellen von Attributen mit Methoden
4. Modifizierung von Attributen mit Methoden
5. Verwendung von 'return'

1. Syntax


2. Übergabe eines Arguments an eine Methode
--------------------------------------------------------------------------
# in diesem Fall an 'sail'
# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self, destination):
        print("The {} has sailed for {}!".format(self.name, destination))


dest = input()
black_pearl = Ship("Black Pearl", 800)

black_pearl.sail(dest

3. Erstellen von Attributen mit Methoden
---------------------------------------------------------------------------
- alle möglichen Attribute sollten in __init__ definiert werden
- wenn man den Wert eines Attributes in einer Methode definieren will
  listet man ihn mit 'None' auf :
        
        class Ship:
            def __init__(self, name, capacity):
                self.name = name
                self.capacity = capacity
                self.cargo = 0
                self.captain = None
                
4. Modifizierung von Attributen mit Methoden
------------------------------------------------------------------------------
- Methoden können verwendet werden um Instance Attribute zu modifizieren.
- Als Beispiel dienen die Methoden 'load_cargo' und 'unload_cargo':
  Beide Methoden sollen den Wert des Attributs cargo ändern, wenn diese
  Änderungen möglich sind. Bei der load_cargo-Methode wird zunächst geprüft, 
  ob die Beladung mit einem bestimmten Gewicht die Kapazität des Schiffes nicht
  überschreitet, und bei der unload_cargo-Methode wird geprüft, ob beim Entladen
  das Gewicht der Ladung nicht negativ wird. Dann nehmen beide die Änderungen 
  vor oder drucken eine Meldung aus, dass diese Änderungen unmöglich sind. 
    class Ship:
        def __init__(self, name, capacity):
            self.name = name
            self.capacity = capacity
            self.cargo = 0
     
        def load_cargo(self, weight):
            if self.cargo + weight <= self.capacity:
                self.cargo += weight
                print("Loaded {} tons".format(weight))
            else:
                print("Cannot load that much")
     
        def unload_cargo(self, weight):
            if self.cargo - weight >= 0:
                self.cargo -= weight
                print("Unloaded {} tons".format(weight))
            else:
                print("Cannot unload that much")
   
    # Beispiel
        black_pearl.load_cargo(600)
        # "Loaded 600 tons"
         
        black_pearl.unload_cargo(400)
        # "Unloaded 400 tons"
         
        black_pearl.load_cargo(700)
        # "Cannot load that much"
         
        black_pearl.unload_cargo(300)
        # "Cannot unload that much"
        
5. Verwendung von 'return'
--------------------------------------------------------------------------
- Bisher haben unsere Methoden nichts zurück gegeben, da wir die 'print'
  Funktion benutzt haben.
- Wenn wir aber die Werte unserer Methoden weiter verwenden wollen, nutzen
  wir 'return'
- wenn wir die folgende methode 'free_space' benutzen passiert gar nichts,
  weil wir das Ergebnis nur 'returnen' aber nicht ausdrucken. 
    class Ship:
    # all other methods
        def free_space(self):
            return self.capacity - self.cargo
- das 'return' bewirkt aber, das man mit dem Ergebniss von 'free_space'
  weiter arbeiten kann. Siehe hierzu das folgende Beispiel:
    class Ship:
        # updated load_cargo method
        def load_cargo(self, weight):
            if weight <= self.free_space():
                self.cargo += weight
                print("Loaded {} tons".format(weight))
            else:
                print("Cannot load that much")
- In diesem Beispiel haben wir eine Methode innerhalb einer anderen Methode 
  aufgerufen und die Werte in unseren Berechnungen verwendet. Wiederum verwendeten 
  wir self, um sicherzustellen, dass wir uns nur mit der bestimmten Instanz der 
  Klasse Schiff befassen und dass alle Berechnungen sich auf diese Instanz beziehen.