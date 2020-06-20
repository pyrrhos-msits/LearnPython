y = []
while True:
    x = input()
    if x != '.':
        y.append(float(x))
    if x == '.':
        print(min(y))
        break


