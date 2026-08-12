
# ============================================================
# 03_Constructors.py
# Constructors in Python
# ============================================================


# ============================================================
# 1. BASIC CONSTRUCTOR
# ============================================================

# A constructor is a special method that runs automatically
# when an object is created.
#
# In Python, the constructor is:
#
# __init__()
#
# It is commonly used to initialize object attributes.


class Student:

    def __init__(self, name, age):
        # Store the values inside the object
        self.name = name
        self.age = age

    def show(self):
        # Display student information
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Create a Student object
student1 = Student("Jaya", 25)

# Display student details
student1.show()


# ============================================================
# 2. MULTIPLE OBJECTS
# ============================================================

# We can create multiple objects from the same class.
#
# Each object can have different attribute values.

student2 = Student("Rahul", 23)

student2.show()


# ============================================================
# 3. CONSTRUCTOR WITH MORE DATA
# ============================================================

# A constructor can accept multiple parameters.
#
# Here, Employee stores:
# - name
# - role
# - salary


class Employee:

    def __init__(self, name, role, salary):
        # Initialize employee attributes
        self.name = name
        self.role = role
        self.salary = salary

    def show(self):
        # Display employee information
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Salary: ₹{self.salary}")


# Create an Employee object
employee = Employee(
    "Jaya",
    "AI Engineer",
    90000
)

# Display employee details
employee.show()


# ============================================================
# 4. DEFAULT VALUE
# ============================================================

# Constructor parameters can have default values.
#
# If color is not provided, "White" will be used.


class Car:

    def __init__(self, brand, color="White"):
        self.brand = brand
        self.color = color

    def show(self):
        print(f"{self.brand} - {self.color}")


# Color will use the default value "White"
car1 = Car("Toyota")

# Here, we provide a custom color
car2 = Car("BMW", "Black")

car1.show()
car2.show()


# ============================================================
# 5. REAL-WORLD EXAMPLE - BANK ACCOUNT
# ============================================================

# A BankAccount class can represent a real-world
# bank account.
#
# The constructor initializes:
# - owner
# - balance


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(
            f"{self.owner}: ₹{self.balance}"
        )


# Create a BankAccount object
account = BankAccount("Jaya", 50000)

# Display account balance
account.show_balance()


# ============================================================
# KEY POINT
# ============================================================

# __init__() runs automatically
# when an object is created.
#
# Example:
#
# student1 = Student("Jaya", 25)
#
# Python automatically calls:
#
# Student.__init__("Jaya", 25)
#
# The constructor is mainly used to initialize
# object attributes.


# ============================================================
# 6. PRACTICE
# ============================================================

# Create a Product class with a constructor.
#
# Store:
#
# - name
# - price
# - category
#
# Create two objects and display their details.
#
#
# Example:
#
# class Product:
#
#     def __init__(self, name, price, category):
#         self.name = name
#         self.price = price
#         self.category = category
#
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Price: ₹{self.price}")
#         print(f"Category: {self.category}")
#
#
# Then create two Product objects:
#
# product1 = Product(
#     "Laptop",
#     85000,
#     "Electronics"
# )
#
# product2 = Product(
#     "Mouse",
#     1500,
#     "Accessories"
# )
#
# product1.show_details()
# product2.show_details()


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Constructors lesson completed successfully!")
print("=" * 50)
