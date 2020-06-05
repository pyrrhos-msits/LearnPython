1. Herausbekommen ob pip installiert ist:
    - cmd öffnen
    - py -m pip --version
    - die Befehle funktionieren nicht in der Python Konsole sondern nur in der CMD Line

2. Installation von packages:
    - py -m pip install 'some package'
    - wenn man eine bestimmte Version installieren will: install 'some_package==1.1.2'
    - oder eine minimum Version angeben: py -m pip install "some_package>=1.1.2" Wichtig doppelte Anführungszeichen

3. Weiter Befehle

    - pip show some_package | Zeigt infos and
    - pip list 
    - pip list --outdated oder pip list -o 
    - pip install --upgrade 'PackageName'
    - pip uninstall 'PackageName'

4 Anforderungsdatei erstellen
    - pip freeze > requirements.txt 

5. Alle elemente aus Anforderungsdatei installieren 
    - pip install -r requirements.txt 







