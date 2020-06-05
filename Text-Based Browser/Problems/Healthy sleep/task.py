a = int(input())
b = int(input())
h = int(input())

# if h <= b and h >= a:
#     print('Normal')
# elif h > b:
#     print('Excess')
# else:
#     print('Deficiency')


if a <= h <= b:
    print('Normal')
elif h > b:
    print('Excess')
else:
    print('Deficiency')