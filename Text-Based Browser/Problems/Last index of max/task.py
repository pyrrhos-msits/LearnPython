numbers = [8, 11, 15, 15, 15, 12]
def last_indexof_max(numbers):
    index = 0
    for i in range(0, len(numbers)):
        if numbers[i] >= numbers[index]:
            index = i
    return index

last_indexof_max(numbers)