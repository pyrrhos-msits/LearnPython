summe = 0
count = 0
x = input()
while x != '.':
    summe += int(x)
    count += 1
    x = input()
print(summe / count)
