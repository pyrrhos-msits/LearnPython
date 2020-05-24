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

# Man kann die werte auch in() mitgeben:
https://hyperskill.org/learn/daily/8441
column = int(input())
row = int(input())
def king(spalte, reihe):
    if spalte in(8, 1):
        if reihe in(8, 1):
            print('3')
        else:
            print('5')
    elif reihe in(8, 1):
        if spalte in(8, 1):
            print('3')
        else:
            print('5')
    else:
        print('8')

king(column, row)