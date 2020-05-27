Pakete sind eine Möglichkeit Module mit Hilfe der 'dotted module names' hierarchisch zu strukturieren

1. Paketdefinition und struktur
----------------------------------------------------------------------------------------------------------

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

2. Pakete importieren und referenzieren
-------------------------------------------------------------------------------------------------------------
            