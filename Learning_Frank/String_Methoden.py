# Strings sind unveränderlich. Das bedeutet, das die meisten Zeichenkettenmethoden
# eine Kopie der Zeichenkette zurück geben => Um Änderungen für die spätere Verwendung zu
# speichern, müssen diese Änderungen in einer Variablen gespeichert werden.
# Übersicht über string methoden
https://www.w3schools.com/python/python_ref_string.asp

1. Wichtige String Methoden
2. Hinzufügen oder Entfernen von Teilen des Strings
3. Membership testing (in / not in)
4. Elemente am Anfang oder Ende eines Strings suchen
5. Position des Elements im String finden (find() , index() 
6. Suchen nach Substrings in einem String
7. Rückwärtssuche (rfind(), rindex())
8. Zählen wie oft ein element oder Substring in einem String vorkommt(count())

1. Wichtige string methoden
-------------------------------------------------------------------------------


- str.capitalize() 
    #changes the first character of the string to the upper case and the rest to the lower case.

- str.islower()
    #Gibt 'True' oder 'False' zurück wenn alle Zeichen im String klein geschrieben sind

- str.isupper()
    #Gibt 'True' oder 'False' zurück wenn alle Zeichen im String gross geschrieben sind


- str.lower() 
	#converts all characters of the string to the lower case.

- str.replace(old, new[, count]) 
	#replaces all occurrences of old with the new. The count argument is optional, and if it is specified, only the first count occurrences are replaced.

- str.swapcase() 
    #converts upper case to lower case and vice versa.

- str.title() 
    #converts the first character of each word to upper case.

- str.upper() 
    #converts all characters of the string to the upper case.
	
# Beispiele
print(message.upper())  # BONJOUR AND WELCOME TO PARIS!
# the message is not changed
print(message)  # bonjour and welcome to Paris!
 
title_message = message.title() 
# title_message contains a new string with all words capitalized
print(title_message)  # Bonjour And Welcome To Paris!
 
 
replaced_message = message.replace("o", "!")
# again, the "source" string is unchanged, only its copy is modified
print(replaced_message)  # b!nj!ur and welc!me t! Paris!
 
# the string is the same as it was
print(message)  # bonjour and welcome to Paris!

2. Hinzufügen oder Entfernen von Teilen des Strings
-------------------------------------------------------------------------------

# chars meint die Zeichenfolge die hinzugefügt oder entfernt werden soll
- str.lstrip([chars]) 
	#removes the leading characters . If the argument chars isn’t specified, leading whitespaces are removed.
- str.rstrip([chars]) 
	#entfernt die Zeichen . The default for the argument chars is also whitespace.
- str.strip([chars]) 
	#entfernt beides the leading and the trailing characters. The default is whitespace.

# Beispiele
whitespace_string = "     hey      "
normal_string = "incomprehensibilities"
# delete spaces from the left side
whitespace_string.lstrip()  # "hey      "
# löscht "i" oder "s" oder "is" von der linken Seite
normal_string.lstrip("is")  # "ncomprehensibilities"
# delete spaces from the right side
whitespace_string.rstrip()  # "     hey"
# delete "i" or "s" or "is" from the right side
normal_string.rstrip("is")  # "incomprehensibilitie"
# no spaces from both sides
whitespace_string.strip()  # "hey"
# delete trailing "i" or "s" or "is" from both sides
normal_string.strip("is")  # "ncomprehensibilitie"

3. Membership testing (in / not in)
-------------------------------------------------------------------------------
    Prüft ob ein bestimmtes Muster in einer Zeichenkette vorkommt oder auch nicht
    vorkommt. Gibt 'True' oder 'False' zurück.
        print("apple" in "pineapple")  # True
        print("milk" in "yogurt")      # False
        
    Ein leerer String wird als Bestandteil jedes Strings betrachtet
        print('' in '')           # True
        print('' not in "lemon")  # False
     

4. Elemente am Anfang oder Ende eines Strings suchen
--------------------------------------------------------------------------------
    startswith() und endswith() suchen nach einem Muster am Anfang oder Ende eines Strings und geben dann true oder
	false zurück
    #Beispiele
    email = "email_address@something.com"
    email.startswith("www.")  # False
    email.endswith("@something.com")  # True

    Mehrere Argumente übergeben
    word.startswith(('a','A'))] # Hierbei wird das erste Argument (der Suchbuchstabe) in Klammern übergeben


    Mann kann optional noch start und end parameter verwenden. Dann wird festgelegt 
    wo die suche anfängt und wo sie aufhört
        syntax: str.startswith(pattern, start, end)
        # Hier wird der Start der Suche auf den Index 2 bzw. 3 festgelegt.
        email = "my_email@something.com"
        print(email.startswith("email", 2))  # False
        print(email.startswith("email", 3))  # True
        # Hier das Beispiel für 'endswith()
        email = "my_email@something.com"
        print(email.endswith("@", 5, 8))  # False
        print(email.endswith("@", 5, 9))  # True
        
5. Position des Elements im String finden (find() , index() )
-------------------------------------------------------------------------------

    Um die genaue Position eines Elements in einem String zu finden gibt es zwei
    Methoden find() und index()
    # finde den Index des Buchstaben 'i' im String
        best = 'friend'
        print(best.find("i"))   # 2
        print(best.index("i"))  # 2
    
    Zunächst funktionieren beide Methoden gleich. Der Unterschied liegt in der 
    Behandlung von Fehlern wenn das gesuchte Element nicht vorhanden ist:
    während find() -1 zurück gibt, erhält man bei index() einen ValueError
    # finde den Buchstaben 'u' in der Variable 'best'
        print(best.find("u"))   # -1
        print(best.index("u"))  # ValueError

6. Suchen nach Substrings in einem String
---------------------------------------------------------------------------------

    Man kann auch nach Substrings in einem String suchen. Hierbei gilt es aber 
    zu beachten, das nur das erste Aufkommen des Substrings im String zurückgegeben
    wird. Es wird auch nur der Index des ersten Buchstaben zurück gegeben
        best = "friend"
        print(best.find("end"))  # 3
        
        magic = "abracadabra"
        print(magic.find("ra"))  # 2
        
    Es ist auch möglich ein Intervall für die Suche zu definieren
        string.find(pattern, start, end)
        # auch hier gilt, der End index gehört nicht zur Suche
        magic = "abracadabra"
        print(magic.find("ra", 5))      # 9
        print(magic.find("ra", 5, 10))  # -1
        
7. Rückwärtssuche (rfind(), rindex())
    
    Man kann auch Rückwärts suchen
        magic = "abracadabra"
        print(magic.rfind("ra"))  # 9
        print(magic.rindex("a"))  # 10
       
8. Zählen wie oft ein element oder Substring in einem String vorkommt(count())

        magic = "abracadabra"
        print(magic.count("abra"))  # 2
        print(magic.count("a"))     # 5