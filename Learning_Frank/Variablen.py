# leere Variable definieren
my_str = ''
my_num = 0

# mehrere Variablen auf einmal deklarieren u bearbeiten
a, b = 4, 15
print(a, b)# 4, 15
a, b = a, a + b # a bleibt , b = 4 + 15
print(a , b) # 4 19
a , b = b, b - a # a ist gleich b (19) , b = 19 - 4
print(a, b) # 19, 15
