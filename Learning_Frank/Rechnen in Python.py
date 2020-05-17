
1. Rechneoperationen
2. Operation priority
3. Runden
4. Wurzel ziehen

1. Rechneoperationen >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 1.
- // ist die Division von Integer
- /  ist die Division von Floating
- - Operator ist ein unary Operator | print(-(100 + 200))  # -300
- % modulo Operator gibt den Rest aus. Wenn ich wissen will ob eine Zahl gerade oder ungerade ist, 
                  muss ich prüfen ob der Rest = 0 ist.
- ** Power print(10 ** 2) #100  scheint so als würde das 10 hoch 2 entsprechen

2. Operation priority >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 2.
1 parentheses
2 power
3 unary minus
4 multiplication, division, and remainder
5 addition and subtraction


3. Runden: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 3.
- round() rundet Mathematisch  als Argumente kann man die Komma-
  stellen mit geben. 
  a = 25.2635
  b = round(a, 2)
  print(b)

- Aufrunden auf nächst ganzzahl:
    import math
    x = 25.01
    y = math.ceil(x)
    print(y) #26

- Abrunden auf nächste Ganzzahl:
    import math
    x = 25.99
    y = math.floor(x)
    print(y) #25
    
4. Wurzel ziehen
    import math
    x = math.sqrt(49)
    print(X) #7