cafe = input().split()

largest = cafe[0]

while cafe != 'MEOW':
    if cafe[1] > largest[1]:
        largest = cafe[0]
        largest[1] = cafe[1]
    #cafe = input().split()
print(largest)