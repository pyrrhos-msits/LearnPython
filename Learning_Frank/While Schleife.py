

while True:
    a, b = input().split()
    if int(b) != 0:
        print(a, b)
        continue
    if int(b) == 0:
        print('error')
        continue
  
# Schreibe einen Loop bei dem zwei Zahlen eingegeben werden  
# Wenn der Nutzer nur eine Zahl ausdruckt, drucke diese
# Wenn die Nutzereingabe leer ist mache weiter
# Wenn es zwei gültige Zahlen sind drucke die Summe dieser Zahlen
# Wenn der User '/exit' eingibt beende das Program
while True:
    user = input()
    listuser = user.split()
    if user == '/exit':
        print('Bye!')
        break
    elif user == '':
        continue
    elif len(listuser) == 1:
        print(user)
        continue
    else:
        a, b = user.split()
        print(int(a) + int(b))