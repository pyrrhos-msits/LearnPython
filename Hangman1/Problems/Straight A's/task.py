#  Posted from EduTools plugin
a = input()
a_list = []
for el in a:
    b = ['A', 'B', 'C', 'D', 'F']
    if el in b:
        a_list.append(el)
a_countA = 0
a_len = len(a_list)
for el in a:
    if el == 'A':
        a_countA += 1
x =  (a_countA / a_len)
y = round(x , 2)
print(y)
