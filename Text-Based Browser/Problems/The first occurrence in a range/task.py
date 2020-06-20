numbers = input().split()
target = input()
c, d, = input().split()
a = int(c)
b = int(d)

def search(numbers, target, a, b):
    lst = numbers[a:b]
    cnt = 0
    for indx, el in enumerate(lst, a):
        if el == target:
            print(indx)
            cnt += 1
            break
    if cnt == 0:
        print(-1)

search(numbers, target, a, b)
