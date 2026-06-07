# -----Base Class-----

class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def introduce(self):
        print(f"Hi, I am {self.name},I am {self.age} years old.")
    
    def result(self):
        if self.marks>=40:
            print(f"{self.name} has passed with {self.marks} marks.")
        else:
            print(f"{self.name} has failed.")
s1=Student("Megshyam",22,78)
s2=Student("Rahul",24,35)
s1.introduce()
s1.result()

s2.introduce()
s2.result()

#  ----Class variable vs Instance variable----
class Student:
    college="Priyadarshini College Nagpur" #this is a class varibale
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

s1=Student("Megshyam",77)
s2=Student("Rahul",56)
print(s1.college)
print(s2.college)
print(s1.name)
print(s2.name)
Student.college="KDK College" #this is an instance varibale
print(s1.college)

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return f"Student:{self.name}|{self.marks}"

s1=Student("Megshyam",78)
print(s1)
# ---Inheritance---
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says:Meow ")

class Duck(Animal):
    pass

d=Dog("Bruno")
c=Cat("Tom")
duck=Duck("donald")
d.speak()
c.speak()
duck.speak()

# ----parent func----
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"I am {self.name},age {self.age}.")
class Employee(Person):
    def __init__(self,name,age,company,salary):
        super().__init__(name,age)
        self.company = company
        self.salary = salary
    def details(self):
        print(f"{self.name} works at {self.company} and earns {self.salary}/month.")

e1=Employee("Megshyam",23,"Techstartup",45000)
e1.introduce()
e1.details()