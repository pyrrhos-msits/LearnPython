def range_sum(numbers, a, b):
    summe = 0
    for el in numbers:
        if int(el) >= int(a):
            if int(el) <= int(b):
                summe += int(el)
    return summe



numbers =  input().split()
a, b =  input().split()
print(range_sum(numbers, a, b))

