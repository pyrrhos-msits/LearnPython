#  Posted from EduTools plugin
#text = input()
text = 'WWW.GOOGLE.COM uses 100-percent renewable energy sources and www.ecosia.com plants a tree for every 45 searches!'
#text = text.lower()
words = text.split()
for word in words:
    if word.startswith('www.') or word.startswith('WWW.')\
            or word.startswith('http://') or word.startswith('https://'):
        print(word)

