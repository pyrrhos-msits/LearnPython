# https://docs.python.org/3.6/library/string.html#format-specification-mini-language
# https://www.w3schools.com/python/ref_func_format.asp
#format() Methode
	es werden geschweifte klammern als Platzhalter eingefügt. Der Inhalt dieser Platzhalter wird in der Reihenfolge des
	Auftretens in format angegeben. Mann kann den Platzhaltern auch nummern geben. Diese Nummern beziehen sich dann auf den
	Index in .format(). Man kann auch Keywords benutzen. So lange man entweder Nummern ODER keywords benutzt kann man dieser
	Reihenfolge des Auftretens durch Eintragen in den Platzhaltern festlegen. Wenn man beides mischt, gilt: in der format methode
	kommt zuerst das Argument für die Zahl (positional argument) und dann das Argument für das keyword (keyword Argument)
  #Beispiel:
  print('Mix {}, {} and a {} to make an ideal omelet.'.format('2 eggs', '30 g of milk', 'pinch of salt'))
	Mix 2 eggs, 30 g of milk and a pinch of salt to make an ideal omelet.
  #Beispiel mit Index:
  print('{0} in the {1} by Frank Sinatra'.format('Strangers', 'Night'))
	Strangers in the Night by Frank Sinatra
  print('{1} in the {0} by Frank Sinatra'.format('Strangers', 'Night'))
    Night in the Strangers by Frank Sinatra
  #Beispiel mit Keywords
   print('The {film} at {theatre} was {adjective}!'.format(film='Lord of the Rings',adjective='incredible',theatre='BFI IMAX'))
	 The Lord of the Rings at BFI IMAX was incredible!
  #Beispiel für gemischt 
   print('The {0} was {adjective}!'.format('Lord of the Rings', adjective='incredible'))
	 The Lord of the Rings was incredible!
  #Beispiel für fehlerhafte Anordnumg der Argumente (SyntaxError)
   print('The {0} was {adjective}!'.format(adjective='incredible', 'Lord of the Rings'))
	 SyntaxError: positional argument follows keyword argument
	 
#formatierte String literale
wird genutzt um werte in einen String einzubetten. Man definiert die Werte als variablen. Beim Aufruf wird dann nur
ein f vor den String gesetzt
	#Beispiel:
	name = 'Elizabeth II'
	title = 'Queen of the United Kingdom and the other Commonwealth realms'
	reign = 'the longest-lived and longest-reigning British monarch'
	f'{name}, the {title}, is {reign}.'
	Elizabeth II, the Queen of the United Kingdom and the other Commonwealth realms, is the longest-lived and longest-reigning British monarch.
	# Ein anderes Beispiel
	hundred_percent_number = 1823
	needed_percent = 16
	needed_percent_number = hundred_percent_number * needed_percent / 100
	print(f'{needed_percent}% from {hundred_percent_number} is {needed_percent_number}')
	  16% from 1823 is 291.68
	print(f'Rounding {needed_percent_number} to 1 decimal place is {needed_percent_number:.1f}')
	  Rounding 291.68 to 1 decimal place is 291.7

#Codebeispiel
	gibt den eingegebenen Wert als 
	number = float(input())
	decimal_count = int(input())
	x = '{number:.{digits}f}'.format(number=number, digits=decimal_count)
	print(x)

	