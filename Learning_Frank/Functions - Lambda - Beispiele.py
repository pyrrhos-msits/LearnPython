
print((lambda x: x * 2)(25))

def create_function(n):
    return lambda x: n * x

doubler = create_function(2)
print(doubler(2))

tripler = create_function(3)

print(tripler(3))



