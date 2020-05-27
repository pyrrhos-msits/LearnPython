import string
names = ['Alice', 'bob', 'John']
def startswith_capital_counter(names):
    count = 0
    alph = string.ascii_uppercase
    for name in names:
        if name[0] in alph:
            count += 1
    return count

startswith_capital_counter(names)

