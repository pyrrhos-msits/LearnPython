import re

findall() - Gibt Liste mit allen matches zurück
search() - gibt match object zurück
split()
sub()

text = 'Lorem ipsum dolor sit amet, consetetur sadipscing'

1. match() prüft ob der suchstring am Anfang des Textes vorhanden ist
    bei erfolgreichem match wird das ergebnis als match Objekt zurück
    gegeben. Wenn nicht 'None'

regexp = 'Lorem'
result = re.match(regexp, text)
print(result) # <re.Match object; span=(0, 5), match='Lorem'>
print(result.span()) # (0, 5)

regexp = 'ipsum'
result = re.match(regexp, text)
print(result) # 'None'

result = re.match('Fr', 'Frank')