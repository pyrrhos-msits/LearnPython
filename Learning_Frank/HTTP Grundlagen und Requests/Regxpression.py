import re

text = 'Lorem ipsum dolor sit amet, consetetur sadipscing'
#match() positive
regexp = 'Lorem'
result = re.match(regexp, text)
print(result)
#match() negative
regexp = 'ipsum'
result = re.match(regexp, text)
print(result)
# match zur prüfung von teilen eines Wortes
result = re.match('Fr', 'Frank')
print(result)

regex = 'n?N?ever gonna'
string1 =
string2 =
string3 =