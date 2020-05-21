# read sums.txt
file = open('sums.txt','r')
lines = file.readlines()
for el in lines:
    a, b = el.split()
    print(int(a) + int(b))
file.close()