1. any()
2. all()
3. Non-Boolean als Boolean
4. Fallstricke
5. Conditions
6. Beispiele


# arbeiten nur mit iterierbaren Objekten wie z.B. String und List

1. any()>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''any()
gibt 'true' zurück wenn wenigstens eines der elemente in einer Liste oder String
die Bedingung 'true' erfüllt'''

your_results = [True, False, False]
print(any(your_results))  # True

x = [0,0,20356]
print(any(x)) #True

x = ['Frank','Sabine', 'Erwin']
print(any(x)) #True

'''es wird True als 1 und false als 0 angesehen. Dies ergiebt sich aus der bool() Funktion'''
# Beispiel
andy_results = [False, False, False]
print(any(andy_results))  # False

# ebenfalls 'false' weil kein true
jam_results = []
print(any(jam_results))  # False

2. all() >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''all()
prüft ob alle Elemente den Wert 'true' haben '''

x = ['Frank',1, 'Erwin']
print(all(x)) #True

# aber:
x = ['Frank',0, 'Erwin']
print(all(x)) #False

jam_results = []
print(all(jam_results))  # True

3. Non-Boolean als Boolean >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
''' Umwandlung von non-boolean zu boolean '''
# Liste scores. Alle Werte prüfen ob >=3 ergibt die neue Liste [False, False,True,True]
# Mit dieser Liste kann man dann weiter arbeiten
scores = [1, 2, 3, 4]
boolean_scores = [score >= 3 for score in scores]  # [False, False, True, True]
print(any(boolean_scores))  # True
print(all(boolean_scores))  # False

4. Fallstricke >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Beide 'False'
rocket_science_scores = [0, -0, 0.0, +0]
any(rocket_science_scores)  # False
all(rocket_science_scores)  # False

# all() false weil 0 enthalten
math_scores = [0, 1, 2, 3]
any(math_scores)  # True
all(math_scores)  # False

# beide true
biology_scores = [1, 2, 3, 4]
any(biology_scores)  # True
all(biology_scores)  # True

5. Conditions
# schneller Weg um schnell die elemente eine Liste zu prüfen

box = [10, 20, 33]
if any([candy % 2 for candy in box]):
    print("It is not a proper gift.")
else:
    print("Perfect!")#"It is not a proper gift."
    
box = [10, 20, 32]
if any([candy % 2 for candy in box]):
    print("It is not a proper gift.")
else:
    print("Perfect!")#"Perfect !"

6. Beispiele  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# alle Lose über 44 gewinnen. Prüfe ob wenigstens ein Gewinn dabei ist
tickets = [11, 22, 33, 44, 55]
winning_tickets = [i >= 44 for i in tickets]
tickets_bool = any(winning_tickets)