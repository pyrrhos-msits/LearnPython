lambda ist eine anonyme Funktion - weil sie keinen Namenn hat

def doubler(x):
    return 2 * x

ist das selbe wie:

lambda x: 2 * x

1. Syntax:
---------------------------------------------------------------------
    lambda arguments: expression

Lambda Funktion kann eine beliebige Anzahl von Argumenten annehmen 
muss aber aus nur einer expression bestehen
    lambda x, y: (x + y) % 2

lambda Funktionen benötigen keine return Anweisung

Für Lambda Bedingungen verwenden wir den ternary Operator:
    first_alternative if condition else second_alternative
    #Beispiel
    lambda x: 'even' if x % 2 == 0 else 'odd'

2. Aufruf
---------------------------------------------------------------------

Wenn man die Argumente in Klammern setzt kann man die Argumente sofort
übergeben.

    (lambda x, y: (x + y) % 2)(1, 5) # x = 1, y = 5
    # Output ist 0

Mann kann auch einer Variablen ein Funktionsobjekt zuweisen.
Dies entspricht aber nicht den Stilrichtlinien
    # Falsches Beispiel
    func = lambda x, y: (x + y) % 2
    func(1, 10)
    # The output is 1

3. Sinn 
----------------------------------------------------------------------
Lambda Funktionen sind praktisch wenn man sie in Kombination mit anderen Funktionen
verwendet. 
Im folgenden Beispiel verwendet 'create_function' ein Argument 'n' und gibt eine Funktion
zurück, die eine bestimmte Zahl 'x' mit dieser Zahl 'n' multipliziert.
    1. Schritt:
        definieren der variable doubler bestehend aus der function und dem Argument not
    2. Schritt:
        aufruf der Variable doubler und übergabe des Arguments x

    def create_function(n):
        return lambda x: n * x

    doubler = create_function(2)
    print(doubler(2))

    tripler = create_function(2)
    print(tripler(3))


4. Beispiele:
-------------------------------------------------------------------------------
#1. Turn into a lambda function 
def func(x):
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'

func = lambda x: 'even' if x % 2 == 0 else 'odd'


