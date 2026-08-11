# 04_Custom_Exceptions
# ============================================================
# 04_Custom_Exceptions.py
# Custom Exceptions in Python
# ============================================================

# Custom exceptions allow us to create
# our own error types.


# ============================================================
# 1. CREATE A CUSTOM EXCEPTION
# ============================================================

class AgeError(Exception):
    pass


try:
    age = 15

    if age < 18:
        raise AgeError(
            "Age must be 18 or above."
        )

except AgeError as error:
    print(f"Error: {error}")


# ============================================================
# 2. REAL-WORLD EXAMPLE - BANK ACCOUNT
# ============================================================

class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient balance."
        )

    return balance - amount


try:
    balance = withdraw(50000, 60000)

    print(balance)

except InsufficientBalanceError as error:
    print(f"Error: {error}")


# ============================================================
# 3. LOGIN EXAMPLE
# ============================================================

class LoginError(Exception):
    pass


def login(username, password):

    if username != "admin":
        raise LoginError(
            "Invalid username."
        )

    if password != "1234":
        raise LoginError(
            "Invalid password."
        )

    return "Login successful."


try:
    print(
        login("admin", "1234")
    )

except LoginError as error:
    print(f"Error: {error}")


# ============================================================
# KEY POINT
# ============================================================

# Custom exceptions are created by
# inheriting from the Exception class.
#
# Example:
#
# class MyError(Exception):
#     pass
#
#
# Custom exceptions make programs
# easier to understand and maintain.


# ============================================================
# 4. CUSTOM EXCEPTION WITH ADDITIONAL DATA
# ============================================================

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age

        super().__init__(
            f"Invalid age: {age}"
        )


try:
    age = -5

    if age < 0:
        raise InvalidAgeError(age)

except InvalidAgeError as error:
    print(f"Error: {error}")


# ============================================================
# 5. PRACTICE
# ============================================================

# Create a custom exception:
#
# InvalidMarksError
#
#
# Create a function:
#
# validate_marks(marks)
#
#
# If marks are:
#
# - Less than 0
# - Greater than 100
#
# Raise InvalidMarksError.
#
#
# Otherwise print:
#
# "Valid marks."


# ============================================================
# PRACTICE SOLUTION
# ============================================================

class InvalidMarksError(Exception):
    pass


def validate_marks(marks):

    if marks < 0 or marks > 100:
        raise InvalidMarksError(
            "Marks must be between 0 and 100."
        )

    print("Valid marks.")


# Valid marks
try:
    validate_marks(85)

except InvalidMarksError as error:
    print(f"Error: {error}")


# Invalid marks
try:
    validate_marks(120)

except InvalidMarksError as error:
    print(f"Error: {error}")


# ============================================================
# 6. REAL-WORLD STUDENT EXAMPLE
# ============================================================

class InvalidMarksError(Exception):
    pass


def calculate_grade(marks):

    if marks < 0 or marks > 100:
        raise InvalidMarksError(
            "Marks must be between 0 and 100."
        )

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 40:
        return "D"

    else:
        return "F"


try:
    marks = 92

    grade = calculate_grade(marks)

    print(
        f"Marks: {marks}"
    )

    print(
        f"Grade: {grade}"
    )

except InvalidMarksError as error:
    print(f"Error: {error}")


# ============================================================
# CUSTOM EXCEPTION FLOW
# ============================================================

#             Input
#                |
#          Validate Data
#                |
#        +-------+-------+
#        |               |
#      Valid           Invalid
#        |               |
#     Continue          raise
#                        |
#                Custom Exception
#                        |
#                     except
#                        |
#                  Handle Error


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Custom Exceptions lesson completed successfully!")
print("=" * 50)