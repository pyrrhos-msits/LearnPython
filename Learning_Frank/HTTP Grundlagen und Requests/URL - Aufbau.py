1. Struktur der URL:

# Beispiel
https://material.io/design/material-theming/#material-theming
https://     - protocol
material.io  - Domain
/design/material-theming/   - Pfad
#material-theming   - Anker (anchor)

#Struktur der URL
<protocol>://<login>:<password>@<host>:<port>/<path>?<request parameters>#<anchor>

<protocol>  - Möglichkeit, Daten mit einer Ressource auszutauschen. (z.B http oder https)
<login><password>  - Präfixe die bei Bedarf Authentifizierungsdaten übertragen
<host> - Domainname oder IP Adresse
<port> - für Verbindung des hosts erforderlich. Prinzipiell alles erlaubt. Aber es gibt 
            Standardports: - http 80 oder 8080
                            - https 443
<path> - gibt die genaue Adresse der ressource (seite) an.
<request parameters> - sind parameter die an die seite übermittelt werden
<anchor> - ermöglicht die Verbindung zu einem bestimmten Teil einer webseite oder eines Dokuments

Wenn man nur eine bestimmte Seite anzeigen will ist die Struktur einfacher:
<protocol>://<host>

2. Absolute und relative URL's
relativ : www.jetbrains.com 
absolut : https://www.jetbrains.com/pycharm/ 

