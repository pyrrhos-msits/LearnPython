#  Posted from EduTools plugin
# a = '5 8 2 7 8 8 2 4'
c = input().split()
#c = a.split()
b= input()
d = []


for el in range(len(c)):
    if c[el] == b:
        d.append(str(el))

if len(d) > 0:
    print(' '.join(d))
else:
    print('not found')


