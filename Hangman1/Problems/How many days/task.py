#  Posted from EduTools plugin
import math
seconds = [86400, 3600, 1028397, 8372891, 219983, 865779330, 3276993204380912]
days = []

for second in seconds:
    days.append(math.ceil(second // 86400))

print(days)