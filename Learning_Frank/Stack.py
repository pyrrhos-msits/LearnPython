
1. Listen als Stack
----------------------------------------------------------------------
Keine gute Idee, da sehr langsam und bei größeren Datenmengen 
inkonsistent

my_stack = []
y_stack.append('Out')
my_stack.append('First')
my_stack.append('In')
my_stack.append('Last')
print(my_stack) # ['Out', 'First', 'In', 'Last']

'''pop() nimmt immer das letzte Teil vom Stapel'''
print(my_stack.pop()) # Last
print(my_stack.pop()) # In
print(my_stack.pop()) # First
print(my_stack.pop()) # Out

2. Richtig mit deque aus dem collections Modul
-----------------------------------------------------------------------
from collections import deque
 
'''Definition des Stack'''
my_stack = deque()

'''Elemente hinzufügen'''
- Entweder mit append()
 - Oder mit appendleft()

my_stack.append('k')
my_stack.append('c')
my_stack.append('a')
my_stack.append('t')
my_stack.append('s')

'''Elemente entfernen'''
- Entweder mit pop()
- oder mit popleft()

print(my_stack.pop()) # 's'
print(my_stack.pop()) # 't'
print(my_stack.pop()) # 'a'
print(my_stack.pop()) # 'c'
print(my_stack.pop()) # 'k'

''' Errormessage wenn Stack leer'''
my_stack.pop() # IndexError: pop from an empty deque

'''Errormessage vermeiden mit len()'''
len(my_stack) #0

my_stack.append('a')
len(my_stack) # 1
