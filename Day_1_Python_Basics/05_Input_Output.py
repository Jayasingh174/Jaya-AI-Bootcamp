# 05_Input_Output
# 05_Input_Output.py

# Python Basics - Input and Output

# ============================================================

# 1. OUTPUT USING print()

# ============================================================

# print() displays information on the screen.

print("Hello, Python!")
print("Welcome to AI Bootcamp!")
print(100)
print(25.5)

# ============================================================

# 2. PRINTING MULTIPLE VALUES

# ============================================================

name = "Jaya"
age = 25

print("Name:", name)
print("Age:", age)

print("Name:", name, "Age:", age)

# ============================================================

# 3. USER INPUT

# ============================================================

# input() is used to receive information from the user.

# Uncomment the following code to try it.

# name = input("Enter your name: ")

# print("Hello", name)

# ============================================================

# 4. INPUT IS ALWAYS A STRING

# ============================================================

# Important:

# input() always returns data as a string.

# age = input("Enter your age: ")

# print(age)

# print(type(age))

# ============================================================

# 5. CONVERTING INPUT TO INTEGER

# ============================================================

# If the user enters a number and we want to perform

# mathematical calculations, convert it to int.

# age = int(input("Enter your age: "))

# print("Your age is:", age)

# print("Next year you will be:", age + 1)

# ============================================================

# 6. CONVERTING INPUT TO FLOAT

# ============================================================

# Use float() when the user enters decimal numbers.

# price = float(input("Enter product price: "))

# print("Product Price:", price)

# print("Price with tax:", price * 1.18)

# ============================================================

# 7. STRING INPUT

# ============================================================

# String input does not require conversion.

# city = input("Enter your city: ")

# print("You live in:", city)

# ============================================================

# 8. BOOLEAN INPUT

# ============================================================

# input() returns a string, so this does NOT work as expected:

# is_student = bool(input("Are you a student? "))

# A better approach is to compare the user's input.

# answer = input("Are you a student? (yes/no): ")

# is_student = answer.lower() == "yes"

# print("Student:", is_student)

# ============================================================

# 9. MULTIPLE USER INPUTS

# ============================================================

# first_name = input("Enter first name: ")

# last_name = input("Enter last name: ")

# print("Full Name:", first_name, last_name)

# ============================================================

# 10. MULTIPLE VALUES IN ONE LINE

# ============================================================

# We can use split() to receive multiple values.

# first_name, last_name = input(

# "Enter first and last name: "

# ).split()

# print("First Name:", first_name)

# print("Last Name:", last_name)

# ============================================================

# 11. MULTIPLE NUMBERS IN ONE LINE

# ============================================================

# Convert each input value to integer.

# a, b, c = map(int, input(

# "Enter three numbers: "

# ).split())

# print("Sum:", a + b + c)

# ============================================================

# 12. OUTPUT USING sep

# ============================================================

# sep controls the separator between values.

print("Python", "Java", "C++")

print("Python", "Java", "C++", sep=" | ")

print("2026", "08", "11", sep="-")

# ============================================================

# 13. OUTPUT USING end

# ============================================================

# By default, print() moves to a new line.

print("Hello")
print("World")

# end changes this behavior.

print("Hello", end=" ")
print("World")

print("Python", end=" ---> ")
print("Programming")

# ============================================================

# 14. BASIC CALCULATOR

# ============================================================

# Uncomment this section to run the calculator.

# number1 = float(input("Enter first number: "))

# number2 = float(input("Enter second number: "))

# print("Addition:", number1 + number2)

# print("Subtraction:", number1 - number2)

# print("Multiplication:", number1 * number2)

# print("Division:", number1 / number2)

# ============================================================

# 15. STUDENT INFORMATION PROGRAM

# ============================================================

# name = input("Enter student name: ")

# age = int(input("Enter student age: "))

# course = input("Enter course: ")

# score = float(input("Enter score: "))

# print("\n----- Student Information -----")

# print("Name:", name)

# print("Age:", age)

# print("Course:", course)

# print("Score:", score)

# ============================================================

# 16. EMPLOYEE INFORMATION PROGRAM

# ============================================================

# employee_name = input("Enter employee name: ")

# employee_id = int(input("Enter employee ID: "))

# department = input("Enter department: ")

# salary = float(input("Enter salary: "))

# print("\n----- Employee Information -----")

# print("Name:", employee_name)

# print("Employee ID:", employee_id)

# print("Department:", department)

# print("Salary:", salary)

# ============================================================

# 17. SHOPPING BILL

# ============================================================

# product = input("Enter product name: ")

# price = float(input("Enter product price: "))

# quantity = int(input("Enter quantity: "))

# total = price * quantity

# print("\n----- Shopping Bill -----")

# print("Product:", product)

# print("Price:", price)

# print("Quantity:", quantity)

# print("Total:", total)

# ============================================================

# 18. USER INPUT + CALCULATION

# ============================================================

# length = float(input("Enter length: "))

# width = float(input("Enter width: "))

# area = length * width

# print("Area of rectangle:", area)

# ============================================================

# 19. TEMPERATURE CONVERTER

# ============================================================

# Celsius to Fahrenheit:

#

# Fahrenheit = (Celsius * 9/5) + 32

# celsius = float(input("Enter temperature in Celsius: "))

# fahrenheit = (celsius * 9 / 5) + 32

# print("Temperature in Fahrenheit:", fahrenheit)

# ============================================================

# 20. REAL-WORLD AI EXAMPLE

# ============================================================

# Ask the user for AI model configuration.

# model_name = input("Enter AI model name: ")

# temperature = float(input("Enter temperature: "))

# max_tokens = int(input("Enter maximum tokens: "))

# print("\n----- AI Configuration -----")

# print("Model:", model_name)

# print("Temperature:", temperature)

# print("Max Tokens:", max_tokens)

# ============================================================

# 21. PRACTICE PROGRAM

# ============================================================

# Create a simple bank account input program.

#

# Ask the user for:

# Account holder name

# Account number

# Initial balance

#

# Then display the account information.

# account_holder = input("Enter account holder name: ")

# account_number = input("Enter account number: ")

# balance = float(input("Enter account balance: "))

# print("\n----- Bank Account -----")

# print("Account Holder:", account_holder)

# print("Account Number:", account_number)

# print("Balance:", balance)

# ============================================================

# 22. MINI CHALLENGE

# ============================================================

# Create a simple shopping calculator.

#

# Ask the user for:

# 1. Product name

# 2. Product price

# 3. Quantity

# 4. Discount percentage

#

# Calculate:

# Total price

# Discount amount

# Final price

# product_name = input("Enter product name: ")

# product_price = float(input("Enter product price: "))

# quantity = int(input("Enter quantity: "))

# discount = float(input("Enter discount percentage: "))

# total_price = product_price * quantity

# discount_amount = total_price * discount / 100

# final_price = total_price - discount_amount

# print("\n========== BILL ==========")

# print("Product:", product_name)

# print("Price:", product_price)

# print("Quantity:", quantity)

# print("Total:", total_price)

# print("Discount:", discount_amount)

# print("Final Price:", final_price)

# ============================================================

# 23. IMPORTANT CONCEPT

# ============================================================

# Remember:

#

# input() -> always returns str

#

# int(input()) -> integer

#

# float(input()) -> floating-point number

#

# input().lower() -> lowercase string

#

# input().split() -> multiple values

# ============================================================

# END

# ============================================================

print("Input and Output lesson completed successfully!")
