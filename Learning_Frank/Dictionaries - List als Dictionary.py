my_dict = [
     { "name": "Tom", "age": 10 },
     { "name": "Mark", "age": 5 },
     { "name": "Pam", "age": 7 },
     { "name": "Dick", "age": 12 }
 ]

for item in my_dict:
    print(item)

for item in my_dict:
    print(item.keys(), item.values())

for el in my_dict:
    if el['name'] == 'Pam':
        print(el['name'], el['age'])

meals = [
        {"title": "Oatmeal pancakes with apple and cinnamon", "kcal": 370},
        {"title": "Italian salad with fusilli and ham", "kcal": 320},
        {"title": "Bulgur with vegetables", "kcal": 350},
        {"title": "Curd souffle with lingonberries and ginger", "kcal": 225},
        {"title": "Oatmeal with honey and peanuts", "kcal": 440}]

cal = 0
for items in meals:
    cal += items.get('kcal')
print(cal) # 1705