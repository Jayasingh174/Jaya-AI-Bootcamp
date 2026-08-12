
# 08_All_Basics.py
# Python Basics - Complete Revision

#

# Topics Covered:

# 1. Comments

# 2. print()

# 3. Variables

# 4. Data Types

# 5. Operators

# 6. Input and Output

# 7. F-Strings

# 8. Type Casting

# ============================================================

# 1. COMMENTS

# ============================================================

# Comments explain what the code is doing.

# Python ignores comments during execution.

print("Welcome to Python Basics!")

# ============================================================

# 2. VARIABLES

# ============================================================

student_name = "Jaya"
student_age = 25
student_course = "AI Software Engineering"

print(student_name)
print(student_age)
print(student_course)

# ============================================================

# 3. DIFFERENT DATA TYPES

# ============================================================

name = "Alex"                  # str
age = 25                       # int
salary = 85000.50              # float
is_employee = True             # bool

skills = ["Python", "FastAPI", "AI"]    # list
coordinates = (10, 20)                  # tuple
unique_numbers = {1, 2, 3}              # set

employee = {
"id": 101,
"name": "Alex",
"department": "AI"
}                                        # dict

result = None                            # NoneType

print("\n========== DATA TYPES ==========")

print(f"Name: {name} -> {type(name)}")
print(f"Age: {age} -> {type(age)}")
print(f"Salary: {salary} -> {type(salary)}")
print(f"Employee: {is_employee} -> {type(is_employee)}")
print(f"Skills: {skills} -> {type(skills)}")
print(f"Coordinates: {coordinates} -> {type(coordinates)}")
print(f"Unique Numbers: {unique_numbers} -> {type(unique_numbers)}")
print(f"Employee: {employee} -> {type(employee)}")
print(f"Result: {result} -> {type(result)}")

# ============================================================

# 4. ARITHMETIC OPERATORS

# ============================================================

a = 20
b = 5

print("\n========== ARITHMETIC OPERATORS ==========")

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponent: {a ** b}")

# ============================================================

# 5. COMPARISON OPERATORS

# ============================================================

age = 25

print("\n========== COMPARISON OPERATORS ==========")

print(f"Age == 25: {age == 25}")
print(f"Age != 30: {age != 30}")
print(f"Age > 18: {age > 18}")
print(f"Age < 18: {age < 18}")
print(f"Age >= 21: {age >= 21}")
print(f"Age <= 25: {age <= 25}")

# ============================================================

# 6. LOGICAL OPERATORS

# ============================================================

age = 25
has_id = True

can_enter = age >= 18 and has_id

print("\n========== LOGICAL OPERATORS ==========")

print(f"Age >= 18 AND has ID: {can_enter}")

is_student = True
is_employee = False

can_access_course = is_student or is_employee

print(f"Student OR Employee: {can_access_course}")

is_logged_in = True

print(f"NOT logged in: {not is_logged_in}")

# ============================================================

# 7. ASSIGNMENT OPERATORS

# ============================================================

score = 100

print("\n========== ASSIGNMENT OPERATORS ==========")

print(f"Initial Score: {score}")

score += 10
print(f"After += 10: {score}")

score -= 20
print(f"After -= 20: {score}")

score *= 2
print(f"After *= 2: {score}")

score //= 2
print(f"After //= 2: {score}")

# ============================================================

# 8. MEMBERSHIP OPERATORS

# ============================================================

skills = ["Python", "FastAPI", "AI"]

print("\n========== MEMBERSHIP OPERATORS ==========")

print(f"'Python' in skills: {'Python' in skills}")
print(f"'Java' in skills: {'Java' in skills}")
print(f"'Java' not in skills: {'Java' not in skills}")

# ============================================================

# 9. IDENTITY OPERATORS

# ============================================================

value = None

print("\n========== IDENTITY OPERATORS ==========")

print(f"value is None: {value is None}")
print(f"value is not None: {value is not None}")

# ============================================================

# 10. STRING OPERATIONS

# ============================================================

first_name = "Jaya"
last_name = "Patel"

full_name = first_name + " " + last_name

print("\n========== STRING OPERATIONS ==========")

print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Full Name: {full_name}")
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")
print(f"Length: {len(full_name)}")

# ============================================================

# 11. F-STRINGS

# ============================================================

name = "Jaya"
age = 25
salary = 90000.5678

print("\n========== F-STRINGS ==========")

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"My salary is ₹{salary:,.2f}.")

# ============================================================

# 12. TYPE CASTING

# ============================================================

age_string = "25"
salary_string = "85000.50"

age = int(age_string)
salary = float(salary_string)

print("\n========== TYPE CASTING ==========")

print(f"Age: {age}")
print(f"Age Type: {type(age)}")

print(f"Salary: {salary}")
print(f"Salary Type: {type(salary)}")

# ============================================================

# 13. INPUT AND OUTPUT

# ============================================================

# Uncomment the following section to make the program

# interactive.

# user_name = input("Enter your name: ")

#

# print(f"Welcome, {user_name}!")

# ============================================================

# 14. INPUT WITH TYPE CASTING

# ============================================================

# Uncomment to run this section.

# user_age = int(input("Enter your age: "))

#

# print(f"You are {user_age} years old.")

# print(f"Next year you will be {user_age + 1}.")

# ============================================================

# 15. REAL-WORLD EXAMPLE - STUDENT

# ============================================================

student_name = "Rahul"

math_marks = 85
python_marks = 92
ai_marks = 88

total_marks = math_marks + python_marks + ai_marks
average_marks = total_marks / 3

print("\n========================================")
print("          STUDENT REPORT")
print("========================================")

print(f"Student Name : {student_name}")
print(f"Math         : {math_marks}")
print(f"Python       : {python_marks}")
print(f"AI           : {ai_marks}")
print(f"Total        : {total_marks}")
print(f"Average      : {average_marks:.2f}")

if average_marks >= 40:
    print("Result       : PASS")
else:
    print("Result       : FAIL")

# ============================================================

# 16. REAL-WORLD EXAMPLE - SHOPPING

# ============================================================

product_name = "Laptop"
product_price = 85000
quantity = 2
discount_percentage = 10

subtotal = product_price * quantity

discount_amount = (
subtotal * discount_percentage / 100
)

final_price = subtotal - discount_amount

print("\n========================================")
print("          SHOPPING BILL")
print("========================================")

print(f"Product       : {product_name}")
print(f"Price         : ₹{product_price:,.2f}")
print(f"Quantity      : {quantity}")
print(f"Subtotal      : ₹{subtotal:,.2f}")
print(f"Discount      : {discount_percentage}%")
print(f"Discount Amt   : ₹{discount_amount:,.2f}")
print(f"Final Price   : ₹{final_price:,.2f}")

# ============================================================

# 17. REAL-WORLD EXAMPLE - EMPLOYEE

# ============================================================

employee_name = "Alex"
employee_id = 101
department = "Artificial Intelligence"

basic_salary = 75000
bonus = 10000

total_salary = basic_salary + bonus

print("\n========================================")
print("          EMPLOYEE DETAILS")
print("========================================")

print(f"Name          : {employee_name}")
print(f"Employee ID   : {employee_id}")
print(f"Department    : {department}")
print(f"Basic Salary  : ₹{basic_salary:,.2f}")
print(f"Bonus         : ₹{bonus:,.2f}")
print(f"Total Salary  : ₹{total_salary:,.2f}")

# ============================================================

# 18. REAL-WORLD EXAMPLE - AI MODEL

# ============================================================

model_name = "GPT"
temperature = 0.7
max_tokens = 2000
is_production = True

print("\n========================================")
print("          AI MODEL CONFIG")
print("========================================")

print(f"Model         : {model_name}")
print(f"Temperature   : {temperature}")
print(f"Max Tokens    : {max_tokens:,}")
print(f"Production    : {is_production}")

# ============================================================

# 19. MINI CALCULATOR

# ============================================================

number1 = 50
number2 = 10

print("\n========================================")
print("          CALCULATOR")
print("========================================")

print(f"{number1} + {number2} = {number1 + number2}")
print(f"{number1} - {number2} = {number1 - number2}")
print(f"{number1} * {number2} = {number1 * number2}")
print(f"{number1} / {number2} = {number1 / number2}")

# ============================================================

# 20. MINI CHALLENGE - BANK ACCOUNT

# ============================================================

account_holder = "Alex"
account_number = 123456
initial_balance = 50000

deposit = 10000
withdrawal = 5000

balance = initial_balance + deposit - withdrawal

print("\n========================================")
print("          BANK ACCOUNT")
print("========================================")

print(f"Account Holder : {account_holder}")
print(f"Account Number : {account_number}")
print(f"Initial Balance: ₹{initial_balance:,.2f}")
print(f"Deposit        : ₹{deposit:,.2f}")
print(f"Withdrawal     : ₹{withdrawal:,.2f}")
print(f"Final Balance  : ₹{balance:,.2f}")

# ============================================================

# 21. FINAL REVISION

# ============================================================

# Python Basics includes:

# Comments

# print()

# Variables

# Data Types

# Operators

# Input / Output

# F-Strings

# Type Casting

# ============================================================

# DAY 1 COMPLETE

# ============================================================

print("\n" + "=" * 50)
print("DAY 1 - PYTHON BASICS COMPLETED!")
print("=" * 50)
