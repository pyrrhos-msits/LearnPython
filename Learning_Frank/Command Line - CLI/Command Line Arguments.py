https://hyperskill.org/learn/step/7981

1. Script aufrufen
2. Zugreifen auf die angegebenen Argumente 
3. Überprüfen der Anzahl der Argumente mit len()

1. Script aufrufen
    - py (oder Python) damit der Interpreter weiß das es Python istitle
    - Pfadname
    - Dateiname
    - Argumente werden durch Leerzeichen getrennt nach dem Scriptnahmen geschrieben
    # Beispiel:
    - Hier sollen 2 Argumente übergeben und dann multipliziert werden: 
    - py C:\python_scripts\add_two_numbers.py 11 44
    - py ..\python_scripts\add_two_numbers.py 11 44
    
2. Zugreifen auf die angegebenen Argumente 
- import sys
- mit sys.argv erhalten wir die vom User angegebenen Argumente als Liste
- hierbei ist sys.argv[0] der Name unseres Python Scripts
- die nächten Listenelemente, sind Argumente auf die mittels Index zugegriffen werden
    kann. ACHTUNG die Argumente sind string. Wenn Zahlen gebraucht werden, muss 
    konvertiert werden.
    # Beispiel:
    import sys  # first, we import the module
 
    args = sys.argv  # we get the list of arguments
    first_num = float(args[1])  # convert arguments to float
    second_num = float(args[2])
     
    product = first_num * second_num
     
    print("The product of " + args[1] + " times " + args[2] + " equals " + str(product))
 
 3. Überprüfen der Anzahl der Argumente mit len()
        import sys  
        args = sys.argv  
         
        if len(args) != 3:
            print("The script should be called with two arguments, the first and the second number to be multiplied")
         
        else:
            first_num = float(args[1])  
            second_num = float(args[2])
         
            product = first_num * second_num
         
            print("The product of " + args[1] + " times " + args[2] + " equals " + str(product))
            