# 12_Hierarchical_Inheritance
# ============================================================
# 12_Hierarchical_Inheritance.py
# Hierarchical Inheritance in Python
# ============================================================


# ============================================================
# WHAT IS HIERARCHICAL INHERITANCE?
# ============================================================

# Hierarchical inheritance means:
#
# One parent → Multiple child classes
#
#
# Example:
#
#             Parent
#             /    \
#          Child1  Child2
#
#
# Multiple child classes inherit from
# the same parent class.


# ============================================================
# 1. BASIC EXAMPLE
# ============================================================

# Animal is the parent class.

class Animal:

    def eat(self):
        print("Animal is eating.")


# Dog inherits from Animal.

class Dog(Animal):

    def bark(self):
        print("Dog is barking.")


# Cat also inherits from Animal.

class Cat(Animal):

    def meow(self):
        print("Cat is meowing.")


# Create Dog object
dog = Dog()

# Create Cat object
cat = Cat()


# Dog can access the parent method
dog.eat()

# Dog's own method
dog.bark()


# Cat can also access the parent method
cat.eat()

# Cat's own method
cat.meow()


# ============================================================
# 2. REAL-WORLD EXAMPLE
# ============================================================

# Employee is the parent class.

class Employee:

    def work(self):
        print("Employee is working.")


# Developer inherits from Employee.

class Developer(Employee):

    def code(self):
        print("Developer is coding.")


# Manager also inherits from Employee.

class Manager(Employee):

    def manage(self):
        print("Manager is managing the team.")


# Create Developer object
developer = Developer()

# Create Manager object
manager = Manager()


# Developer uses inherited method
developer.work()

# Developer's own method
developer.code()


# Manager uses inherited method
manager.work()

# Manager's own method
manager.manage()


# ============================================================
# 3. CONSTRUCTOR EXAMPLE
# ============================================================

# Person is the parent class.

class Person:

    def __init__(self, name):
        self.name = name


# Student inherits from Person.

class Student(Person):

    def study(self):
        print(f"{self.name} is studying.")


# Teacher also inherits from Person.

class Teacher(Person):

    def teach(self):
        print(f"{self.name} is teaching.")


# Create Student object
student = Student("Rahul")

# Create Teacher object
teacher = Teacher("Jaya")


# Student uses inherited name
student.study()

# Teacher uses inherited name
teacher.teach()


# ============================================================
# INHERITANCE FLOW
# ============================================================

#              Person
#              /    \
#             /      \
#        Student    Teacher
#
#
# Student inherits from Person.
#
# Teacher inherits from Person.
#
# Both child classes can use the
# attributes and methods of Person.


# ============================================================
# 4. KEY POINT
# ============================================================

# Hierarchical inheritance:
#
# One parent → Multiple child classes
#
#
# Example:
#
#              Employee
#              /      \
#             /        \
#       Developer     Manager
#
#
# Both Developer and Manager inherit
# from the same Employee class.


# ============================================================
# 5. PRACTICE
# ============================================================

# Create a class Vehicle:
#
# Method:
# - start()
#
#
# Create two child classes:
#
# Car:
# - drive()
#
# Bike:
# - ride()
#
#
# Create one Car object and one Bike object.
#
# Call:
#
# car.start()
# car.drive()
#
# bike.start()
# bike.ride()
#
#
# Expected output:
#
# Vehicle started.
# Car is driving.
# Vehicle started.
# Bike is riding.


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Hierarchical Inheritance lesson completed successfully!")
print("=" * 50)