eingabe = input().split()
target = int(input())
numbers = []

for ele in eingabe:
    numbers.append(int(ele))

def count(a, b):
    cnt = 0
    for i, el in enumerate(a):
        if el == b:
            cnt += 1
    print(cnt)

count(numbers, target)
