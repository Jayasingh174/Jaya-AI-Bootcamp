
# 02_Variables.py

# Python Basics - Variables

# ============================================================

# 1. WHAT IS A VARIABLE?

# ============================================================

# A variable is a name used to store a value in Python.

name = "Jaya"
age = 25
salary = 75000

print(name)
print(age)
print(salary)

# ============================================================

# 2. VARIABLE ASSIGNMENT

# ============================================================

# The = operator is used for assignment.

student_name = "Alex"
student_age = 22
student_course = "Python"

print(student_name)
print(student_age)
print(student_course)

# ============================================================

# 3. VARIABLES CAN STORE DIFFERENT DATA TYPES

# ============================================================

name = "Jaya"          # String
age = 25               # Integer
height = 5.6           # Float
is_student = True      # Boolean

print(name)
print(age)
print(height)
print(is_student)

# ============================================================

# 4. VARIABLE VALUES CAN BE CHANGED

# ============================================================

age = 25

print("Before:", age)

age = 26

print("After:", age)

# ============================================================

# 5. MULTIPLE ASSIGNMENT

# ============================================================

# Python allows us to assign values to multiple variables

# in a single statement.

name, age, city = "Jaya", 25, "Ahmedabad"

print(name)
print(age)
print(city)

# ============================================================

# 6. ASSIGNING THE SAME VALUE TO MULTIPLE VARIABLES

# ============================================================

x = y = z = 100

print(x)
print(y)
print(z)

# ============================================================

# 7. SWAPPING VARIABLES

# ============================================================

# Python allows us to swap values without using a temporary

# variable.

first_name = "John"
last_name = "Smith"

print("Before swapping:")
print(first_name)
print(last_name)

first_name, last_name = last_name, first_name

print("After swapping:")
print(first_name)
print(last_name)

# ============================================================

# 8. VARIABLE NAMING RULES

# ============================================================

# Rule 1:

# Variable names can contain letters, numbers and underscore.

student_name = "Alex"
student_age = 21
student1 = "John"

# Rule 2:

# A variable name cannot start with a number.

# 1student = "Alex"     # INVALID

# Rule 3:

# Variable names cannot contain spaces.

# student name = "Alex" # INVALID

# Use underscore instead.

student_name = "Alex"

# Rule 4:

# Python variable names are case-sensitive.

name = "Jaya"
Name = "Alex"

print(name)
print(Name)

# Rule 5:

# Do not use Python keywords as variable names.

# class = "Python"      # INVALID

# if = 10               # INVALID

# for = 20              # INVALID

# Rule 6:

# Variable names should be meaningful.

# Bad:

x = 50000

# Better:

salary = 50000

# ============================================================

# 9. VALID VARIABLE NAMES

# ============================================================

name = "Jaya"
student_name = "Alex"
student_name1 = "John"
_age = 25
total_marks = 450

# ============================================================

# 10. INVALID VARIABLE NAMES

# ============================================================

# 1name = "Jaya"

# student-name = "Alex"

# student name = "John"

# class = "Python"

# ============================================================

# 11. PYTHON NAMING CONVENTION

# ============================================================

# Python commonly uses snake_case for variable names.

first_name = "Jaya"
last_name = "Patel"
date_of_birth = "2000-01-01"
total_marks = 500
average_score = 85.5

# ============================================================

# 12. CONSTANTS

# ============================================================

# Python does not have a true constant keyword.

#

# By convention, constants are written using UPPERCASE letters.

PI = 3.14159
MAX_USERS = 100
COMPANY_NAME = "JHEX"

print(PI)
print(MAX_USERS)
print(COMPANY_NAME)

# Python technically allows constants to be changed.

PI = 3.14

print(PI)

# However, developers should avoid changing constants.

# UPPERCASE tells other developers:

# "Treat this value as a constant."

# ============================================================

# 13. REAL-WORLD EXAMPLE - STUDENT

# ============================================================

student_name = "Rahul"
student_age = 21
student_course = "Artificial Intelligence"
student_score = 88.5

print("Student Name:", student_name)
print("Age:", student_age)
print("Course:", student_course)
print("Score:", student_score)

# ============================================================

# 14. REAL-WORLD EXAMPLE - E-COMMERCE

# ============================================================

product_name = "Laptop"
product_price = 85000
quantity = 2

total_price = product_price * quantity

print("Product:", product_name)
print("Price:", product_price)
print("Quantity:", quantity)
print("Total Price:", total_price)

# ============================================================

# 15. REAL-WORLD EXAMPLE - EMPLOYEE

# ============================================================

employee_name = "John"
employee_id = 101
department = "Artificial Intelligence"
monthly_salary = 7500

print("Employee Name:", employee_name)
print("Employee ID:", employee_id)
print("Department:", department)
print("Monthly Salary:", monthly_salary)

# ============================================================

# 16. REAL-WORLD EXAMPLE - AI APPLICATION

# ============================================================

model_name = "GPT"
temperature = 0.7
max_tokens = 1000
is_production = True

print("Model:", model_name)
print("Temperature:", temperature)
print("Max Tokens:", max_tokens)
print("Production:", is_production)

# ============================================================

# 17. VARIABLE TYPE CHECKING

# ============================================================

name = "Jaya"
age = 25
salary = 75000.50
is_employee = True

print(type(name))
print(type(age))
print(type(salary))
print(type(is_employee))

# ============================================================

# 18. PRACTICE

# ============================================================

# Create variables for a bank account.

account_holder = "Alex"
account_number = 123456
balance = 25000.50
is_active = True

print("Account Holder:", account_holder)
print("Account Number:", account_number)
print("Balance:", balance)
print("Active:", is_active)

# ============================================================

# 19. MINI CHALLENGE

# ============================================================

# Create variables for a shopping cart:

#

# product_name

# product_price

# quantity

# discount

#

# Calculate the final price.

product_name = "Headphones"
product_price = 5000
quantity = 2
discount = 10

total = product_price * quantity
discount_amount = total * discount / 100
final_price = total - discount_amount

print("Product:", product_name)
print("Total:", total)
print("Discount:", discount_amount)
print("Final Price:", final_price)

# ============================================================

# END

# ============================================================

print("Variables lesson completed successfully!")
