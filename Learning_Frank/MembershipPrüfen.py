- mit den Operatoren in und not in
- für alle Container (list, tuples, sets, dictionaries, strings, bytes)
- Rückgabewert ist true oder false
- Syntax ist für alles die selbe: value in container

print ('a' in 'apple') #True
print('b' not in 'apple') #True
print('apple' in 'applepie') #True
print('pear' not in 'applepie') #True
- In jedem String ist ein leerer Substring. Deshalb ist die folgende Zeile True
print('' in 'a') # true