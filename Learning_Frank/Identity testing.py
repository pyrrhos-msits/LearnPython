a = [1, 2, 3]
b = [1, 2, 3]
 
print(a == b)  # True, they contain the same value
 
# But they have different identities
print(id(a))  # 4558721352
print(id(b))  # 4560238984

2. referenzieren beide Variablen das selbe Objekt ist die Id gleich
a = [1, 2, 3]
c = a
 
print(a == c)  # True, they contain the same value
 
# And they also have the same identity
print(id(a))  # 4558721352
print(id(c))  # 4558721352

3. Unterschied zwischen identity Operator und equality Operator
a = [1, 2, 3]
b = [1, 2, 3]
 
identity_test = a is b  # False, because a and b refer to different objects in memory
equality_test = a == b  # True, because a and b contain the same value
 
b = a
 
identity_test = a is b  # True, because now both variables refer to the same object

4. negation von is 
a = [1, 2, 3]
b = [4, 5]
 
print(a is not b)  # True, as expected

5. Wann nutzt man den identity Operator ?
    Zum prüfen ob ein Wert 'None', 'True' oder 'False' ist
    None bedeutet in Python 'kein Wert'
    Es ist üblch in Funktionsdefinitionen None als default value
    für optionale Parameter zu benutzen
    
    def say_hello(name=None):
        if name is None:
            print('Hello!')
        else:
            print(f'Hello, {name}!')
 
 
    say_hello()        # 'Hello!'
    say_hello('Nick')  # 'Hello, Nick!'
    