import argparse
import math

# argparse >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type")
parser.add_argument("-c", "--principal", default = None, type=float)
parser.add_argument("-i", "--interest", default = None , type=float)
parser.add_argument("-m", "--payment", default= None, type=float)
parser.add_argument("-p", "--periods", default = None, type=int)
args = parser.parse_args()
# Variablendeklaration >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
type = args.type
principal = args.principal
interest = args.interest
mtly_paymt = args.payment
periods = args.periods
arglst = [principal, interest, mtly_paymt, periods, type]
wish_calc = ''
errmsg = 'Incorrect Parameters'
# Prüfung ob die Argumente den Vorgaben entsprechen >>>>>>>>>>>>>>>>>>>>>>
def check_args():
    if type != 'annuity':
        if type != 'diff':
            print(errmsg)
            exit()
    count = 0
    for el in arglst:
        if el is not None:
            count += 1
    if count != 4:
        print(errmsg)
        exit()
        #print('Zu wenig Parameter gegeben')
    for el in arglst:
        if isinstance(el, int) or isinstance(el, float):
            if el < 0:
                print(errmsg)
                exit()
                #print('Negativer Parameter')
# Prüfung um welche Kreditform es sich handelt und aufruf der entsprechenden Funktionen
def check_credit_type():
    if type == 'annuity':
        check_wish()
    elif type == 'diff':
        diff_form()
# Berechnen der 'diff' Zahlung
# Gegeben:
# -principal=500000 --periods=8 --interest=7.8
def diff_form():
    global principal, periods, interest
    m = 1
    summe = 0
    print('nom_int =', nom_int())
    for el in range(periods):
        dm = math.ceil((principal / periods) + (nom_int() * (principal - (principal * (m -1)) / periods )))
        m += 1
        summe += dm
        print('Month {}: paid out {}'.format(m, dm))
    print('Overpay =', math.ceil(summe - principal))




# Prüfung welcher Wert fehlt um daraus ableitend diesen zu berechnen (nur Annuität)
def check_wish():
    global wish_calc
    if periods is None:
        wish_calc = 'n'
    elif mtly_paymt is None:
        wish_calc = 'a'
    elif principal is None:
        wish_calc = 'p'

# Anfang der Formeldefinitionen >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def nom_int(): # berechnet den Monatlichen Zins
    global nominal_interest
    nominal_interest = interest / (12 * 100)
    return nominal_interest

def periods_calc(): # berechnet die Monate
    global periods
    nomint = nom_int()
    paymt = mtly_paymt
    print('Nom_int = ', nom_int())
    periods = math.ceil(math.log(paymt / (paymt - nomint * principal), 1 + nomint ))
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

def annuity_payment(): # berechnet die Monatsrate
    global periods, principal, mtly_paymt
    i = nom_int()
    mtly_paymt = math.ceil(principal * (i * (1 + i) ** periods) / (((1 + i) ** periods) - 1))
    print('Your annuity payment = {}!'.format(mtly_paymt))

def credit_principal(): # berechnet die Höhe des Annuitätendarlehens
    global periods, principal
    i = nom_int()
    n = periods
    a = mtly_paymt
    principal = round(a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
    print('Your credit principal = {}!'.format(principal))

def overpay_Ann():
    overpay = math.ceil(mtly_paymt * periods - principal)
    print('Overpayment =', overpay)



def selection():
    if wish_calc == "n":
        months_years()
    elif wish_calc == "a":
        annuity_payment()
    elif wish_calc == "p":
        credit_principal()
    if type == 'annuity':
        overpay_Ann()
# Funktionsaufrufe >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
check_args()
check_credit_type()
selection()
