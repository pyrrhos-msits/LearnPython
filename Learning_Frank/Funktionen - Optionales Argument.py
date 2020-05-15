def heading(string, number=1):
    if number >= 6:
        number = 6
    elif number in range(1, 6):
        number = number
    else:
        number = 1
    print('#' * number, string)

heading('Positive Zahl', 6)
heading('Negative Zahl', -1)
heading('Null', 0)
heading('Optionales Feld ist leer')