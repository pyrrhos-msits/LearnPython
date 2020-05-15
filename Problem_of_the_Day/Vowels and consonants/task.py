chars = input()

vowels = 'aeiou'

for char in chars:
    if char.isalpha():
        if char in vowels:
            print('vowel')
        else:
            print('consonant')
    else:
        break