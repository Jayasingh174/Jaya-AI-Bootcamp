# 05_Practice
# 05_Practice.py
#
# Day 4 - Exception Handling Practice
#
# Topics Covered:
# 1. try and except
# 2. Multiple exceptions
# 3. else and finally
# 4. raise
# 5. Custom exceptions
# 6. Exception handling with classes
#
# ============================================================
# 1. BASIC EXCEPTION HANDLING
# ============================================================

# try block contains code that may produce an error.
#
# If the user enters something that cannot be converted
# into an integer, Python will raise a ValueError.

try:

    number = int(input("Enter a number: "))

    print(f"Number: {number}")

# except handles the specific error.
#
# ValueError occurs when the input cannot be converted
# into an integer.

except ValueError:

    print("Please enter a valid number.")


# ============================================================
# 2. DIVISION
# ============================================================

# This example demonstrates:
#
# ValueError
# ZeroDivisionError
# else
# finally

try:

    # Take the first number from the user.
    a = int(input("Enter first number: "))

    # Take the second number from the user.
    b = int(input("Enter second number: "))

    # Perform division.
    #
    # This can cause ZeroDivisionError
    # if b is 0.

    result = a / b


# ValueError occurs when the user enters
# something that is not a valid integer.

except ValueError:

    print("Please enter numbers only.")


# ZeroDivisionError occurs when we try
# to divide a number by zero.

except ZeroDivisionError:

    print("Cannot divide by zero.")


# else runs only when the try block
# executes successfully without an exception.

else:

    print(f"Result: {result}")


# finally always runs whether an error
# occurs or not.

finally:

    print("Calculation completed.")


# ============================================================
# 3. RAISE EXCEPTION
# ============================================================

# The raise keyword is used to manually
# create an exception.
#
# Here we check whether a person is eligible
# based on their age.

def check_age(age):

    # If age is less than 18,
    # manually raise a ValueError.

    if age < 18:

        raise ValueError(
            "Age must be 18 or above."
        )

    # If the condition is valid,
    # return "Eligible".

    return "Eligible"


# Call the function inside try
# because it may raise an exception.

try:

    print(check_age(20))


# Handle the ValueError raised by
# the check_age() function.

except ValueError as error:

    print(error)


# ============================================================
# 4. CUSTOM EXCEPTION
# ============================================================

# A custom exception allows us to create
# our own meaningful error type.
#
# Custom exceptions are useful in real-world
# applications because they make errors
# easier to understand and handle.

class InsufficientBalanceError(Exception):

    pass


# Function to withdraw money from an account.

def withdraw(balance, amount):

    # Check whether the withdrawal amount
    # is greater than the available balance.

    if amount > balance:

        # Raise our custom exception.

        raise InsufficientBalanceError(
            "Insufficient balance."
        )

    # If enough balance is available,
    # return the remaining balance.

    return balance - amount


# Call withdraw() inside try because
# the function may raise a custom exception.

try:

    balance = withdraw(50000, 60000)

    print(f"Balance: ₹{balance}")


# Handle the custom exception.

except InsufficientBalanceError as error:

    print(f"Error: {error}")


# ============================================================
# 5. FINAL CHALLENGE
# ============================================================

# Create a Student class.
#
# Requirements:
#
# - name
# - marks
#
# Create a custom exception:
#
# InvalidMarksError
#
# If marks are:
#
# - Less than 0
# - Greater than 100
#
# Raise InvalidMarksError.
#
# Otherwise:
#
# Display the student details.


# ============================================================
# CUSTOM EXCEPTION: INVALID MARKS
# ============================================================

# Create our own exception for invalid marks.

class InvalidMarksError(Exception):

    pass


# ============================================================
# STUDENT CLASS
# ============================================================

class Student:

    # Constructor receives the student's
    # name and marks.

    def __init__(self, name, marks):

        # Validate the marks before storing them.

        if marks < 0 or marks > 100:

            # Raise our custom exception
            # if marks are outside the valid range.

            raise InvalidMarksError(
                "Marks must be between 0 and 100."
            )

        # Store the valid student name.

        self.name = name

        # Store the valid marks.

        self.marks = marks


    # ========================================================
    # SHOW STUDENT DETAILS
    # ========================================================

    def show(self):

        # Display student name.

        print(f"Name: {self.name}")

        # Display student marks.

        print(f"Marks: {self.marks}")


# ============================================================
# CREATE STUDENT OBJECT
# ============================================================

# Student creation is placed inside try
# because the constructor can raise
# InvalidMarksError.

try:

    student = Student("Jaya", 90)

    # Display student details.

    student.show()


# Handle invalid marks.

except InvalidMarksError as error:

    print(f"Error: {error}")


# ============================================================
# KEY CONCEPTS
# ============================================================

# try
# ----
# Contains code that may cause an exception.
#
#
# except
# ------
# Handles an exception.
#
#
# else
# ----
# Runs only when there is NO exception.
#
#
# finally
# -------
# Always runs whether an exception occurs or not.
#
#
# raise
# -----
# Manually creates an exception.
#
#
# Custom Exception
# ----------------
# Allows us to create our own meaningful
# exception classes.
#
# Example:
#
# class MyError(Exception):
#     pass


# ============================================================
# END
# ============================================================

print("\n" + "=" * 55)
print("Day 4 Exception Handling Practice Completed!")
print("=" * 55)
