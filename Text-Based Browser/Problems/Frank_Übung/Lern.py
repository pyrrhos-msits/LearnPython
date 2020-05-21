def fib(n):
    a, b = 0, 1
    print('Startwert a =', a)
    print('Startwert b =', b)
    for _ in range(n):
        print(a)
        a, b = b, a + b
        print('Folgewert a =', a)
        print('Folgewert b =', b)

fib(5)