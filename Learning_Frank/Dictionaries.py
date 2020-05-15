my_dict = {'Name': 'Frank', 'Street': 'Stieglitzweg', 'No': '3', 'PLZ': '87527', 'City': 'Sonthofen'}

print(my_dict)

print('----------------------------------------')

x = my_dict.get('Name')
print(x)

print('----------------------------------------')

for keys in my_dict:
    print(keys)

print('----------------------------------------')

for value in my_dict.values():
    print(value)

print('----------------------------------------')

for key, value in my_dict.items():
    print(key, value)

