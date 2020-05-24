# read animals.txt
# and write animals_new.txt

animal = open('animals.txt', 'r')
lst_animal = []
for el in animal:
    lst_animal.append(el.rstrip())
animal.close()
new_animal = open('animals_new.txt', 'w', encoding='utf-8')
new_animal.write(' '.join(lst_animal))
new_animal.close()