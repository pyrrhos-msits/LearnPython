# use the function blackbox(lst) that is already defined

lst = [2, 4, 6]
idlst = id(lst)
idlst1 = id(blackbox(lst))

if idlst == idlst1:
    print('modifies')
else:
    print('new')