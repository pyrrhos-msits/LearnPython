cards = {'Ace': 14, 'King': 13, 'Queen': 12, 'Jack': 11}
count = 0
summe = 0
while count < 6:
    card = input()
    if card.isdigit():
        summe += int(card)
    else:
        summe += cards.get(card)
    count += 1
print(summe / count)

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