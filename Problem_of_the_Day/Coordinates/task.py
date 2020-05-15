x = float(input())
y = float(input())

def calc_quadrant(a, b):
    if a < 0:
        if b < 0:
            print('III')
        else:
            print('II')
    elif a > 0:
        if b < 0:
            print('IV')
        else:
            print('I')

calc_quadrant(x, y)