from collections import deque

numb = int(input())
count = 0
booklst = deque()
while count < numb:
    action = input()
    if action == 'READ':
        print(booklst.pop())
    else:
        action, book = action.split(' ', 1)
        booklst.append(book)
    count += 1
