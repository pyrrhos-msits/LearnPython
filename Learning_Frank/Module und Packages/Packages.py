Pakete sind eine Möglichkeit Module mit Hilfe der 'dotted module names' hierarchisch zu strukturieren

1. Paketdefinition und struktur
############################################################################################################
Um ein Paket zu erstellen muss ein Unterordner im Programmverzeichniss erstellt werden.
Der Name des Ordners entspricht dem Namen des Paketes.
Ein Paket kann beliebig viele weitere Pakete (subpackages) enthalten die wiederum subpackages enthalten können 

# Beispiel

        package/                           # Zuerst bezeichnen wir das Haupt oder Toplevel package
                    __init__.py            # dieses directory sollte als package behandelt werden
                    subpackage/            # subpackages werden mit extra modulen hinzugefügt
                        __init__.py        # dieses directory sollte als subpackage behandelt werden
                        artificial.py
                        amateurs.py
                        ...
                    subpackage2/                  
                        __init__.py  # wichtig ist __init__.py Dieses sorgt dafür das Python das Verzeichnis
                        amazing.py   # als Paket / Unterpaket behandelt
                        animate.py
                        barriers.py
                        ...
__init__.py muss als Datei angelegt sein (Laut Buch nur bis Python 3.3). Diese Datei kann leer sein oder den Initialisierungscode für 
das Paket ausführen.

2. Pakete importieren und referenzieren
############################################################################################################
Es gibt zwei Möglichkeiten das 'artificial' Submodul aus dem 'subpackage' zu importieren
    1. Methode
    ----------
    - from package.subpackage import artificial
        Jetzt braucht man bei verwendung des Submoduls das Paket und Subpaket nicht zu benennen:
            - artificial.function(arg1, arg2)
    2. Methode (die Übersichtlichere)
    ----------------------------------
    - import package.subpackage.artificial
        wenn das Submodul so geladen wurde sollte auf seinen Inhalt mit seinem vollständigem Namen 
        verwiesen werden:
            - package.subpackage.artificial(arg1, arg2)
    3. Es ist auch möglich nur eine bestimmte Funktion aus dem Submodul zu importieren
    ----------------------------------------------------------------------------------
    - from package.subpackage.artificial import function
        Danach kann man die function direkt adressieren ohne den vollständigen Pfad zu einem Module
        anzugeben:
            - function(arg1, arg2)

3. Import * Vorteile und Nachteile
#############################################################################################################
Es wäre auch möglich alle Submodule eines Subpaketes auf einmal zu importieren.
    - from package.subpackage import *
Dieses ist aber zeitaufwändig und schlechte Praxis weil, man auch Sachen mit importiert, die man nicht braucht
    - wichtig ist das Paket mit Hilfe der __all__ Anweisung mit einem bestimmten Index zu versehen, der in 
        die Datei __init__.py eingefügt werden soll. Dort wollen Sie die Submodule auflisten, die importiert 
        werden sollen, während die Operation "from package import *" ausgeführt wird.
            - __all__ = ["submodule1", "submodule10"]

4. Intra-Paketreferenzen
###############################################################################################################
Um das ganze auf die Spitze zu treiben ist es auch möglich auf Submodule von Geschwisterpaketen zu verweisen.
Wenn man z.B. mit package.subpackage.artificial arbeitet und dort etwas aus package.subpackage2.amazing braucht,
kann man es nach artificial importieren mit: 'package.subpackage2 import amazing'

Es geht auch mit der 'relativer Import' methode. Hierbei werden führende Punkte verwendet um aktuelle und über-
geordnete Pakete anzuzeigen. Hierbei würde für den Import von 'amateurs'(subpackage) folgendes verwendet werden:
    - from . import artificial # ein Punkt adressiert zu einem atuellem Package/subpackage
    - from .. import subpackage2 # zwei Punkte adressieren eine Verzeichnisebene höher
    - from .. subpackage2 import module

5. Zu vermeiden
################################################################################################################




