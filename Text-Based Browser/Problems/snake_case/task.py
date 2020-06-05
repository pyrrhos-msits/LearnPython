satz = input()
snake = ''

for el in satz:
    if el.islower():
        snake += el
    elif el.isupper():
        snake += '_' + el.lower()
print(snake)
