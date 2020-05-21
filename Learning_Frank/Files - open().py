C: == root in Windows
./ == root in Linux

Allgemeines Schema zum arbeiten mit Dateien
-------------------------------------------------------------------------------
1. - Öffnen
2. - Tun was zu tun ist
3. - Schliessen

1. Öffnen der Datei open()
-------------------------------------------------------------------------------
Kein separates Modul erforderlich
- Funktion => open()
    my_file = open('myFile.txt)
  
  Der Parameter kann entweder ein Dateiname oder ein Pfad sein
- Übersicht über die optionalen Parameter von open()
    https://docs.python.org/3/library/functions.html#open
    
2. Parameter in open()
-------------------------------------------------------------------------------
- Zugriffsmodi
    - 'r' - read wenn Datei nicht vorhanden 'error'
    - 'w' - write wenn Datei bereits vorhanden ist, wird sie überschrieben
    - 'a' - zum schreiben offen. Wenn Datei bereits vorhanden, wird der Inhalt angehängt
    - 'b' - im Binärmodus öffnen
    - '+' - zum aktualisieren geöffnet lesen und schreiben
    - 't' - als text öffnen (default) kann deshalb weggelassen werden

- standardmäßig ist der Modus 'rt' aktiviert (read, text)
- Modi können kombiniert werden 
    - 'r+' (read, bearbeiten)
    - 'wb' (write, binär) öffnen zum Schreiben in Binärform
    - 't' textobjekt
    - 'b' byte Objekt
 - Unterschied zwischen 'w' und 'a'
    - 'w' löscht Inhalt und schreibt neu
    - 'a' behält Inhalt und hängt neuen Inhalt an
    
- Encoding wird verwendet wenn Text nicht passt
    # UTF-8
    file_utf8 = open('my_file.txt', encoding='utf-8')
 
    # UTF-16
    file_utf16 = open('my_file.txt', encoding='utf-16')
     
    # CP1252
    file_cp1252 = open('my_file.txt', encoding='cp1252')
  
3. Datei schließen
-------------------------------------------------------------------------------  
- Nach dem arbeiten mit der Datei muss diese geschlossen werden
    # closing the file
    my_file.close()