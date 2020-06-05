eingabe = input()
#list = '12345'

def runing_Average(list):
    newList = []
    avlist = []
    for el in list:
        newList.append(int(el))

    for el in range(len(newList) - 1):
            if el < len(newList):
                newValue = (newList[el] + newList[el + 1]) / 2
                avlist.append(newValue)
    print(avlist)

runing_Average(eingabe)


