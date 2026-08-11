# 08_Static_Methods
# ============================================================
# 08_Static_Methods.py
# Static Methods in Python
# ============================================================


# ============================================================
# WHAT ARE STATIC METHODS?
# ============================================================

# A static method does not use:
#
# - self
# - cls
#
# It belongs to the class but does not need
# object data or class data.
#
# Static methods are defined using:
#
# @staticmethod


# ============================================================
# 1. BASIC EXAMPLE
# ============================================================

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


# Call the static method using the class name
print(Calculator.add(10, 20))


# ============================================================
# 2. MULTIPLE STATIC METHODS
# ============================================================

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def square(number):
        return number ** 2


# Call static methods using the class name
print(Calculator.add(10, 5))
print(Calculator.multiply(10, 5))
print(Calculator.square(5))


# ============================================================
# 3. STATIC METHOD WITH OBJECT
# ============================================================

# A static method can also be called using an object.
#
# However, it does not receive self automatically.


class Math:

    @staticmethod
    def is_even(number):
        return number % 2 == 0


# Create an object
math = Math()

# Call the static method using the object
print(math.is_even(10))
print(math.is_even(7))


# ============================================================
# 4. REAL-WORLD EXAMPLE - EMAIL VALIDATION
# ============================================================

# Static methods are useful for utility functions
# that do not need object or class data.


class User:

    @staticmethod
    def validate_email(email):
        return "@" in email


# Test email validation
print(User.validate_email("jaya@gmail.com"))
print(User.validate_email("jaya"))


# ============================================================
# 5. REAL-WORLD EXAMPLE - TEMPERATURE CONVERSION
# ============================================================

class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32


# Convert Celsius to Fahrenheit
print(
    Temperature.celsius_to_fahrenheit(25)
)


# ============================================================
# KEY POINT
# ============================================================

# Instance Method → self
#
# Class Method    → cls
#
# Static Method   → no self / cls
#
#
# Instance method:
#
# def method(self):
#     ...
#
#
# Class method:
#
# @classmethod
# def method(cls):
#     ...
#
#
# Static method:
#
# @staticmethod
# def method():
#     ...


# ============================================================
# WHEN TO USE STATIC METHODS
# ============================================================

# Use static methods when a function:
#
# - Does not need object data
# - Does not need class data
# - Performs an independent utility operation
#
#
# Common examples:
#
# - Validation
# - Calculations
# - Conversions
# - Formatting
# - Utility functions


# ============================================================
# 6. PRACTICE
# ============================================================

# Create a class called Validator.
#
# Add the following static methods:
#
# 1. is_positive(number)
#    - Return True if the number is positive.
#
# 2. is_even(number)
#    - Return True if the number is even.
#
# 3. is_email(email)
#    - Return True if the email contains "@"
#
#
# Example structure:
#
# class Validator:
#
#     @staticmethod
#     def is_positive(number):
#         return number > 0
#
#     @staticmethod
#     def is_even(number):
#         return number % 2 == 0
#
#     @staticmethod
#     def is_email(email):
#         return "@" in email
#
#
# Test the methods:
#
# print(Validator.is_positive(10))
# print(Validator.is_positive(-5))
#
# print(Validator.is_even(10))
# print(Validator.is_even(7))
#
# print(Validator.is_email("jaya@gmail.com"))
# print(Validator.is_email("jaya"))


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Static Methods lesson completed successfully!")
print("=" * 50)