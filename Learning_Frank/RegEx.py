
1. match() 
2. das Punktzeichen
3. Das Fragezeichen
4. Kombination aus Punkt und Fragezeichen
5. Zusammenfassung:

Re Modul wird benötigt
import re

Regular expressions sind casesensitiv


text = 'Lorem ipsum dolor sit amet, consetetur sadipscing'

1. match() 
    prüft ob der suchstring am Anfang des Textes vorhanden ist
    bei erfolgreichem match wird das ergebnis als match Objekt zurück
    gegeben. Wenn nicht 'None'
    Suche nach leerzeichen gibt immer ein match. 

        regexp = 'Lorem'
        result = re.match(regexp, text)
        print(result) # <re.Match object; span=(0, 5), match='Lorem'>
        print(result.span()) # (0, 5)

        regexp = 'ipsum'
        result = re.match(regexp, text)
        print(result) # 'None'

        result = re.match('Fr', 'Frank')
        print(result is None) # False
        print(result) # <re.Match object; span=(0, 2), match='Fr'>

        #Return True oder False wenn der string mit dem template matched:
        def matched(template, string):
            return bool(re.match(template, string))

2. das Punktzeichen
    kann für jedes Zeichen verwendet werden mit Außnahme von '\n'

        regexp = 'python .'
        re.match(regexp, 'python 1') # match
        re.match(regexp, 'python 2') # match
        re.match(regexp, 'python x') # match

        re.match(regexp, 'python \n')# None
        re.match(regexp, 'python?!') # None

3. Das Fragezeichen
    Das Fragezeichen ersetzt kein Zeichen für sich alleine. Es bezieht sich
    auf das Zeichen davor und bedeutet, das dieses Zeichen einmal vorhanden sein 
    kann oder auch nicht.

        regexp = 'regexp?'
        word1 = re.match(regexp, 'regex')  # match
        word2 = re.match(regexp, 'regexp')  # match

4. Kombination aus Punkt und Fragezeichen
    Man kann auch Punkt und Fragezeichen kombinieren. Dies bedeutet dann,
    das vor dem Fragezeichen irgendein Zeichen stehen kann oder auch nicht

    regexp = '.? points? to gryffindor'
 
        # `.? points?` matches `1 point`
        re.match(regexp, '1 point to gryffindor')
        
        # `.? points?` matches `0 points`
        re.match(regexp, '0 points to gryffindor')
        
        # no match, since `.? points?` doesn't match `-5 points`
        re.match(regexp, '-5 points to gryffindor') # weil -5 2 Zeichen sind

5. Zusammenfassung:

Für die Behandlung regulärer Ausdrücke in Python wird das Modul re verwendet.
match()-Funktion des re-Moduls prüft, ob es am Anfang der Zeichenkette eine 
Teilzeichenkette gibt, die mit Ihrer regexp-Vorlage übereinstimmt.
Das Ergebnis der match()-Funktion ist entweder None oder ein Match-Objekt. 
Ein in bool umgewandeltes Match-Objekt ist immer gleich True.
Standardmäßig wird bei regulären Ausdrücken zwischen Groß- und Kleinschreibung
unterschieden.
Punkt . ersetzt jedes Zeichen außer '\n', Fragezeichen ? bedeutet, dass 
das vorherige Zeichen optional ist und in einer Zeichenkette fehlen kann.

