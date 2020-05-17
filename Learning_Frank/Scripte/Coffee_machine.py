# '''Druckt die Liste aus Task 1'''
# print('''
# Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!
# ''')
# '''Task 2 Fragt die Menge an Tassen ab und gibt dann die entsprechenden Mengen für jedes Produkt aus'''
# cups_count = int(input('Write how many cups of coffee you will need: >'))
# für eine Tasse Kaffee wird folgendes benötigt:
water_const = 200 #ml
milk_const = 50 #ml
beans_const = 15 #g
# water_need = water_const  * cups_count
# milk_need = milk_const * cups_count
# beans_need = beans_const * cups_count
# print('''For {} cups of coffee you will need:
# {} ml of water
# {} ml of milk
# {} g of coffee beans'''.format(cups_count, water_need, milk_need, beans_need))
'''Task 3 Fragt die vorhandenen Mengen an Rohstoffen ab und berechnet dann wieviele
Tassen Kaffee gekocht werden können'''
#1. Abfragen der vorhandenen Mengen an Rohstoffen
water_av = int(input('Write how many ml of water the coffee machine has: >'))
milk_av = int(input('Write how many ml of milk the coffee machine has: >'))
beans_av = int(input('Write how many grams of coffee beans the coffee machine has: >'))
#2. Abfragen der gewünschten Kaffeemenge
cups_count = int(input('Write how many cups of coffee you will need: >'))
#3. Berechnen wieviel Tassen Kaffee geliefert werden können

