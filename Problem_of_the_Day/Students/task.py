class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        idno = self.name[0] + self.last_name + self.birth_year
        print(idno)

x = input()
y = input()
z = input()
frank = Student(x, y, z)
