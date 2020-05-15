income = int(input())

tax = 0

if input <= 15527:
    tax = 0
elif input <= 42707:
    tax = 15
elif input <= 85414:
    tax = 22
elif input <= 13406:
    tax = 26
else:
    tax = 28

print(tax)