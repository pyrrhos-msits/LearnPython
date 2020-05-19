#Startet mit leerem Playground und druckt diesen aus
line_of_cells = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

playground = """---------\n| {} {} {} |\n| {} {} {} |\n| {} {} {} |\n---------"""\
    .format(line_of_cells[0][0], line_of_cells[0][1],line_of_cells[0][2],
            line_of_cells[1][0], line_of_cells[1][1],line_of_cells[1][2],
            line_of_cells[2][0], line_of_cells[2][1],line_of_cells[2][2]
            )

print(playground)

# <<<<<<<<<<<<<<<  Here starts the input and check of the coordinates
mover = 'X' #Der jeweilige Spieler 'X' oder 'O'
moves = 0  # Anzahl der Züge, nach 9 sollte Schluss sein, da es nur 9 Felder sind
winner = ''
x = 0 # Erste Eingabe
y = 0 # Zweite Eingabe
occu = 1

def changeMover():
    global mover
    if mover == 'X':
        mover = 'O'
    elif mover == 'O':
        mover = 'X'



def error():
    global moves
    print("This cell is occupied! Choose another one!")
    moves -= 1

def pr_playground():
    global occu
    print("""---------\n| {} {} {} |\n| {} {} {} |\n| {} {} {} |\n---------""" \
          .format(line_of_cells[0][0], line_of_cells[0][1], line_of_cells[0][2],
                  line_of_cells[1][0], line_of_cells[1][1], line_of_cells[1][2],
                  line_of_cells[2][0], line_of_cells[2][1], line_of_cells[2][2]
                  ))
    changeMover()#Setzt den Player von 'X' zu 'O' und umgekehrt
    occu -= 1

def move():
    global a, b, x, y, occu, playground, mover
    occu = 1
    if x == 1 and y == 3:
        if line_of_cells[0][0] == ' ': #wenn leer
            line_of_cells[0][0] = mover# dann setze den Wert auf den value der Variable 'mover'
            pr_playground()
        else:
            error()
    elif x == 1 and y == 2:
        if line_of_cells[1][0] == ' ':
            line_of_cells[1][0] = mover
            pr_playground()
        else:
            error()
    elif x == 1 and y == 1:
        if line_of_cells[2][0] == ' ':
            line_of_cells[2][0] = mover
            pr_playground()
        else:
            error()
    elif x == 2 and y == 3:
        if line_of_cells[0][1] == ' ':
            line_of_cells[0][1] = mover
            pr_playground()
        else:
            error()
    elif x == 2 and y == 2:
        if line_of_cells[1][1] == ' ':
            line_of_cells[1][1] = mover
            pr_playground()
        else:
            error()
    elif x == 2 and y == 1:
        if line_of_cells[2][1] == ' ':
            line_of_cells[2][1] = mover
            pr_playground()
        else:
            error()
    elif x == 3 and y == 3:
        if line_of_cells[0][2] == ' ':
            line_of_cells[0][2] = mover
            pr_playground()
        else:
            error()
    elif x == 3 and y == 2:
        if line_of_cells[1][2] == ' ':
            line_of_cells[1][2] = mover
            pr_playground()
        else:
            error()
    elif x == 3 and y == 1:
        if line_of_cells[2][2] == ' ':
            line_of_cells[2][2] = mover
            pr_playground()
        else:
            error()
'''Prüft ob die eingegebenen Coordinaten zwischen 1 und 3 liegen'''
def check_coord():
    global moves
    count = 0
    if x == 0 or x > 3:
        count += 1
        #print('X erhöht count:' ,count)
    elif y == 0 or y > 3:
        count += 1
        #print('Y erhöht count:', count)
    if count > 0:
        print("Coordinates should be from 1 to 3!" )
        moves -= 1
    else:
        move()

def play():
        global x, y, moves
        a, b = input('Enter the coordinates: >').split()
        if a.isdigit() and b.isdigit():
            x = int(a)
            y = int(b)
            check_coord()
        else:
            print('You should enter numbers!')
            moves -= 1




def result_check():
    resul_l = [0,0,0,0,0,0,0,0,0]

# x = 0,2,4,6
# y = 1,3,5,7
    x_r = 0
    o_r = 0
    x_s = 0
    o_s = 0
    x_dl = 0
    o_dl = 0
    x_dr = 0
    o_dr = 0
    draw = 0
    empty_el = 0

# Prüfen auf Reihen
    result_row = ''
    for cell in line_of_cells:
        for el in cell:
            if cell[0] == cell[1] and cell[1] == cell[2]:
                if cell[0] == 'X':
                    x_r += 1
                    resul_l[0] = 1
                elif cell[0] == 'O':
                    o_r += 1
                    resul_l[1] = 1
            if el == ' ' or el == '_':
                empty_el += 1

# prüfen auf Spalten
    result_col = ''
    if line_of_cells[0][0] == line_of_cells[1][0] == line_of_cells[2][0]:
        if line_of_cells[0][0] == 'X':
            x_s += 1
            resul_l[2] = 1
        if line_of_cells[0][0] == 'O':
            o_s += 1
            resul_l[3] = 1
    if line_of_cells[0][1] == line_of_cells[1][1] == line_of_cells[2][1]:
        if line_of_cells[0][1] == 'X':
            x_s += 1
            resul_l[2] = 1
        if line_of_cells[0][1] == 'O':
            o_s += 1
            resul_l[3] = 1
    if line_of_cells[0][2] == line_of_cells[1][2] == line_of_cells[2][2]:
        if line_of_cells[0][2] == 'X':
            x_s += 1
            resul_l[2] = 1
        if line_of_cells[0][2] == 'O':
            o_s += 1
            resul_l[3] = 1

# prüfe die Diagonalen links oben nach rechts unten
    result_diag_left = ''
    if line_of_cells[0][0] == line_of_cells[1][1] == line_of_cells[2][2]:
        if line_of_cells[0][0] == 'X':
            x_dl += 1
            resul_l[4] = 1
        if line_of_cells[0][0] == 'O':
            o_dl += 1
            resul_l[5] = 1

# prüfe die Diagonalen rechts oben nach links unten
    result_diag_rigth = ''
    if line_of_cells[0][2] == line_of_cells[1][1] == line_of_cells[2][0]:
        if line_of_cells[0][2] == 'X':
            x_dr += 1
            resul_l[6] = 1
        if line_of_cells[0][2] == 'O':
            o_dr += 1
            resul_l[7] = 1



# x = 0,2,4,6
# y = 1,3,5,7

# Prüfen auf DRAW und Game ot finished
# count0 = 0
# count1 = 0
# for res in resul_l:
#     if res == 0:
#         count0 += 1
#         if count0 == len(resul_l):
#             if empty_el > 0:
#                 print("Game not finished" )
#             else:
#                 print("Draw")

# # prüfen auf  X vins, O vins
    global winner
    if resul_l[0] == 1 or resul_l[2] == 1 or resul_l[4] == 1 or resul_l[6] == 1 and resul_l[1] == 0 and resul_l[2] == 0 and resul_l[5] == 0 and resul_l[7] == 0:
       print('X wins')
       winner = 'X'
    elif resul_l[1] == 1 or resul_l[3] == 1 or resul_l[5] == 1 or resul_l[7] == 1 and resul_l[0] == 0 and resul_l[2] == 0 and resul_l[4] == 0 and resul_l[6] ==0:
         print('O wins')
         winner = 'O'

while moves <= 9:
    play()
    result_check()
    moves += 1
    if winner == 'X' or winner == 'O':
        break
    if moves == 9:
        if winner != 'X' and winner != 'O':
            print('Draw')
            break