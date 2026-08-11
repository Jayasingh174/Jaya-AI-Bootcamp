# 01_Classes
# ============================================================
# 01_Classes.py
# Classes in Python
# ============================================================


# ============================================================
# 1. BASIC CLASS
# ============================================================

# A class is a blueprint for creating objects.
#
# Here, Student is a class.
# The show() method displays a message.


class Student:

    def show(self):
        print("This is a student.")


# Creating an object of the Student class
student1 = Student()

# Calling the method using the object
student1.show()


# ============================================================
# 2. CLASS WITH ATTRIBUTES
# ============================================================

# A class can contain attributes and methods.
#
# Attributes store data.
# Methods define behavior.


class Employee:

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: ₹{self.salary}")


# Creating the first Employee object
employee1 = Employee()

# Adding attributes to the object
employee1.name = "Jaya"
employee1.salary = 90000

# Calling the method
employee1.show_details()


# ============================================================
# 3. MULTIPLE OBJECTS
# ============================================================

# We can create multiple objects
# from the same class.

employee2 = Employee()

employee2.name = "Rahul"
employee2.salary = 80000

employee2.show_details()


# ============================================================
# 4. CALCULATOR EXAMPLE
# ============================================================

# A class can contain multiple methods.
#
# Here, Calculator provides methods for
# addition and multiplication.


class Calculator:

    # Add two numbers
    def add(self, a, b):
        return a + b

    # Multiply two numbers
    def multiply(self, a, b):
        return a * b


# Create Calculator object
calculator = Calculator()

# Call the add() method
print(calculator.add(10, 20))

# Call the multiply() method
print(calculator.multiply(10, 20))


# ============================================================
# 5. REAL-WORLD EXAMPLE - BANK ACCOUNT
# ============================================================

# Classes are commonly used to represent
# real-world entities.
#
# BankAccount is an example of a real-world class.


class BankAccount:

    # Deposit money into the account
    def deposit(self, amount):
        self.balance += amount

    # Display the current balance
    def show_balance(self):
        print(f"Balance: ₹{self.balance}")


# Create a BankAccount object
account = BankAccount()

# Set the initial account balance
account.balance = 50000

# Deposit money
account.deposit(10000)

# Display balance
account.show_balance()


# ============================================================
# 6. PRACTICE
# ============================================================

# Create a Car class with:
#
# - brand
# - model
# - price
# - show_details() method
#
# Example:
#
# class Car:
#
#     def show_details(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Price: ₹{self.price}")
#
#
# Create a Car object and assign:
#
# brand = "Toyota"
# model = "Camry"
# price = 3500000
#
# Then call show_details()


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Classes lesson completed successfully!")
print("=" * 50)