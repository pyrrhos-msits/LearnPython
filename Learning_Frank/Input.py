# input() liest vom user eingegebene Daten und gibt diese als String zurück
# int(input()) gibt einen Integer zurück
# float(input()) gibt floating ponint zurück
day = int(input())
month = input()
print(day , month)
input()

# <<Fragt nur den usernamen ab. >>
# user_name = input('Please enter your name: ')
# print('Hello, ' + user_name)
# input()

# Eine andere Art den Username abzufragen
print('Enter your Name: ')
user_name = input()
print('Hello, ' + user_name)
input()

# Mehrere Werte als Liste eingeben
# die Werte müssen mit Freizeichen getrennt sein.
# nach Eingabe des Letzten Wertes kommt Enter
mylist = [int(n) for n in input().split()]
print(mylist)