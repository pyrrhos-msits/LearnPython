
units = int(input())

def classify_units(n):
    if n > 999:
        print('legion')
    elif n > 499:
        print('swarm')
    elif n > 49:
        print('horde')
    elif n > 9:
        print('pack')
    elif n > 0:
        print('few')
    else:
        print('no army')

classify_units(units)