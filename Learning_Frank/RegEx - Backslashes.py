Der '.' und das '?' haben besondere Bedeutung in Regex
Wenn wir jetzt einen von den beiden suchen wollen, benötigen wir den '\'
davor.

    # Beispiele
    import re
    re.match('\?', '?') #match
    re.match('\\?', '?') #match
    re.match('\.', '.') #match
    re.match('?', '?') # syntax error

Wenn man nach Backslashes '\' selber suchen will. muss man einen 
doppelten Backslash vor die Suche machen '\\'

    #Beispiel
    re.match('\\\\', '\\') # match
    re.match('\\', '\\') # SyntaxError

Es gibt keine Probleme, wenn man den Bachslash mit einem Zeichen danach sucht
    #Beispiel
    re.match('\t', '\t') # match
    re.match('\\t', '\t') #match

Man kann auch auf Backslashes verzichten wenn man den prefix 'r' verwendet

    #Beispiel
    regexp = r'?'

Der r prefix ist ein 'raw string notation prefix' Er sagt Python, das es keine
Escape Sequencen benutzen soll. Dadurch werden alle backslashes behandelt wie 
normale Zeichen.

re.escape
