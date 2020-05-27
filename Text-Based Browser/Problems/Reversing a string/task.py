from collections import deque
n = int(input())
count = 0
my_stack = deque()
while count < n:
    el = input()
    my_stack.append(el)
    count += 1
count = 0
while count < len(my_stack):
    print(my_stack.pop())
