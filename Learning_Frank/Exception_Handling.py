# Lehrmaterial auf JetBrain Academy
    https://hyperskill.org/learn/step/6270
# Dokumentation der Exceptions in Python:
    https://docs.python.org/3/library/exceptions.html#bottom
# Hierarchie der Exeptions
    https://docs.python.org/3/library/exceptions.html#exception-hierarchy
    
1. try-except statement
2. Exception handling keywords
3. Behandlung mehrerer Ausnahmen
4. Globale Fehlerbehandlung (Alle Built In Exceptions abfangen)
    
1. try-except statement
Wenn z.B eine Division durch null erfolgen soll, kommt der 
'ZeroDivisionError'. Um dies zu verhindern, fügen wir an der Stelle
wo der Fehler auftreten könnte, den 'try-except' Block ein:
#Beispiel:
    #In dieser Konstellation crasht das Programm:
    >>> Please, enter the first number: 5
    >>> Please, enter the second number: 0
    Traceback (most recent call last):
    File "<input>", line 1, in <module>
    File "C:/Users/User/.PyCharm2018.2/config/scratches/scratch_9.py", line 4, in <module>
        print("The result of your division is: ", a/b)
    ZeroDivisionError: division by zero

    # Das selbe Beispiel mit 'try-except'. Hier crasht nichts
    while True:
       number_one = int(input("Please, enter the first number: "))
       number_two = int(input("Please, enter the second number: "))
       try:
           result = number_one / number_two
       except ZeroDivisionError:
           print("We achieve it thanks to except ***You can not divide by zero!!")
       else:
           print("The result of your division is: ", result)
       finally:
           print("It is done through finally ***Thanks for using our calculator! Come again!")
           
    # Hier die Ausführung dazu:
    >>> Please, enter the first number: >? 5
    >>> Please, enter the second number: >? 0
    >>> We achieve it thanks to except ***You can not divide by zero!!
    >>> It is done through finally ***Thanks for using our calculator! Come again!
    
2. Exception handling keywords
- try
- except
- else
- finally

- Zuerst durchläuft Python den 'try' Block.
- Wenn dort kein Fehler auftritt, ist alles gut. Der Block wird ausgeführt
    und beendet
- Wenn ein Fehler auftritt, wird der Rest des 'try' Blocks übersprungen und
    Python prüft ob der exception type mit der Exception übereinstimmt, die 
    nach dem except keyword definiert wurde. Es durchläuft den except Block
    und fährt mit der Programmausführung nach dem except Block fort.
- Wenn die Exception nicht mit der in der except clausel festgelegten übereinstimmt,
    handelt es sich um eine 'unhandled exception' und das Programm stoppt mit einem
    'Traceback Error'
- Der else Block wird nr ausgeführt, wenn keine exception auftritt
- Es KANN eine finally Klausel angegeben sein. Wenn diese angegeben ist, so wird sie
    vor dem verlassen des try except Blocks ausgeführt. unabhängig ob eine Exception
    aufgetreten ist oder nicht.

3. Behandlung mehrerer Ausnahmen
- Um alle Exceptions in der Python Dokumentation abzufangen, könnte man z.B die 
    folgenden except Klausel einfügen:
        except:
        print("An error occurred! Try again.")
    Dieses würde jeden Fehler mit der Message abfangen. Allerdings sagt die Meldung
    nichts aus und gilt ausserdem als schlechter Programmierstil
- wenn man also mehrere Exceptions abfangen will, so kann man mehrere except Blöcke
    hintereinander aufführen:
        except ZeroDivisionError:
        print("We achieve it thanks to except ***You can't divide by zero!!")
        except ValueError:
        print("You can only enter numbers consisting of digits, not text!!")
- ebenfalls ist es möglich in Klammern mehrere mögliche Exceptions aufzuführen und 
    so eine Fehlermeldung für mehrere Exceptions auszugeben:
        except (ValueError, TypeError):
        print("You can only enter numbers consisting of digits, not text!!")
- Auch möglich z.B. alle 'ArithmeticError' (Link in Zeile 4) mit einer except
    Klausel abzufangen:
        except ArithmeticError:
        print("I will also catch FloatingPointError, OverflowError, and ZeroDivisionError")
        
4. Globale Fehlerbehandlung (Alle Built In Exceptions abfangen)
- Wenn man gar keine Vorstellung hat, welche Fehler auftreten könnten, kann man folgenden
    Klausel verwenden:
        except Exception:
        # do something
    Mit dieser Klausel fängt man alle Built In Exceptions ab. Mit Ausnahme von:
        - 'GeneratorExit'
        - 'KeyboardInterrupt'
        - 'SystemExit'
    Bei Nutzung dieser Klausel ist es also immer noch möglich das System mit dem KeyboardInterrupt
    oder über SysteExit Befehle zu beenden.

        
    
























