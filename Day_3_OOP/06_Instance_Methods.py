# 06_Instance_Methods
# ============================================================
# 06_Instance_Methods.py
# Instance Methods in Python
# ============================================================


# ============================================================
# WHAT ARE INSTANCE METHODS?
# ============================================================

# Instance methods work with object data.
#
# They use "self" as the first parameter.
#
# Instance methods can:
# - Access instance variables
# - Modify instance variables
# - Perform operations using object data


# ============================================================
# 1. BASIC EXAMPLE
# ============================================================

class Student:

    def __init__(self, name):
        # Instance variable
        self.name = name

    def show_name(self):
        # Access the instance variable using self
        print(f"Name: {self.name}")


# Create a Student object
student = Student("Jaya")

# Call the instance method
student.show_name()


# ============================================================
# 2. METHOD WITH PARAMETERS
# ============================================================

# Instance methods can also accept additional parameters.
#
# "self" refers to the current object.
# "a" and "b" are additional method parameters.


class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


# Create Calculator object
calculator = Calculator()

# Call the methods
print(calculator.add(10, 20))
print(calculator.multiply(10, 20))


# ============================================================
# 3. MODIFY INSTANCE DATA
# ============================================================

# Instance methods can modify instance variables.
#
# Here, deposit() changes the account balance.


class BankAccount:

    def __init__(self, balance):
        # Instance variable
        self.balance = balance

    def deposit(self, amount):
        # Modify the balance
        self.balance += amount

    def show_balance(self):
        # Display the current balance
        print(f"Balance: ₹{self.balance}")


# Create a BankAccount object
account = BankAccount(50000)

# Deposit money
account.deposit(10000)

# Display updated balance
account.show_balance()


# ============================================================
# 4. MULTIPLE INSTANCE METHODS
# ============================================================

# A class can contain multiple instance methods.
#
# Here:
# - increase_salary() modifies salary
# - show_details() displays employee information


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, amount):
        # Increase employee salary
        self.salary += amount

    def show_details(self):
        # Display employee details
        print(f"Name: {self.name}")
        print(f"Salary: ₹{self.salary}")


# Create an Employee object
employee = Employee("Jaya", 90000)

# Increase salary
employee.increase_salary(10000)

# Display updated details
employee.show_details()


# ============================================================
# 5. REAL-WORLD EXAMPLE - SHOPPING CART
# ============================================================

# A ShoppingCart object can maintain a list of items.
#
# Instance methods can add items and display the cart.


class ShoppingCart:

    def __init__(self):
        # Each ShoppingCart object gets its own list
        self.items = []

    def add_item(self, item):
        # Add an item to the cart
        self.items.append(item)

    def show_items(self):
        # Display all items
        print("Cart:", self.items)


# Create a ShoppingCart object
cart = ShoppingCart()

# Add products to the cart
cart.add_item("Laptop")
cart.add_item("Mouse")

# Display cart contents
cart.show_items()


# ============================================================
# KEY POINT
# ============================================================

# Instance method:
#
# - Uses self as the first parameter
# - Works with object data
# - Can access instance variables
# - Can modify instance variables
#
#
# Example:
#
# class Employee:
#
#     def increase_salary(self, amount):
#         self.salary += amount
#
#
# employee.increase_salary(10000)
#
# Here, self refers to the employee object.


# ============================================================
# 6. PRACTICE
# ============================================================

# Create a Student class.
#
# Instance variables:
#
# - name
# - marks
#
# Methods:
#
# - show_details()
# - add_marks()
# - calculate_average()
#
#
# Example structure:
#
# class Student:
#
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Marks: {self.marks}")
#
#     def add_marks(self, amount):
#         self.marks += amount
#
#     def calculate_average(self):
#         return self.marks / len(self.marks)
#
#
# NOTE:
# If "marks" is a single number, calculate_average()
# needs a different design. For example, you could store
# marks as a list:
#
# self.marks = marks
#
# Then:
#
# def calculate_average(self):
#     return sum(self.marks) / len(self.marks)
#
# Try implementing the class yourself.


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Instance Methods lesson completed successfully!")
print("=" * 50)