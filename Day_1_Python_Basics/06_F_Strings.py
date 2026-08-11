# 06_F_Strings
# 06_F_Strings.py

# Python Basics - F-Strings

# ============================================================

# 1. WHAT IS AN F-STRING?

# ============================================================

# An f-string allows us to insert variables and expressions

# directly inside a string.

name = "Jaya"
age = 25

print(f"My name is {name}")
print(f"I am {age} years old")

# ============================================================

# 2. BASIC F-STRING SYNTAX

# ============================================================

# Syntax:

#

# f"Text {variable}"

name = "Alex"

message = f"Hello, {name}!"

print(message)

# ============================================================

# 3. MULTIPLE VARIABLES

# ============================================================

first_name = "Jaya"
last_name = "Patel"
age = 25

print(
f"My name is {first_name} {last_name} "
f"and I am {age} years old."
)

# ============================================================

# 4. F-STRINGS WITH DIFFERENT DATA TYPES

# ============================================================

name = "Jaya"
age = 25
salary = 75000.50
is_employee = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Salary: {salary}")
print(f"Employee: {is_employee}")

# ============================================================

# 5. EXPRESSIONS INSIDE F-STRINGS

# ============================================================

a = 10
b = 20

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")

# ============================================================

# 6. CALCULATIONS INSIDE F-STRINGS

# ============================================================

price = 1000
quantity = 3

print(f"Total price: {price * quantity}")

# ============================================================

# 7. USING FUNCTIONS INSIDE F-STRINGS

# ============================================================

name = "jaya"

print(f"Uppercase name: {name.upper()}")
print(f"Name length: {len(name)}")

# ============================================================

# 8. NUMBER FORMATTING

# ============================================================

price = 12345.6789

print(f"Price: {price:.2f}")

# .2f means:

# Display exactly 2 digits after the decimal point.

# ============================================================

# 9. FORMATTING DECIMAL VALUES

# ============================================================

number = 10.56789

print(f"{number:.1f}")
print(f"{number:.2f}")
print(f"{number:.3f}")
print(f"{number:.4f}")

# ============================================================

# 10. PERCENTAGE FORMATTING

# ============================================================

score = 0.875

print(f"Score: {score:.2%}")

# .2% converts 0.875 into:

# 87.50%

# ============================================================

# 11. COMMA NUMBER FORMATTING

# ============================================================

salary = 750000

print(f"Salary: {salary:,}")

# Output:

# Salary: 750,000

# ============================================================

# 12. CURRENCY FORMATTING

# ============================================================

price = 12500.50

print(f"Price: ${price:,.2f}")

# ============================================================

# 13. ALIGNMENT

# ============================================================

name = "Python"

print(f"|{name:<20}|")
print(f"|{name:>20}|")
print(f"|{name:^20}|")

# < = left align

# > = right align

# ^ = center align

# ============================================================

# 14. PADDING WITH ZEROS

# ============================================================

employee_id = 25

print(f"Employee ID: {employee_id:05}")

# Output:

# Employee ID: 00025

# ============================================================

# 15. DATE-LIKE FORMATTING

# ============================================================

year = 2026
month = 8
day = 11

print(f"Date: {year:04}-{month:02}-{day:02}")

# ============================================================

# 16. BOOLEAN VALUES

# ============================================================

is_logged_in = True
is_admin = False

print(f"Logged In: {is_logged_in}")
print(f"Admin: {is_admin}")

# ============================================================

# 17. F-STRING WITH LISTS

# ============================================================

skills = ["Python", "FastAPI", "AI"]

print(f"My skills are: {skills}")

print(f"First skill: {skills[0]}")

# ============================================================

# 18. F-STRING WITH DICTIONARIES

# ============================================================

student = {
"name": "Rahul",
"age": 22,
"course": "Python"
}

print(f"Student Name: {student['name']}")
print(f"Student Age: {student['age']}")
print(f"Course: {student['course']}")

# ============================================================

# 19. REAL-WORLD EXAMPLE - STUDENT REPORT

# ============================================================

student_name = "Rahul"
math_marks = 85
python_marks = 92
ai_marks = 88

total_marks = math_marks + python_marks + ai_marks
average = total_marks / 3

print("\n========== STUDENT REPORT ==========")

print(f"Student: {student_name}")
print(f"Math: {math_marks}")
print(f"Python: {python_marks}")
print(f"AI: {ai_marks}")
print(f"Total: {total_marks}")
print(f"Average: {average:.2f}")

# ============================================================

# 20. REAL-WORLD EXAMPLE - EMPLOYEE PAYSLIP

# ============================================================

employee_name = "Jaya"
employee_id = 101
basic_salary = 75000
bonus = 10000

total_salary = basic_salary + bonus

print("\n========== PAYSLIP ==========")

print(f"Employee: {employee_name}")
print(f"Employee ID: {employee_id:05}")
print(f"Basic Salary: ${basic_salary:,.2f}")
print(f"Bonus: ${bonus:,.2f}")
print(f"Total Salary: ${total_salary:,.2f}")

# ============================================================

# 21. REAL-WORLD EXAMPLE - SHOPPING BILL

# ============================================================

product = "Laptop"
price = 85000
quantity = 2
discount_percentage = 10

subtotal = price * quantity
discount = subtotal * discount_percentage / 100
final_price = subtotal - discount

print("\n========== SHOPPING BILL ==========")

print(f"Product: {product}")
print(f"Price: ₹{price:,.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ₹{subtotal:,.2f}")
print(f"Discount: {discount_percentage:.2f}%")
print(f"Discount Amount: ₹{discount:,.2f}")
print(f"Final Price: ₹{final_price:,.2f}")

# ============================================================

# 22. REAL-WORLD EXAMPLE - AI MODEL CONFIGURATION

# ============================================================

model_name = "GPT"
temperature = 0.7
max_tokens = 2000
is_production = True

print("\n========== AI MODEL CONFIGURATION ==========")

print(f"Model: {model_name}")
print(f"Temperature: {temperature:.1f}")
print(f"Max Tokens: {max_tokens:,}")
print(f"Production: {is_production}")

# ============================================================

# 23. F-STRING WITH CONDITIONAL EXPRESSION

# ============================================================

age = 22

print(
f"Status: {'Adult' if age >= 18 else 'Minor'}"
)

# ============================================================

# 24. REAL-WORLD RESULT

# ============================================================

marks = 85

result = "Pass" if marks >= 40 else "Fail"

print(f"Marks: {marks}")
print(f"Result: {result}")

# ============================================================

# 25. F-STRING WITH MULTIPLE EXPRESSIONS

# ============================================================

name = "Jaya"
age = 25
salary = 90000

print(
f"Name: {name} | "
f"Age: {age} | "
f"Salary: ₹{salary:,}"
)

# ============================================================

# 26. COMMON MISTAKE

# ============================================================

name = "Jaya"

# Without f:

print("My name is {name}")

# With f:

print(f"My name is {name}")

# The 'f' before the string is important.

# ============================================================

# 27. F-STRING VS STRING CONCATENATION

# ============================================================

name = "Jaya"
age = 25

# String concatenation requires conversion:

message = "My name is " + name + " and I am " + str(age)

print(message)

# F-string is cleaner:

message = f"My name is {name} and I am {age}"

print(message)

# ============================================================

# 28. PRACTICE

# ============================================================

# Create a student report using f-strings.

#

# Store:

# name

# age

# course

# score

# percentage

#

# Display the information neatly.

student_name = "Alex"
student_age = 23
course = "Artificial Intelligence"
score = 450
total = 500

percentage = score / total

print("\n========== STUDENT REPORT ==========")

print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"Course: {course}")
print(f"Score: {score}/{total}")
print(f"Percentage: {percentage:.2%}")

# ============================================================

# 29. MINI CHALLENGE

# ============================================================

# Create a professional invoice using f-strings.

#

# Product: Monitor

# Price: 15000

# Quantity: 2

# GST: 18%

#

# Calculate:

# 1. Subtotal

# 2. GST amount

# 3. Final amount

#

# Format the amounts with commas and 2 decimal places.

product_name = "Monitor"
product_price = 15000
quantity = 2
gst_rate = 18

subtotal = product_price * quantity
gst_amount = subtotal * gst_rate / 100
final_amount = subtotal + gst_amount

print("\n========== INVOICE ==========")

print(f"Product: {product_name}")
print(f"Price: ₹{product_price:,.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ₹{subtotal:,.2f}")
print(f"GST: {gst_rate:.2f}%")
print(f"GST Amount: ₹{gst_amount:,.2f}")
print(f"Final Amount: ₹{final_amount:,.2f}")

# ============================================================

# END

# ============================================================

print("\nF-Strings lesson completed successfully!")
