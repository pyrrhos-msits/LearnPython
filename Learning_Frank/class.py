'''https://hyperskill.org/learn/step/6661
1. class definieren
2. erzeugen einer Instanz
3. __init__
4. self
5. Aufrufmöglichkeiten einer Methode
6. Instanz Attribute
7. Attribute ändern
8. Hinzufügen von Attributen
    8.1 Neues class Attribute anlegen
    8.2 Neues Instanzattribute anlegen
9. Beispiele aus JetBrain
1. class definieren
-----------------------------------------------------------------------------------------'''
# class name startet mit einem Grossbuchstaben und wird in 
# CamelCase geschrieben. Keine Unterstriche
'''classen enthalten die definitionen für Daten und Verhalten.
Das Verhalten wird über die Methoden gesteuert'''
class MyClass:
    var = ... #some Variable
    
    def do_smt(self):
    # some Method
'''
- Daten werden in attributen (variablen) gespeichert
- es gibt class attributes und instance Attributes
2. Erzeugen einer Instanz
----------------------------------------------------------------------------------------'''
# Book class
class Book:
    material = "paper"
    cover = "paperback"
    all_books = []
# Zugriff auf die class Attributes über dot.notation
Book.material  # "paper"
Book.cover  # "paperback"
Book.all_books  # []
#Class attributes werden innerhalb der class aber außerhalb der methoden definiert.
# es sind sozusagen die default werte für alle Objekte
# instanzatrribute werden innerhalb der Methoden definiert. Insbesondere über __init__
''' Erzeugen einer Instanz der class Book'''
# Book instance
my_book = Book()
# Hier erzeugen wir nicht nur eine Instanz von Book, sondern wir weisen diese Instanz
# auch gleich der Variablen my_Book zu
# Unser my_Book Object hat zugang zum Inhalt der class Book
print(my_book.material)  # "paper"
print(my_book.cover)  # "paperback"
print(my_book.all_books)  # []

'''ENDE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''
'''
3. __init__
-----------------------------------------------------------------------------------------
zum Anpassen des initial Statusses einer Instanz
- die __init__ methode ist ein constructor
- eine class kann nur einen constructor haben
- wenn __init__ innerhalb einer class definiert ist, 
  wird es automatisch aufgerufen, wenn wir eine neue class instance erzeugen
- __init__ legt explizit fest, welche Attribute die Instanz einer class
  von Anfang an haben muss. Hat sie es nicht -> Error'''

class River:
    # list of all rivers
    all_rivers = []
    
    def __init__(self, name, length):
        self.name = name
        self.length = length
        # add current river to the list of all rivers
        River.all_rivers.append(self)
 
volga = River("Volga", 3530)
seine = River("Seine", 776)
nile = River("Nile", 6852)
 
# print all river names
for river in River.all_rivers:
    print(river.name)
# Output:
# Volga
# Seine
# Nile
'''
4. self
-----------------------------------------------------------------------------------------
- ist ein Argument der __init__ Methode
- repräsentiert eine bestimmte instance der class und erlaubt den Zugang
  zu deren Attributen und Methoden.
- es ist wichtig den self Parameter zu nutzen, wenn man die Werte der Instanz
  für die spätere Nutzung speichern will
- meistens muss self auch in andere Methoden geschrieben werden, denn wenn
  die Methode aufgerufen wird, ist das erste Argument was übergeben wird, 
  das Objekt selbst.'''
  # Definition der class
 class River:
    all_rivers = []
 
    def __init__(self, name, length):
        self.name = name
        self.length = length
        River.all_rivers.append(self)
 
    def get_info(self):
        print("The length of the {0} is {1} km".format(self.name, self.length))
  # Aufruf der methode get_info       
volga.get_info()
# The length of the Volga is 3530 km
seine.get_info()
# The length of the Seine is 776 km
nile.get_info()
# The length of the Nile is 6852 km

5. Aufrufmöglichkeit einer Methode
- Zwei Möglichkeiten eine Methode aufzurufen
    erstens: self.method()
    zweitens: class.method(self)

# self.method()
volga.get_info()
# The length of the Volga is 3530 km
 
# class.method(self)
River.get_info(volga)
# The length of the Volga is 3530 km
'''
6. Instanz Attribute
-----------------------------------------------------------------------------------------
- class in Python hat zwei Attribute typen:
    - class Attributes
    - instance Attributes werden innerhalb von Methoden definiert und speichern
      instanzspezifische Informationen
    - in der class River sind die attribute name und length instance Attribute
      weil sie innerhalb der __init__ methode definiert wurden und self davor
      haben. 
    - üblicherweise werden instance Attribute innerhalb der __init__ methode
      definiert, weil diese der constructor ist. Aber man kann instance 
      Attribute auch in anderen Methoden definieren.
    - Instanzattribute sind nur aus dem Scope des Objektes verfübgar. Deshalb wirft
      der folgende Code auch einen Fehler:
        print(River.name)  # AttributeError
    - Instanze Attribute werden genutzt um Objekte voneinander zu unterscheiden.
      Ihre werte sind für jede Instanz verschieden.
        volga.name  # "Volga"
        seine.name  # "Seine"
        nile.name   # "Nile"
 Wenn Sie also entscheiden, welche Attribute in Ihrem Programm gewählt werden sollen, 
 sollten Sie zunächst entscheiden, ob es Werte speichern soll, die für jedes Objekt 
 der Klasse eindeutig sind, oder im Gegenteil, die von allen Instanzen gemeinsam 
 genutzt werden.'''
''' 
 7. Attribute ändern
 ----------------------------------------------------------------------------------------
 - Erläuterungen an folgendem Beispiel:'''
 '''Wir haben eine Klasse Pet:'''
 class Pet:
    kind = "mammal"
    n_pets = 0  # number of pets
    pet_names = []  # list of names of all pets
 
    def __init__(self, spec, name):
        self.spec = spec
        self.name = name
        self.legs = 4
''' Hierfür erzeugen wir 3 instanzen:'''
tom = Pet("cat", "Tom")
avocado = Pet("dog", "Avocado")
ben = Pet("goldfish", "Benjamin")
''' Jetzt wollen wir das class Attribut n_pets ändern:'''
n_pets ist ein Integer. Also ein unveränderlicher(Immutable) Datentyp
Um diesen immutablen Datentyp zu ändern müssen wir das class Attribute
ansprechen:
# Änderung des class Attributes in der Klasse ändert auch die Instanz Attribute
Pet.n_pets += 3
# Result :
Pet.n_pets      # 3
tom.n_pets      # 3
avocado.n_pets  # 3
ben.n_pets      # 3
# Änderung eines class Attributes in der Instanz ändert nur das jeweilige 
# Instanzattribute
tom.n_pets += 1
avocado.n_pets += 1
ben.n_pets += 1
 
Pet.n_pets      # 0
tom.n_pets      # 1
avocado.n_pets  # 1
ben.n_pets      # 1
# das selbe gilt für das class Attribut 'kind':
Dieses ist ein String. Auch dieser ist unveränderlich. Deshalb ändert 
sich auch immer nur der Wert für die entsprechende Instanz:
ben.kind = "fish"
 
Pet.kind      # "mammal"
tom.kind      # "mammal"
avocado.kind  # "mammal"
ben.kind      # "fish"
''' Anders verhält es sich bei mutablen (veränderlichen) Datentypen'''
#Eine Änderung hier führt zu einer Änderung für alle Instanzen:
tom.pet_names.append(tom.name)
avocado.pet_names.append(avocado.name)
ben.pet_names.append(ben.name)
 
Pet.pet_names      # ["Tom", "Avocado", "Benjamin"]
tom.pet_names      # ["Tom", "Avocado", "Benjamin"]
avocado.pet_names  # ["Tom", "Avocado", "Benjamin"]
ben.pet_names      # ["Tom", "Avocado", "Benjamin"]
#Wenn man nur einen Wert ändern will, geht das auch.
# Das wiederspricht aber der convention, das class Attribute
# für alle Instanzen gleich sind
tom.pet_names = ["Tom"]
avocado.pet_names = ["Avocado"]
ben.pet_names = ["Benjamin"]
 
Pet.pet_names      # []
tom.pet_names      # ["Tom"]
avocado.pet_names  # ["Avocado"]
ben.pet_names      # ["Benjamin"]

8. Hinzufügen von Attributen
-----------------------------------------------------------------------------------------
Wir könne auch Attribute zur Klasse oder zu einer einzelnen Instanz hinzufügen
8.1 Neues class Attribute anlegen
Wenn wir zum Beispiel die Information sehen wollen, welche spezies alle Tiere
unserer Instanzen haben, können wir es von Anfang an als class Attribute anlegen 
oder wir erstellen eine Variable wie diese:

Pet.all_specs = [tom.spec, avocado.spec, ben.spec]
 
tom.all_specs      # ["cat", "dog", "goldfish"]
avocado.all_specs  # ["cat", "dog", "goldfish"]
ben.all_specs      # ["cat", "dog", "goldfish"]

8.2 Neues Instanzattribute anlegen
Wenn wir zum Beispiel ein neues Attribut 'Rasse' für die 'spec' dog
anlegen wollen, weil dies nur für die 'spec' Hund erforderlich ist, 
können wir dies für die einzelne Instanz tuen:
avocado.breed = "corgi"
Hier erzeugen wir das Attribut 'breed' für das Object 'avocado'. Alle
anderen Instanzen, wie auch die Klasse selber haben dieses Attribut nicht.
Der folgende Code erzeugt also Fehler:
Pet.breed  # AttributeError
tom.breed  # AttributeError
ben.breed  # AttributeError


# Beispiele aus JetBrain
- C:\Users\pyrrh\PycharmProjects\Credit Calculator\Problems\The Louvre\task.py






















