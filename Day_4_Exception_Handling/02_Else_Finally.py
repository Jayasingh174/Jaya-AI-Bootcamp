
# ============================================================
# 02_Else_Finally.py
# Else and Finally in Exception Handling
# ============================================================


# ============================================================
# 1. TRY + EXCEPT + ELSE
# ============================================================

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print(f"You entered: {number}")


# else runs only when there is NO error.


# ============================================================
# 2. TRY + EXCEPT + FINALLY
# ============================================================

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

finally:
    print("Program finished.")


# finally always runs.


# ============================================================
# 3. DIVISION EXAMPLE
# ============================================================

try:
    a = 10
    b = 2

    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print(f"Result: {result}")

finally:
    print("Calculation completed.")


# ============================================================
# 4. REAL-WORLD EXAMPLE - FILE HANDLING
# ============================================================

try:
    file = open("data.txt", "r")
    data = file.read()

except FileNotFoundError:
    print("File not found.")

else:
    print(data)

finally:
    print("File operation completed.")


# ============================================================
# KEY POINT
# ============================================================

# try:
# Code that may cause an error.
#
# except:
# Handles the error.
#
# else:
# Runs when there is NO error.
#
# finally:
# Always runs.


# ============================================================
# EXCEPTION HANDLING FLOW
# ============================================================

#                  try
#                   |
#          +--------+--------+
#          |                 |
#       Error             No Error
#          |                 |
#       except             else
#          |                 |
#          +--------+--------+
#                   |
#                finally
#                   |
#              Program End


# ============================================================
# 5. PRACTICE
# ============================================================

# Create a program that:
#
# 1. Takes two numbers.
#
# 2. Divides them.
#
# 3. Handles ZeroDivisionError.
#
# 4. Uses else to print the result.
#
# 5. Uses finally to print:
#
# "Calculation completed."


# ============================================================
# PRACTICE SOLUTION
# ============================================================

try:
    first_number = float(
        input("Enter first number: ")
    )

    second_number = float(
        input("Enter second number: ")
    )

    result = first_number / second_number

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print(f"Result: {result}")

finally:
    print("Calculation completed.")


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Else and Finally lesson completed successfully!")
print("=" * 50)
