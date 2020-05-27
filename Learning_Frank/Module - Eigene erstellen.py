- Modul ist eigentlich nur eine Datei mit der Erweiterung '.py'
- Einfache Module werden auch als Script bezeichnet

1. Ausführen eines Scripts
---------------------------------------------------------------------------------

    - C:> py <script>
oder
    - C python <script>

Hierbei ist <script> der Name oder Pfad zum Script

2. Modulimport 
---------------------------------------------------------------------------------
- modul wird importiert mit 
    - import Dateiname ohne py #import hello

- Nach dem Import Befehl wird das Modul sofort ausgeführt. Dies lässt sich nicht umgehen
- Um dies zu vermeiden, muss man §3 lesen https://hyperskill.org/learn/step/6057

- simple Lösung 2 Dateien. Eine enthält nur die definitionen. Die andere enthälte den Code
    der Definitionen aus der ersten Datei verwendet und ausführt.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Oder verwendung von if __name__ == "__main__":
    # Beispiel safe_module.py
    
    name = "George"
    if __name__ == "__main__":
        print("Hello,", name)

Hierbei wird der Wert von __name__ überprüft und die Zeile nur gedruckt wenn das Modul als 
Script ausgeführt wird.
     #safe_bye.py script
 
    from safe_module import name
    print("Bye,", name)   

Wenn ich jetzt name importiere wird nicht das script ausgeführt sondern nur der wert der Variable
übergeben
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Wenn ich aber mehrere mehr als nur eine Zeile in einem Script ausführen will, ist es praktischer
den code in eine Funktion namens main auszulagern und ihn dann wie folgt aufzurufen:
    #Beispiel safe_main_module.py
    name = "George"
    
    def main():
        print("Hello,", name)
    
    if __name__ == "__main__":
        main()


3. Verwechslungen mit Built in Modulen vermeiden:
----------------------------------------------------------------------------------

Um verwechslungen mit eingebauten Modulen zu vermeiden sollte man folgende
Benamsung einhalten:
        - anstelle von hello.py einfach hello_script.py

