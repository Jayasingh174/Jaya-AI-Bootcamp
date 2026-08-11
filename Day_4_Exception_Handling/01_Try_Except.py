# 01_Try_Except
# ============================================================
# 01_Try_Except.py
# Try and Except in Python
# ============================================================

# Exception handling prevents
# the program from crashing unexpectedly.


# ============================================================
# 1. BASIC EXAMPLE
# ============================================================

try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Please enter a valid number.")


# ============================================================
# 2. DIVISION ERROR
# ============================================================

try:
    a = 10
    b = 0

    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")


# ============================================================
# 3. MULTIPLE EXCEPTIONS
# ============================================================

try:
    number = int(input("Enter number: "))
    result = 100 / number

    print(result)

except ValueError:
    print("Enter a valid number.")

except ZeroDivisionError:
    print("Number cannot be zero.")


# ============================================================
# 4. GENERAL EXCEPTION
# ============================================================

try:
    numbers = [10, 20, 30]

    print(numbers[5])

except Exception as error:
    print(f"Error: {error}")


# ============================================================
# 5. REAL-WORLD EXAMPLE
# ============================================================

try:
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You can register.")

    else:
        print("You must be 18 or older.")

except ValueError:
    print("Age must be a number.")


# ============================================================
# KEY POINT
# ============================================================

# try:
# Risky code that may cause an exception.
#
# except:
# Code used to handle the exception.


# ============================================================
# 6. PRACTICE
# ============================================================

# Ask the user for two numbers.
#
# Divide the first number
# by the second number.
#
# Handle:
#
# - ValueError
# - ZeroDivisionError


# ============================================================
# PRACTICE SOLUTION
# ============================================================

try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    result = first_number / second_number

    print(f"Result: {result}")

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Try and Except lesson completed successfully!")
print("=" * 50)