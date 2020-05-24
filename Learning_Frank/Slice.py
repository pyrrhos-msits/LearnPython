


# Drucke alle ungeraden Zahlen einer Liste aus
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ungerade = nums[1::2]
print(ungerade)
ungerade = nums[::-2]
print(ungerade)

# Create a list of numbers divisible by 5 from the list numbersbelow and print it.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

num_5 = numbers[0::5]
print(num_5)
print(numbers[0::5])

'''The string below has an encoded message. Find out what it is by 
taking every 5th letter and then reversing the sequence. Spaces are considered as symbols here.'''
string = "no clouds here to spy on pets"
neu_str = string[::5]
print(neu_str[::-1]) # Trick um String reverse auszuführen

'''To find out if a word is a palindrome we would need to check if it reads the same forward and backward.
The condition for that check has already been written in the code below, but the parts that need to be 
compared are there. Finish the code by defining variables forward and backward.
The variable that stores the word in question is called word.'''
# please work with the preset variable `word`
forward = 'laptop'
backward =  forward[::-1]
if forward == backward:
    print("Yes")
else:
    print("No")