# 14_Method_Overriding
# ============================================================
# 14_Method_Overriding.py
# Method Overriding in Python
# ============================================================


# ============================================================
# WHAT IS METHOD OVERRIDING?
# ============================================================

# Method overriding means:
#
# A child class provides its own version
# of a method already defined in the parent class.
#
#
# Parent:
#     work()
#
# Child:
#     work()
#
#
# The child version overrides the
# parent version when called on a child object.


# ============================================================
# 1. BASIC EXAMPLE
# ============================================================

# Parent class

class Animal:

    def sound(self):
        print("Animal makes a sound.")


# Child class

class Dog(Animal):

    # This method overrides the
    # sound() method of Animal.

    def sound(self):
        print("Dog says Woof.")


# Create objects

animal = Animal()
dog = Dog()


# Parent version

animal.sound()

# Child version

dog.sound()


# ============================================================
# 2. REAL-WORLD EXAMPLE
# ============================================================

# Parent class

class Employee:

    def work(self):
        print("Employee is working.")


# Developer overrides work()

class Developer(Employee):

    def work(self):
        print("Developer is writing code.")


# Manager also overrides work()

class Manager(Employee):

    def work(self):
        print("Manager is managing the team.")


# Store different child objects
# in the same list.

employees = [
    Developer(),
    Manager()
]


# Same method call:
#
# employee.work()
#
# But each child class provides
# different behavior.

for employee in employees:
    employee.work()


# ============================================================
# 3. METHOD OVERRIDING USING super()
# ============================================================

# Parent class

class Person:

    def introduce(self):
        print("I am a person.")


# Child class

class Student(Person):

    def introduce(self):

        # Call the parent class method
        super().introduce()

        # Add child-specific behavior
        print("I am also a student.")


# Create Student object

student = Student()

student.introduce()


# ============================================================
# HOW super() WORKS
# ============================================================

# Without super():
#
# The child completely replaces
# the parent method.
#
#
# With super():
#
# The child can call the parent method
# and then add its own behavior.
#
#
# Example:
#
# Student.introduce()
#       ↓
# super().introduce()
#       ↓
# Person.introduce()
#       ↓
# Student's additional code


# ============================================================
# 4. REAL-WORLD AI EXAMPLE
# ============================================================

# Parent AI model

class AIModel:

    def generate(self):
        print("AI model generates a response.")


# ChatGPT overrides generate()

class ChatGPT(AIModel):

    def generate(self):
        print("ChatGPT generates a response.")


# Gemini overrides generate()

class Gemini(AIModel):

    def generate(self):
        print("Gemini generates a response.")


# Store different AI models
# in the same list.

models = [
    ChatGPT(),
    Gemini()
]


# Same method call
# but different behavior.

for model in models:
    model.generate()


# ============================================================
# 5. METHOD OVERRIDING WITH CONSTRUCTORS
# ============================================================

# Parent class

class PersonDetails:

    def __init__(self, name):
        self.name = name


# Child class overrides __init__()

class EmployeeDetails(PersonDetails):

    def __init__(self, name, salary):

        # Call the parent constructor
        super().__init__(name)

        # Add child-specific data
        self.salary = salary

    def show(self):
        print(f"Name: {self.name}")
        print(f"Salary: ₹{self.salary}")


# Create object

employee = EmployeeDetails(
    "Jaya",
    90000
)

employee.show()


# ============================================================
# KEY POINT
# ============================================================

# Method overriding occurs when:
#
# 1. A parent class has a method.
#
# 2. A child class defines a method
#    with the same name.
#
# 3. The child method provides
#    different behavior.
#
#
# Example:
#
# Parent:
#     work()
#
# Child:
#     work()
#
#
# The child's method overrides
# the parent's method.


# ============================================================
# METHOD OVERRIDING VS POLYMORPHISM
# ============================================================

# Method overriding is one common way
# to achieve polymorphic behavior.
#
#
# Example:
#
# Developer.work()
# Manager.work()
#
#
# Same method name:
#     work()
#
# Different behavior:
#     Developer → Writing code
#     Manager   → Managing team


# ============================================================
# 6. PRACTICE
# ============================================================

# Create a parent class:
#
# class Vehicle:
#
#     def start(self):
#         print("Vehicle is starting.")
#
#
# Create two child classes:
#
# class Car(Vehicle):
#
#     def start(self):
#         print("Car starts with a key.")
#
#
# class Bike(Vehicle):
#
#     def start(self):
#         print("Bike starts with a button.")
#
#
# Create objects:
#
# car = Car()
# bike = Bike()
#
#
# Call:
#
# car.start()
# bike.start()
#
#
# Expected output:
#
# Car starts with a key.
# Bike starts with a button.


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Method Overriding lesson completed successfully!")
print("=" * 50)
