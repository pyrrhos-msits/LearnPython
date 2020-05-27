import math

real_number = float(input())
# change the next line
check = None

if math.isinf(real_number) or math.isnan(real_number):
    check = False
else:
    check = True
