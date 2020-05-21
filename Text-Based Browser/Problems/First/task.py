# read test_file.txt
file = open('test_file.txt', 'r', encoding='utf-16')
x = file.readlines()
print(x[0])
file.close()
