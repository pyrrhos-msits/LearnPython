<< Loop Schema >>
for variable in iterable:
    statement
	
<< Iteration über ein Tupel >>
oceans = ['Atlantic', 'Pacific', 'Indian', 'Southern', 'Arctic']
for ocean in oceans:
    print(ocean)
<< Einzelne Buchstaben aus einem String >>
for char in 'magic':
    print(char)
	
<< range() function anwenden >>
for i in range(5):
	print(i)
# 0 1 2 3 4 5

# Finden des Indexes eines Wertes in einer Liste
list = [2, 3, 5, 7, 9]
for index in range(len(list)):
    print('Der Index ist :', index, 'Der Wert lautet :' , list[index])

# Finden eines bestimmten Wertes in einer Liste:
list = [2, 3, 5, 7, 9]
search = 5
for index in range(len(list)):
    if list[index] == search:
        print('Der Index ist :', index, 'Der Wert lautet :' , list[index])


- 5 Startwer, 30 Endwert , 5, Increment
for i in range(5,30,5):
    print(i)
# 5, 10 15 20 25

<< nestet loop >>
names = ['Rose', 'Daniel']
surnames = ['Miller']
for name in names:
    for surname in surnames:
         print(name, surname)
# Rose Miller
# Daniel Miller
''' Selbes Problem unterschiedliche Lösungen '''
scores = input().split()
incorrect = 0
correct = 0
# lange Lösung
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
    
#kurze Lösung
scores = input().split()
for i in range(1, len(scores) + 1):
    if scores[:i].count('I') == 3:
        print('Game over')
        break
else:
    print('You won')
print(scores[:i].count('C'))
