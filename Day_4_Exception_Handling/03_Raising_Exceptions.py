
# ============================================================
# 03_Raising_Exceptions.py
# Raising Exceptions in Python
# ============================================================

# raise is used to manually create an exception
# when a specific condition occurs.


# ============================================================
# 1. BASIC EXAMPLE
# ============================================================

age = 15

if age < 18:
    raise ValueError("Age must be 18 or above.")


# ============================================================
# NOTE
# ============================================================

# The code above will stop the program because
# the exception is not handled.
#
# To handle the exception, use try and except.


# ============================================================
# 2. RAISE WITH TRY-EXCEPT
# ============================================================

try:
    age = 15

    if age < 18:
        raise ValueError(
            "You must be 18 or older."
        )

except ValueError as error:
    print(error)


# ============================================================
# 3. REAL-WORLD EXAMPLE - BANK WITHDRAWAL
# ============================================================

def withdraw(balance, amount):

    # Amount must be positive.
    if amount <= 0:
        raise ValueError(
            "Amount must be positive."
        )

    # Amount cannot be greater than balance.
    if amount > balance:
        raise ValueError(
            "Insufficient balance."
        )

    return balance - amount


try:
    balance = withdraw(50000, 60000)

    print(balance)

except ValueError as error:
    print(f"Error: {error}")


# ============================================================
# 4. AI EXAMPLE - PROMPT VALIDATION
# ============================================================

def check_prompt(prompt):

    # Check whether the prompt is empty.
    if not prompt:
        raise ValueError(
            "Prompt cannot be empty."
        )

    return "Prompt accepted."


try:
    print(
        check_prompt("Explain Python.")
    )

except ValueError as error:
    print(error)


# ============================================================
# 5. MULTIPLE VALIDATION CHECKS
# ============================================================

def validate_age(age):

    if age < 0:
        raise ValueError(
            "Age cannot be negative."
        )

    if age > 120:
        raise ValueError(
            "Age must be 120 or below."
        )

    return "Valid age."


try:
    print(validate_age(25))

except ValueError as error:
    print(f"Error: {error}")


# ============================================================
# KEY POINT
# ============================================================

# raise → Manually creates an exception.
#
# Example:
#
# if condition:
#     raise ValueError("Error message")
#
#
# Common exceptions:
#
# ValueError
# TypeError
# ZeroDivisionError
# FileNotFoundError


# ============================================================
# RAISE + TRY/EXCEPT FLOW
# ============================================================

#             Function
#                 |
#           Check condition
#                 |
#          +------+------+
#          |             |
#       Valid          Invalid
#          |             |
#       Continue       raise
#                        |
#                      except
#                        |
#                   Handle error


# ============================================================
# 6. PRACTICE
# ============================================================

# Create a function called:
#
# validate_salary()
#
# Requirements:
#
# 1. Accept salary as a parameter.
#
# 2. If salary is less than 0:
#    raise ValueError
#
# 3. Otherwise print:
#
#    "Valid salary."
#
# 4. Test the function using try-except.


# ============================================================
# PRACTICE SOLUTION
# ============================================================

def validate_salary(salary):

    if salary < 0:
        raise ValueError(
            "Salary cannot be negative."
        )

    print("Valid salary.")


try:
    salary = 90000

    validate_salary(salary)

except ValueError as error:
    print(f"Error: {error}")


# ============================================================
# PRACTICE - INVALID SALARY
# ============================================================

try:
    salary = -5000

    validate_salary(salary)

except ValueError as error:
    print(f"Error: {error}")


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Raising Exceptions lesson completed successfully!")
print("=" * 50)
