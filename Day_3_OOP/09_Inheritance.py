# 09_Inheritance
# ============================================================
# 09_Inheritance.py
# Inheritance in Python
# ============================================================


# ============================================================
# WHAT IS INHERITANCE?
# ============================================================

# Inheritance allows a child class to reuse
# code from a parent class.
#
# Parent Class  -> Base Class
# Child Class   -> Derived Class
#
# The child class can access methods and
# attributes from the parent class.


# ============================================================
# 1. BASIC INHERITANCE
# ============================================================

# Animal is the parent class.


class Animal:

    def eat(self):
        print("Animal is eating.")


# Dog inherits from Animal.
#
# Dog can use the eat() method
# even though eat() is defined in Animal.


class Dog(Animal):

    def bark(self):
        print("Dog is barking.")


# Create Dog object
dog = Dog()

# Method inherited from Animal
dog.eat()

# Method defined inside Dog
dog.bark()


# ============================================================
# 2. PARENT + CHILD
# ============================================================

class Person:

    def introduce(self):
        print("I am a person.")


# Employee inherits from Person.


class Employee(Person):

    def work(self):
        print("I am working.")


# Create Employee object
employee = Employee()

# Inherited method
employee.introduce()

# Employee's own method
employee.work()


# ============================================================
# 3. CONSTRUCTOR INHERITANCE
# ============================================================

# The parent class has a constructor.
#
# The child class can use the parent's constructor
# if the child class does not define its own __init__().


class Person:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")


# Student inherits from Person.
#
# Student does not define __init__(),
# so it uses Person's constructor.


class Student(Person):

    def study(self):
        print(f"{self.name} is studying.")


# Create Student object
student = Student("Jaya")

# Method inherited from Person
student.show_name()

# Method defined in Student
student.study()


# ============================================================
# 4. REAL-WORLD EXAMPLE - VEHICLE
# ============================================================

# Vehicle is the parent class.


class Vehicle:

    def start(self):
        print("Vehicle started.")


# Car inherits from Vehicle.


class Car(Vehicle):

    def drive(self):
        print("Car is driving.")


# Create Car object
car = Car()

# Inherited method
car.start()

# Car's own method
car.drive()


# ============================================================
# 5. USING super()
# ============================================================

# super() is used to access methods or
# the constructor of the parent class.
#
# Here, Manager inherits from Employee.
#
# Manager uses super().__init__(name)
# to call the Employee constructor.


class Employee:

    def __init__(self, name):
        self.name = name


class Manager(Employee):

    def __init__(self, name, department):

        # Call the parent class constructor
        super().__init__(name)

        # Manager's own instance variable
        self.department = department

    def show(self):

        print(f"Name: {self.name}")
        print(f"Department: {self.department}")


# Create Manager object
manager = Manager("Jaya", "AI")

# Display manager details
manager.show()


# ============================================================
# KEY POINT
# ============================================================

# Parent Class → Base Class
#
# Child Class  → Derived Class
#
#
# Inheritance allows a child class to:
#
# - Reuse parent methods
# - Reuse parent attributes
# - Add new methods
# - Add new attributes
# - Override parent methods
#
#
# Example:
#
# class Dog(Animal):
#
# Dog can use methods from Animal.


# ============================================================
# 6. PRACTICE
# ============================================================

# Create a class Person:
#
# Instance variable:
# - name
#
# Method:
# - show_name()
#
#
# Create a class Teacher(Person):
#
# Instance variable:
# - subject
#
# Method:
# - teach()
#
#
# Create a Teacher object and display:
#
# - Name
# - Subject
#
#
# Example structure:
#
# class Person:
#
#     def __init__(self, name):
#         self.name = name
#
#     def show_name(self):
#         print(f"Name: {self.name}")
#
#
# class Teacher(Person):
#
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#
#     def teach(self):
#         print(f"{self.name} teaches {self.subject}.")
#
#
# teacher = Teacher("Jaya", "Python")
#
# teacher.show_name()
# teacher.teach()


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Inheritance lesson completed successfully!")
print("=" * 50)