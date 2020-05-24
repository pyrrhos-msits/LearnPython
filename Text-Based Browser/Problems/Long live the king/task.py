column = int(input())
row = int(input())
def king(spalte, reihe):
    if spalte in(8, 1):
        if reihe in(8, 1):
            print('3')
        else:
            print('5')
    elif reihe in(8, 1):
        if spalte in(8, 1):
            print('3')
        else:
            print('5')
    else:
        print('8')

king(column, row)
