https://hyperskill.org/learn/step/6752
https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

Statuscodes:

1xx - Informationen
2xx - Erfolg
3xx - Umleitung weitere Aktion erforderlich
4xx - Client Error
5xx - Servererror


Vor der Arbeit mit requests muss diese erst mal importiert werden

import requests

1. Get requests
-----------------------------------------------------------------------

r = requests.get('https://requests.readthedocs.io/en/master/')
print(r)
# <Response [200]>

print(r.status_code) #200

Der request gibt das response Object zurück (r).

Wenn man dieses response Obfect in einer if Anweisung benutzt so gibt 
diese 'True' zurück wenn der statuscode der response mit 2 oder 3 an-
fängt ('Erfolg' oder 'Umleitung')

if r:
    print('Success')
else:
    print('Fail')

# Sucess
Alles über das responseObject
https://www.w3schools.com/python/ref_requests_response.asp

Um den Inhalt der Server response zu lesen:
- r.text

Requests decodiert automatisch. Um herauszufinden wie die Textnachricht
encodiert ist oder um diese zu ändern kann man die methode encoding nutzen
- r.encoding # utf-8

Andere Informationen z.B den content type bekommt man mit der .headers methode 
- r.headers # druckt den html header aus

Der Header kommt als dictionary. Der header ist nicht case sensitiv
- r.headers['Content-Type'] # 'text/html'
 # funktioniert genauso wie:
- r.headers['content-type'] # 'text/html'

- return requests.get(url).headers['Content-type'] # ohne die Variable 'r'

2. Query parameter
----------------------------------------------------------------------------------

Ein Abfrage String ist eine konvention zum anhängen von key-value paaren an eine url
- Von der standard URL wird er durch ein '?' separiert.
- Key und value werden separiert mit einem '='
- die paare werden separiert durch ein '&'
# 2 Beispiele:

    - http://example.com/?a=c&b=d
    - http://example.com/page?a=c&b=d

Query Strings können Felder enthalten, hinzugefügt zur Basis URL vom Browser oder von anderen
Client Applicationen. Wie diese Paramter genutzt werden, hängt von der Server seitigen 
Applikation ab.
# Beispiel :
    - https://www.python.org/search/ ist die Suchseite von python
        Wenn man dort jetzt nach 'requests' suchen will, sieht die URL 
        so aus:  https://www.python.org/search/?q=requests
        Bei der Benutzung von 'requests' ist es nicht erforderlich den query String 
        manuell an die URL zu hängen. Wir können die Argumente als dictionary 
        von Strings mit dem 'params' keyword mitgeben:
        # The dictionary of the query parameters
        params = {'q': 'requests'}
        
        # This request will get the page with the results of the search for 'requests'
        # on the official Python website:
        r = requests.get('http://python.org/search', params=params)

3. wiederkehrende requests als funktion:
--------------------------------------------------------------------------------
Wenn man einen request innerhalb eines Projektes mehrmals senden muss, ist es 
sinnvoll eine spezielle Funktion dafür zu definieren.
Z.B gibt die folgende Funktion eine seite zurück die die Ergebnisse der Google 
Suche nach 'python' enthält. Die '1' bedeutet, das nur ein Suchergebniss angezeigt 
wird. Würde dort eine '5' stehen, würden 5 Ergebnisse angezeigt.
    def google_search(query, num):
        r = requests.get('https://google.com/search',
                        params={'q': query, 'num': num})
        return r.url
    
    
    print(google_search('python', 1))
    
    # https://www.google.com/search?q=python&num=1


