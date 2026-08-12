
# ============================================================
# 05_Class_Variables.py
# Class Variables in Python
# ============================================================


# ============================================================
# WHAT ARE CLASS VARIABLES?
# ============================================================

# Class variables are shared by all objects of a class.
#
# They are defined inside the class,
# but outside methods.
#
# Example:
#
# class Student:
#     school = "ABC School"
#
# Here, school is a class variable.


# ============================================================
# 1. BASIC EXAMPLE
# ============================================================

class Student:

    # Class variable
    school = "ABC School"

    def __init__(self, name):
        # Instance variable
        self.name = name


# Create two Student objects
student1 = Student("Jaya")
student2 = Student("Rahul")

# Access instance variables
print(student1.name)
print(student2.name)

# Access class variable
print(student1.school)
print(student2.school)


# ============================================================
# 2. CLASS VARIABLE IS SHARED
# ============================================================

class Employee:

    # Class variable
    company = "JHEX"

    def __init__(self, name):
        # Instance variable
        self.name = name


# Create two Employee objects
employee1 = Employee("Jaya")
employee2 = Employee("Alex")

# Both objects access the same class variable
print(employee1.company)
print(employee2.company)


# ============================================================
# 3. CHANGE CLASS VARIABLE
# ============================================================

# Change the class variable using the class name.
#
# This changes the value for all objects
# that are accessing the class variable.

Employee.company = "AI Technologies"

print(employee1.company)
print(employee2.company)


# ============================================================
# 4. INSTANCE VARIABLE VS CLASS VARIABLE
# ============================================================

class Car:

    # Class variable
    wheels = 4

    def __init__(self, brand):
        # Instance variable
        self.brand = brand


# Create two Car objects
car1 = Car("Toyota")
car2 = Car("BMW")

# brand is different for each object
print(car1.brand)
print(car2.brand)

# wheels is shared by the class
print(car1.wheels)
print(car2.wheels)


# brand  -> Instance variable
# wheels -> Class variable


# ============================================================
# 5. REAL-WORLD EXAMPLE - EMPLOYEE COUNT
# ============================================================

class Employee:

    # Class variables
    company = "JHEX"
    employee_count = 0

    def __init__(self, name):

        # Instance variable
        self.name = name

        # Increase the shared employee count
        # whenever a new Employee object is created.
        Employee.employee_count += 1


# Create Employee objects
employee1 = Employee("Jaya")
employee2 = Employee("Rahul")
employee3 = Employee("Alex")

# company is a class variable
print(employee1.company)
print(employee2.company)

# employee_count is shared by all Employee objects
print(
    f"Employees: {Employee.employee_count}"
)


# ============================================================
# KEY POINT
# ============================================================

# Instance variable:
# Different for each object.
#
# Example:
#
# employee1.name = "Jaya"
# employee2.name = "Rahul"
#
# Each object has its own name.


# Class variable:
# Shared by all objects.
#
# Example:
#
# Employee.company = "JHEX"
#
# All Employee objects can access the same company value.


# ============================================================
# 6. PRACTICE
# ============================================================

# Create a BankAccount class.
#
# Class variable:
#
# - bank_name = "ABC Bank"
#
# Instance variables:
#
# - owner
# - balance
#
# Create two accounts and print:
#
# 1. Bank name
# 2. Account owner
# 3. Account balance
#
#
# Example:
#
# class BankAccount:
#
#     bank_name = "ABC Bank"
#
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#
# account1 = BankAccount("Jaya", 50000)
# account2 = BankAccount("Rahul", 75000)
#
# print(account1.bank_name)
# print(account1.owner)
# print(account1.balance)
#
# print(account2.bank_name)
# print(account2.owner)
# print(account2.balance)


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Class Variables lesson completed successfully!")
print("=" * 50)
