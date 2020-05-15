scores = input().split()
incorrect = 0
correct = 0

for score in scores:
    if score == 'I':
        incorrect += 1
        if incorrect == 3:
            break
    if score == 'C':
        correct += 1

if incorrect < 3:
    print('You won\n{}'.format(correct))
else:
    print('Game over\n{}'.format(correct))