import math
principal = 0
mtly_paymt = 0
interest = 0
last_rate = 0
periods = 0
nominal_interest = 0
# definitionen der Inputs >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def principal_inp():
    global principal
    print('Enter credit principal :')
    principal = int(input('> '))

def mtly_inp():
    global mtly_paymt
    print('Enter monthly payment :')
    mtly_paymt = float(input('> '))

def periods_inp():
    global periods
    print('Enter count of periods :')
    periods = int(input('> '))

def interest_inp():
    global interest
    print('Enter credit interest :')
    interest = float(input('> '))
# Ende der Inputdefinitionen <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Anfang der Formeldefinitionen >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def nom_int(): # berechnet den Monatlichen Zins
    global nominal_interest
    nominal_interest = interest / (12 * 100)
    return nominal_interest

def periods_calc(): # berechnet die Monate
    nomint = nom_int()
    periods = math.ceil(math.log(mtly_paymt / (mtly_paymt - nomint * principal), 1 + nomint ))
    print('Periods = ',periods)
    return periods

def months_years():# berechnet Laufzeit und druckt diese aus
    periods = periods_calc()
    years = 0
    months = 0
    if periods >= 12:
        years = periods // 12
        months = periods % 12
    else:
        months = periods
    if years > 0 and months > 0:
        print('You need {} years and {} months to repay this credit !'.format(years, months))
    elif years > 0 and months == 0:
        print('You need {} year to repay this credit !'.format(years))
    elif years == 0 and months > 0:
        print('you need {} months to repay this credit !'.format(months))

def annuity_payment():
    global periods, principal
    i = nom_int()
    ap = math.ceil(principal * (i * (1 + i) ** periods) / (((1 + i) ** periods) - 1))
    print('Your annuity payment = {}!'.format(ap))

def credit_principal():
    global periods, principal
    i = nom_int()
    n = periods
    a = mtly_paymt
    principal = round(a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
    print('Your credit principal = {}!'.format(principal))

# def print_nom_interest():
#     print('Nominal_interest = ',nom_int(),'aus Funktion print_nom_interest')
#
# def print_periods():
#     print('Periods = ', periods_calc(), 'aus Funktion print_periods')

# Ende der Formeldefinitionen <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def printout():
#     if wish_calc == 'm':
#         if periods == 1:
#             print('It takes 1 month to repay the credit')
#         else:
#             print('It takes {} months to repay the credit'.format(periods))
#     elif wish_calc == 'p':
#         if last_rate == 0:
#             print('Your monthly payment = {}'.format(mtl_rate))
#         else:
#             print('Your monthly payment = {} with last month payment = {}'.format(mtl_rate, last_rate))

# #lastpayment = credit - (periods - 1) * payment
# #payment = credit / periods
# def last_payment():
#     global last_rate
#     last_rate = credit - (periods - 1) * mtl_rate
#
# def payment():
#     global mtl_rate
#     mtl_rate = math.ceil(credit / periods)

def wish_n():# Gesucht die Anzahl der Monate
    principal_inp()
    mtly_inp()
    interest_inp()
    months_years()

def wish_a():# gesucht die Annuitätsrate
    principal_inp()
    periods_inp()
    interest_inp()
    annuity_payment()

def wish_p():#gesucht die Kreditsumme
    mtly_inp()
    periods_inp()
    interest_inp()
    credit_principal()

def selection():
    global credit, wish_calc, wish_payment, periods, mtl_rate
    print('What do you want to calculate?\n'
          'type "n" - for count of months,\n'
          'type "a" - for annuity monthly payment,\n'
          'type "p" - for credit principal')
    wish_calc = input('> ')
    if wish_calc == "n":
        wish_n()
    elif wish_calc == "a":
        wish_a()
    elif wish_calc == "p":
        wish_p()

selection()
