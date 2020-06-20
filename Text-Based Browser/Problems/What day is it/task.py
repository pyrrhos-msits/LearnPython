x = float(input())
g = 'Monday'
t = 'Tuesday'
m = 'Wednesday'

def day(a):
    if -10.5 <= a < 0:
        print(t)
    elif a < -10.5:
        print(g)
    elif a > 13.5:
        print(m)
    else:
        print(t)

day(x)