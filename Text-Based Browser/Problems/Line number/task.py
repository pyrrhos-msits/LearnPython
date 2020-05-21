# read sample.txt and print the number of lines
file = open('sample.txt', 'r')
x = file.readlines()
print(len(x))
file.close()

