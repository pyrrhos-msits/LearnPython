num = int(input())


count = 0
if num <= 1:
    print('This number is not prime')
for i in range(2, num):
    if num % i == 0:
        print('This number is not prime')
        count += 1
        break
if count == 0 and num > 1:
    print('This number is prime')
