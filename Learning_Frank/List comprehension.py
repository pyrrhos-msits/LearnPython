# einfache Art neue Listen zu generieren
# ersetzt eine for Schleife
list = [1, 2, 3]
new_list = [x for x in list]
print(new_list)
# the equivalent code
new_list = []
for x in list:
    new_list.append(x)
print(new_list)

# example squared numbers
new_list = [x * x for x in list]
print(new_list)

# from string to float
strings = ["8.9", "6.0", "8.1", "7.5"]
floats = [float(num) for num in strings]  # [8.9, 6.0, 8.1, 7.5]
print(floats)

# List comprehension with if =========================================
#  Syntax
# new_list = [x for x in some_iterable if condition]

# odd numbers
numbers = [4, 8, 15, 16, 23, 42, 108]
odd_list = [x for x in numbers if x % 2 == 1] # [15, 23]

# conditions with functions
text = ["function", "is", "a", "synonym", "of", "occupation"]
words_tion = [word for word in text if word.endswith("tion")]
# result: ["function", "occupation"]

# show all vowels in a given string
vowels = 'aeiou'
word = 'invertebrate'
vow_in_word = [x for x in word if x in vowels]
print(vow_in_word)

# even Numbers
my_numbers = [1,2,3,4,5]
even_list = [x for x in my_numbers if x % 2 == 0]
print(even_list)