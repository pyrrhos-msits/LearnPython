import argparse
import math

# argparse >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type")
parser.add_argument("-c", "--principal", default = None, type=int)
parser.add_argument("-i", "--interest", default = None , type=float)
parser.add_argument("-m", "--mtly_paymt", default= None, type=float)
parser.add_argument("-p", "--periods", default = None, type=int)
args = parser.parse_args()
# Variablendeklaration >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
type = args.type
principal = args.principal
interest = args.interest
mtly_paymt = args.mtly_paymt
periods = args.periods
arglst = [principal, interest, mtly_paymt, periods, type]
errmsg = 'Incorrect Parameters'
# check args >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def check_args():
    if type != 'ann':
        if type != 'diff':
            # print(errmsg)
            print('Falscher Darlehenstyp')
    count = 0
    for el in arglst:
        if el is not None:
            count += 1
    if count != 4:
        #print(errmsg)
        print('Zu wenig Parameter gegeben')
    for el in arglst:
        if isinstance(el, int) or isinstance(el, float):
            if el < 0:
                #print(errmsg)
                print('Negativer Parameter')

def nom_int(): # berechnet den Monatlichen Zins
    global nominal_interest
    nominal_interest = interest / (12 * 100)
    print('Nominal Interest', nominal_interest)
    return nominal_interest

def periods_calc(): # berechnet die Monate
    nomint = nom_int()
    print('Nom_int = ', nom_int())
    periods = math.ceil(math.log(mtly_paymt / (mtly_paymt - nomint * principal), 1 + nomint ))
    #periods = math.log(mtly_paymt / (mtly_paymt - nomint * principal), 1 + nomint)
    print('Periods = ',periods)
    return periods
# Funktionsaufrufe >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
check_args()
nom_int()
periods_calc()



