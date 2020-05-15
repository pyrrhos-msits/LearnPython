class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hello, I am {}!".format(self.name))

pers_name = input()
my_person = Person(pers_name)
my_person.greet()