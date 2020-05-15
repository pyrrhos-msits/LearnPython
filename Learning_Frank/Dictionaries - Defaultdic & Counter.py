
'''Methode dict.setdefault()'''
'''Ermöglicht es, alle Elemente in einem iterierbaren Objekt in ein Set zu schreiben 
    und die Anzahl jedes Elementes zu ermitteln.
    WICHTIG => Der 'default' value ist der Wert an dem angefangen wird zu zählen'''
# 1. Beispiel >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
text = ("Gambit is a chess opening in which a player risks one or more pawns "
        "or a minor piece to gain an advantage in position")

text_list = text.lower().split() # konvertiert den Text zu einer Liste aus Wörtern
print(text_list)
# create empty dictionary
freq_dict = {}
# loop through text and count words
for word in text_list:
    freq_dict.setdefault(word, 0) # set the default value to 0
    freq_dict[word] += 1 # increment the value by 1
# examples
print(freq_dict)
print(freq_dict["gambit"])  # 1
print(freq_dict["a"])  # 3
# Beispiel für einen String
string = 'Adelheid'
string_dict = {}
for el in string:
    string_dict.setdefault(el, 0)
    string_dict[el] += 1
print(string_dict)

#Nutzen von enumerate zur bestimmung des Indexes und hinzufügen von Index und element zu einem dictionary
index_dict = {} # key ist das element, value ist der Index
for index, word in enumerate(text_list):
    index_dict.setdefault(word, []).append(index)
# example
print(index_dict)
print(index_dict["or"])  # [11, 14]
# setdefault() ist auch nützlich, wenn wir einen key vermissen. Die folgende Zeile
# fügt den key 'are' mit value '0' zum freq_dict hinzu
print(freq_dict.setdefault("are", 0))  # 0
print(freq_dict)

