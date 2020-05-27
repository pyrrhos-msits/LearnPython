from collections import deque

inp = input()
my_list = deque()
for el in inp:
    if el == '(' or el == ')':
        my_list.append(el)
c1 = 0
c2 = 0
if my_list[0] == ')':
    print('ERROR')
elif my_list[0] == '(':
     for el in my_list:
         if el == '(':
             c1 += 1
         else:
             c2 += 1
     if c1 == c2:
         print('OK')
     else:
         print('ERROR')



