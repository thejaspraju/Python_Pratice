# in python every thing is object

class Student:
    # Attributes/Class Variables
    id = 0
    name = ""
    gender = ""
    age = 0
    # Methods

    def setDetails(self):
        self.id = int(input("Enter ID = "))
        self.name = input("Enter name = ")
        self.gender = input("Enter gender = ")
        self.age = int(input("Enter age = "))
    def display(self):
        print(f"ID = {self.id}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")

    def displayName(self):
        print(f"Your name is {self.name}")

s1 = Student()
s1.setDetails()
s1.display()