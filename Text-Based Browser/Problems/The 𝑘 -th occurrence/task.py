numbers = input().split()
target = input()
k = int(input())

def kth(number, targe, s):
    cnt = 0
    for indx, el in enumerate(number):
        if el == targe:
            cnt += 1
            if cnt == s:
                print(indx)
                break
    if cnt < k:
        print(-1)

kth(numbers, target, k)
