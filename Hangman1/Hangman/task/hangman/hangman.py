import random
import string
print("H A N G M A N")
print()
words = ['python', 'java', 'kotlin', 'javascript']
word = (random.choice(words))
wordlen = len(word)
tries = 8
wordstrich = []
y = type(wordstrich)
lowerchar = string.ascii_lowercase

for x in word:
    wordstrich.append('-')
goodLetters = []
enteredLetters = []

while tries > 0:
    print(''.join(wordstrich))
    char = input("Input a letter:")
    if len(char) > 1 or char == ' ':
        print('You should print a single letter')
        print()
        continue
    if char not in lowerchar:
        print('It is not an ASCII lowercase letter')
    else:
        if char in enteredLetters:
            print('You already typed this letter')
        else:
            if char not in word:
                print('No such letter in the word')
                tries -= 1
        if char not in enteredLetters:
            enteredLetters.append(char)

    for i in range(len(word)):
        if word[i] == char:
            x = i
            goodLetters.append(char)
            wordstrich.pop(x)
            wordstrich.insert(x, char)

    if '-' not in wordstrich:
        print("{} {}{}\n{}".format('You guessed the word',word,'!','You survived!'))
        break
    else:
        if tries > 0:
            print()
else:
    print('You are hanged!')


