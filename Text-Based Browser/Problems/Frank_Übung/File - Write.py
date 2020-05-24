file = open('test_file.txt', 'a', encoding='utf-8')
file.write('This is a line in a testfile!')
file.close()

names = ['Frank', 'Sabine', 'Franzi']
name_file = open('Namenliste.txt', 'w', encoding= 'utf-8')
for name in names:
    name_file.write(name + '\n')
name_file.close()

file = open('Namenliste.txt', 'r')
print(file.readlines())
file.close()
