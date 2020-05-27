In Python ist ist unendlichkeit eine Konstante größer
als jede reale Zahl. Dies wird als 'inv' bezeichnet
# Beispiel:
    print(float(10 ** 3000))#Overflow error
    print(float('1e3000'))# inf
    Zeile 1 ist zu groß um dargestellt zu werden.
    Zeile 2 gibt inv zurück. Damit kann dan weiter gearbeitet werden
            die Schreibweise heist 'floating point literal'
    
    
Wenn man mit inf experimentieren möchte kann man die
String Literale:
    - 'inf' # Größer als jede reelle Zahl
    - 'infinity'
    - '-inf' # Kleiner als jede reelle Zahl
    - '- infinity'
nutzen.

Syntax ist immer die selbe:
print(float('inf')) #inf


- kleiner als jede reelle Zahl ist -inf
    print(float('-inf')) # -inf

- wie alle Fließkommazahlen unterstützen inv und -inv alle arithmethischen Operationen
    inf = float("inf")
 
    # addition
    print(inf + inf)   # inf
    print(inf + 1)     # inf
     
    # multiplication
    print(-inf * -66)  # inf
    print(-inf * inf)  # -inf
     
    # subtraction
    print(-inf - inf)  # -inf
    print(inf - 9999)  # inf

- Gleitkommazahlen enthalten einen weiteren speziellen Wert:
    -NaN (Not a number)

Unterschiede 'NaN' und 'None'
    - 'NaN' != 'NaN' ist 'True'
    - 'NaN' == 'NaN'  gibt Flase
    - 'None' ist immer 'False'
    
    
-Testen auf 'NaN' mit math.isnan()
    - Gibt nur 'True' zurück wenn ihr Argument 'Nan' lautet
    import math

    inf = math.inf   # an alternative way
    nan = math.nan   # to get the constants
    
    math.isnan(nan)  # True - Not a Number
    math.isnan(inf)  # False - infinity
    math.isnan(0.0)  # False - Float
    
- math.isinf() prüft ob ein wert unendlich ist egal ob positiv oder negativ
    math.isfinite(7.54)  # True
    math.isfinite(inf)   # False
    math.isfinite(nan)   # False
    math.isinf() hilft bei der Suche nach Fließkommazahlen die sich von den sonderwerten 
    unterscheiden
    
- Ähnliche Funktionen sind bei anderen Ressourcen zu finden. Zum Beispiel stellt die Bibliothek
 für wissenschaftliches Rechnen NumPy folgende Funktionen zur Verfügung: isinf, isposinf, iseginf,
 isan und isfinite. Wir empfehlen Ihnen, einige der genannten Funktionen zu verwenden, da sie mit
 größerer Wahrscheinlichkeit ein dem Standard entsprechendes Ergebnis liefern.    
 
- Zusammenfassung:
    Python-Floats enthalten die speziellen Werte inf, -inf und nan.
    Die inf-Konstante ist größer als jede reelle Zahl. Um sie zu erzeugen, verwenden Sie
    float("inf") oder math.inf.
    Die Konstante -inf ist kleiner als jede beliebige Fließkommazahl. Sie können sie über 
    float("-inf") oder -math.inf erhalten.
    Die Konstante nan steht für "not a number" und ist nicht gleich irgendeiner Gleitkommazahl.
    Verwenden Sie float("nan") oder math.nan, um sie zu erhalten.
    Das Mathematikmodul verfügt über Funktionen, die für spezielle Werttests entwickelt wurden: 
    math.isinf(), math.isnan(), math.isfinite().