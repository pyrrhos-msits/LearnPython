'''In erster Linie kann man mit den folgendne Methoden Strings in Listen umwandeln
oder aber Listen in Strings'''

'''String und Joinmethoden verändern die ursprüngliche Zeichenfolge nicht.
Wenn Sie die "geänderte" Zeichenfolge mehrmals verwenden müssen, müssen Sie das Ergebnis der jeweiligen Methode einer Variablen zuweisen.
Wenn Sie dieses Ergebnis nur einmal verwenden müssen, können Sie an Ort und Stelle damit arbeiten, z.B. es drucken().
Es gibt eine Menge Parameter in String-Methoden. Sie können in der Dokumentation nachsehen, wenn Sie eine Feinabstimmung Ihres Programms benötigen.'''

''''<<<<<<<<<<<<<<<< Split >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''

x = 'Coin of the realm is the legal money of the country'
#Split ohne Angabe von Argumenten
a = x.split() #['Coin', 'of', 'the', 'realm', 'is', 'the', 'legal', 'money', 'of', 'the', 'country']
print(a)

# split bei einem bestimmtem Wert
b = x.split('of')#['Coin ', ' the realm is the legal money ', ' the country']
print(b)

#zweites Argument 'maxsplit' sagt wie oft der split durchgeführt werden soll
c = x.split('of', 1)
print(c)#['Coin ', ' the realm is the legal money of the country']

# mit split Werte bestimmten Variablen zuweisen
name, surname = input().split()  # Forrest Gump
print(name)  # Forrest
print(surname)  # Gump

'''<<<<<<<<< Split multiple lines >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''
# arbeitet wie split() aber trennt an den Liniengrenzen (hier \n)

# splitlines example
long_text = 'first line\nsecond line\rthird line\r\nforth line'
long_text.splitlines()
# ['first line', 'second line', 'third line', 'forth line']

# splitline() hat eine Methode 'keepends'. Diese hat 2 werte 'True' oder 'False'
# Wenn keepends = True werden die Linebreaks mit angezeigt.
# keepends
long_text = 'first line\nsecond line\rthird line\r\nforth line'
 
long_text.splitlines(keepends=True)
# ['first line\n', 'second line\r', 'third line\r\n', 'forth line']

# mehrere Methoden aneinander reihen mittels 'chaining'

# chaining example
sent = input()  # "Mary had a little lamb"
new_sent = sent.lower().split()
# ["mary", "had", "a", "little", "lamb"]

'''<<<<<<<<<<<<<<<<<<<<<<<<<<<< Join a list >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''

# Achtung join funktioniert nur mit Strings. 
word_list  = ["dog", "cat", "rabbit", "parrot"]
 
" ".join(word_list)  # "dog cat rabbit parrot"
"".join(word_list)  # "dogcatrabbitparrot"
"_".join(word_list)  # "dog_cat_rabbit_parrot"
" and ".join(word_list)  # "dog and cat and rabbit and parrot"

# Bei Integers wird ein Fehler geworfen
int_list = [1, 2, 3]
" ".join(int_list)  # TypeError!

# bei einer Liste von Strings funktioniet es
str_list = ["1", "2", "3"]
" ".join(str_list)  # "1 2 3"