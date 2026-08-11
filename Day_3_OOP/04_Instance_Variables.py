# 04_Instance_Variables
# ============================================================
# 04_Instance_Variables.py
# Instance Variables in Python
# ============================================================


# ============================================================
# WHAT ARE INSTANCE VARIABLES?
# ============================================================

# Instance variables belong to each individual object.
#
# They are usually created using:
#
# self.variable_name
#
# Each object can have different values
# for its instance variables.


# ============================================================
# 1. BASIC EXAMPLE
# ============================================================

class Student:

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age


# Create two Student objects
student1 = Student("Jaya", 25)
student2 = Student("Rahul", 23)

# Access instance variables
print(student1.name)
print(student2.name)

# Each object has its own data.


# ============================================================
# 2. DIFFERENT VALUES
# ============================================================

class Employee:

    def __init__(self, name, salary):
        # Instance variables
        self.name = name
        self.salary = salary


# Create two Employee objects
employee1 = Employee("Jaya", 90000)
employee2 = Employee("Alex", 80000)

# Each employee has different values
print(employee1.name, employee1.salary)
print(employee2.name, employee2.salary)


# ============================================================
# 3. MODIFY INSTANCE VARIABLE
# ============================================================

# Change employee1's salary
employee1.salary = 95000

print(employee1.salary)

# employee2 is not affected
print(employee2.salary)


# ============================================================
# 4. REAL-WORLD EXAMPLE - BANK ACCOUNT
# ============================================================

# A BankAccount object has its own:
# - owner
# - balance
#
# These are instance variables.


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # Add money to the account balance
        self.balance += amount


# Create a bank account
account = BankAccount("Jaya", 50000)

# Deposit money
account.deposit(10000)

# Access instance variables
print(account.owner)
print(account.balance)


# ============================================================
# 5. CHECK OBJECT DATA
# ============================================================

# The __dict__ attribute shows the instance variables
# stored inside an object.


class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


# Create a Car object
car = Car("Toyota", "White")

# Display the object's instance variables
print(car.__dict__)


# ============================================================
# KEY POINT
# ============================================================

# Instance variables are different for every object.
#
# Example:
#
# employee1.salary = 95000
# employee2.salary = 80000
#
# Changing employee1.salary does not change
# employee2.salary.


# ============================================================
# 6. PRACTICE
# ============================================================

# Create a Product class.
#
# Instance variables:
#
# - name
# - price
# - quantity
#
# Create two Product objects
# and print their details.
#
#
# Example:
#
# class Product:
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Price: ₹{self.price}")
#         print(f"Quantity: {self.quantity}")
#
#
# Create two objects:
#
# product1 = Product(
#     "Laptop",
#     85000,
#     2
# )
#
# product2 = Product(
#     "Mouse",
#     1500,
#     5
# )
#
# product1.show_details()
# product2.show_details()


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Instance Variables lesson completed successfully!")
print("=" * 50)