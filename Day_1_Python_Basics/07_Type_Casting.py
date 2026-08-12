
# 07_Type_Casting.py

# Python Basics - Type Casting

# ============================================================

# 1. WHAT IS TYPE CASTING?

# ============================================================

# Type casting means converting one data type into another.

# Common conversion functions:

#

# int()

# float()

# str()

# bool()

# ============================================================

# 2. CHECKING THE ORIGINAL DATA TYPE

# ============================================================

age = 25

print(age)
print(type(age))

# ============================================================

# 3. INTEGER TO FLOAT

# ============================================================

age = 25

age_float = float(age)

print("Original:", age)
print("Original Type:", type(age))

print("Converted:", age_float)
print("Converted Type:", type(age_float))

# ============================================================

# 4. FLOAT TO INTEGER

# ============================================================

price = 99.99

price_int = int(price)

print("Original:", price)
print("Converted:", price_int)

# Important:

# int() removes the decimal portion.

#

# 99.99 becomes 99.

#

# It does NOT round the number.

# ============================================================

# 5. INTEGER TO STRING

# ============================================================

employee_id = 101

employee_id_string = str(employee_id)

print(employee_id_string)
print(type(employee_id_string))

# ============================================================

# 6. STRING TO INTEGER

# ============================================================

age_string = "25"

print(age_string)
print(type(age_string))

age = int(age_string)

print(age)
print(type(age))

# ============================================================

# 7. STRING TO FLOAT

# ============================================================

price_string = "99.99"

price = float(price_string)

print(price)
print(type(price))

# ============================================================

# 8. FLOAT TO STRING

# ============================================================

salary = 75000.50

salary_string = str(salary)

print(salary_string)
print(type(salary_string))

# ============================================================

# 9. STRING TO BOOLEAN

# ============================================================

# Be careful when converting strings to bool.

print(bool("True"))
print(bool("False"))

# Both return True because both strings are non-empty.

# ============================================================

# 10. EMPTY STRING TO BOOLEAN

# ============================================================

empty_string = ""

print(bool(empty_string))

# An empty string is False.

# ============================================================

# 11. INTEGER TO BOOLEAN

# ============================================================

print(bool(1))
print(bool(10))
print(bool(-5))
print(bool(0))

# Any non-zero number -> True

# Zero -> False

# ============================================================

# 12. FLOAT TO BOOLEAN

# ============================================================

print(bool(10.5))
print(bool(0.0))

# ============================================================

# 13. BOOLEAN TO INTEGER

# ============================================================

print(int(True))
print(int(False))

# True  -> 1

# False -> 0

# ============================================================

# 14. BOOLEAN TO FLOAT

# ============================================================

print(float(True))
print(float(False))

# ============================================================

# 15. BOOLEAN TO STRING

# ============================================================

value = True

value_string = str(value)

print(value_string)
print(type(value_string))

# ============================================================

# 16. IMPLICIT TYPE CONVERSION

# ============================================================

# Python can automatically convert some values

# during calculations.

integer_number = 10
float_number = 5.5

result = integer_number + float_number

print(result)
print(type(result))

# Python automatically converts the integer into a float.

# ============================================================

# 17. EXPLICIT TYPE CONVERSION

# ============================================================

# When the programmer manually converts a value,

# it is called explicit type casting.

age = "25"

age = int(age)

print(age)
print(type(age))

# ============================================================

# 18. USER INPUT AND TYPE CASTING

# ============================================================

# input() always returns a string.

# age = input("Enter your age: ")

# print(type(age))

# Convert input to integer:

# age = int(input("Enter your age: "))

# print("Age:", age)

# print("Type:", type(age))

# ============================================================

# 19. USER INPUT - FLOAT

# ============================================================

# salary = float(input("Enter your salary: "))

# print("Salary:", salary)

# print("Type:", type(salary))

# ============================================================

# 20. USER INPUT - MULTIPLE INTEGERS

# ============================================================

# numbers = input("Enter three numbers: ").split()

# print(numbers)

# Convert each value to integer:

# a, b, c = map(int, input(

# "Enter three numbers: "

# ).split())

# print("Sum:", a + b + c)

# ============================================================

# 21. STRING + INTEGER ERROR

# ============================================================

# This causes an error:

# age = 25

# print("Age: " + age)

# Python does not automatically concatenate

# a string and an integer.

# Correct approach:

age = 25

print("Age: " + str(age))

# Or use an f-string:

print(f"Age: {age}")

# ============================================================

# 22. INVALID STRING TO INTEGER

# ============================================================

# This causes a ValueError:

# number = int("hello")

# "hello" cannot be converted into an integer.

# ============================================================

# 23. DECIMAL STRING TO INTEGER

# ============================================================

# This causes an error:

# number = int("10.5")

# Because "10.5" is not a valid integer string.

# Correct approach:

number = int(float("10.5"))

print(number)

# ============================================================

# 24. TYPE CASTING WITH LISTS

# ============================================================

numbers = ["10", "20", "30"]

print(numbers)

integer_numbers = list(map(int, numbers))

print(integer_numbers)

# ============================================================

# 25. TYPE CASTING WITH TUPLES

# ============================================================

numbers = (10, 20, 30)

numbers_list = list(numbers)

print(numbers_list)
print(type(numbers_list))

# ============================================================

# 26. TYPE CASTING WITH SETS

# ============================================================

numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)

print(unique_numbers)
print(type(unique_numbers))

# ============================================================

# 27. LIST TO TUPLE

# ============================================================

skills = ["Python", "FastAPI", "AI"]

skills_tuple = tuple(skills)

print(skills_tuple)
print(type(skills_tuple))

# ============================================================

# 28. TUPLE TO LIST

# ============================================================

coordinates = (10, 20, 30)

coordinates_list = list(coordinates)

print(coordinates_list)
print(type(coordinates_list))

# ============================================================

# 29. REAL-WORLD EXAMPLE - STUDENT

# ============================================================

student_name = "Rahul"
math_marks = "85"
python_marks = "90"
ai_marks = "88"

math_marks = int(math_marks)
python_marks = int(python_marks)
ai_marks = int(ai_marks)

total = math_marks + python_marks + ai_marks
average = total / 3

print("\n========== STUDENT RESULT ==========")

print(f"Student: {student_name}")
print(f"Math: {math_marks}")
print(f"Python: {python_marks}")
print(f"AI: {ai_marks}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")

# ============================================================

# 30. REAL-WORLD EXAMPLE - SHOPPING

# ============================================================

product_price = "2500.50"
quantity = "3"

product_price = float(product_price)
quantity = int(quantity)

total_price = product_price * quantity

print("\n========== SHOPPING ==========")

print(f"Price: ₹{product_price:,.2f}")
print(f"Quantity: {quantity}")
print(f"Total: ₹{total_price:,.2f}")

# ============================================================

# 31. REAL-WORLD EXAMPLE - EMPLOYEE

# ============================================================

employee_id = "101"
salary = "85000.50"

employee_id = int(employee_id)
salary = float(salary)

print("\n========== EMPLOYEE ==========")

print(f"Employee ID: {employee_id}")
print(f"Salary: ₹{salary:,.2f}")

# ============================================================

# 32. REAL-WORLD EXAMPLE - AI APPLICATION

# ============================================================

# Configuration values may arrive as strings from

# environment variables, configuration files, or APIs.

max_tokens = "2000"
temperature = "0.7"
is_production = "true"

max_tokens = int(max_tokens)
temperature = float(temperature)

print("\n========== AI CONFIGURATION ==========")

print(f"Max Tokens: {max_tokens}")
print(f"Temperature: {temperature}")
print(f"Production Value: {is_production}")

# ============================================================

# 33. CONVERTING TEXT TO BOOLEAN CORRECTLY

# ============================================================

value = "true"

is_production = value.lower() == "true"

print("Production:", is_production)
print(type(is_production))

# Another example:

value = "yes"

is_active = value.lower() == "yes"

print("Active:", is_active)

# ============================================================

# 34. PRACTICE

# ============================================================

# Assume the following values come from user input.

name = "Alex"
age = "23"
salary = "75000.50"

# Convert the values into appropriate types.

age = int(age)
salary = float(salary)

print("\n========== PRACTICE ==========")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Salary: ₹{salary:,.2f}")

print(type(name))
print(type(age))
print(type(salary))

# ============================================================

# 35. MINI CHALLENGE

# ============================================================

# You receive the following data as strings:

#

# product_price = "1500.75"

# quantity = "4"

# discount = "10"

#

# Convert them into appropriate types.

#

# Calculate:

# 1. Subtotal

# 2. Discount amount

# 3. Final price

product_price = "1500.75"
quantity = "4"
discount = "10"

product_price = float(product_price)
quantity = int(quantity)
discount = float(discount)

subtotal = product_price * quantity
discount_amount = subtotal * discount / 100
final_price = subtotal - discount_amount

print("\n========== MINI CHALLENGE ==========")

print(f"Product Price: ₹{product_price:,.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ₹{subtotal:,.2f}")
print(f"Discount: {discount:.2f}%")
print(f"Discount Amount: ₹{discount_amount:,.2f}")
print(f"Final Price: ₹{final_price:,.2f}")

# ============================================================

# 36. TYPE CASTING SUMMARY

# ============================================================

# String -> Integer

# int("25")

# String -> Float

# float("25.5")

# Integer -> String

# str(25)

# Integer -> Float

# float(25)

# Float -> Integer

# int(25.9)

# Float -> String

# str(25.9)

# Integer -> Boolean

# bool(1)

# Boolean -> Integer

# int(True)

# List -> Tuple

# tuple([1, 2, 3])

# Tuple -> List

# list((1, 2, 3))

# List -> Set

# set([1, 2, 2, 3])

# ============================================================

# END

# ============================================================

print("\nType Casting lesson completed successfully!")
