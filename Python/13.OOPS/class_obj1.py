# in python every thing is object

 

class Student:
    # Attributes/Class Variables
    id = 0
    name = ""
    gender = ""
    age = 0
    # Methods
    def display(self):
        print(f"ID = {self.id}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")
    def displayName(self):
        print(f"Your name is {self.name}")


s1 = Student()
s2 = Student()
s1.id = 65
s1.name = "Anirudh Khurana"
s1.age = 56
s1.gender = "Male"
s1.display()
print("--------")
s2.display()