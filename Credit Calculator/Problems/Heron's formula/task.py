import math
def heron(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(s)

heron(int(input()), int(input()), int(input()))
