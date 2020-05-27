CLI - CommandLineInterface
GUI - Graphical User Interface

Alle command Line Befehle https://ss64.com/
argparse https://www.pyimagesearch.com/2018/03/12/python-argparse-command-line-arguments/
1. Python Script von der CLI aufrufen:
    py Pfadname\Scriptname Arg1 Arg 2
    py C:\python_scripts\add_two_numbers.py 11 44
    py ..\python_scripts\add_two_numbers.py 11 44
    
2. System Modul (sys module)
    Stellt Zugang zu funktionen und variablen her und erlaubt
    so die Arbeit mit Python
   
    - sys.argv
        Beim Aufruf von sys.argv stellen wir die Argumente
        als Liste zur Verfügung. Die Argumente sind indexiert.
          Index[0] - Dateiname oder Pad zur Dateiname
    #Beispiel
    import sys # modul importieren
    args = sys.argv # wir erhalten die Liste der Argumente
    if len(args) != 3:
        print("The script should be called with two arguments, the first and the second number to be multiplied")
    else:
        first_num = float(args[1])
        second_num = float(args[2])
        product = first_num * second_num
    print("The product of " + args[1] + " times " + args[2] + " equals " + str(product))
