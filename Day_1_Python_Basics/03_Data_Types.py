# 03_Data_Types
# 03_Data_Types.py

# Python Basics - Data Types

# ============================================================

# 1. WHAT ARE DATA TYPES?

# ============================================================

# A data type tells Python what kind of value a variable contains.

name = "Jaya"
age = 25

print(name)
print(age)

# ============================================================

# 2. INTEGER (int)

# ============================================================

# int is used for whole numbers.

# It can be positive, negative, or zero.

age = 25
year = 2026
temperature = -5
score = 100

print(age)
print(year)
print(temperature)
print(score)

print(type(age))
print(type(year))

# ============================================================

# 3. FLOAT (float)

# ============================================================

# float is used for decimal numbers.

price = 99.99
height = 5.8
percentage = 85.5

print(price)
print(height)
print(percentage)

print(type(price))

# ============================================================

# 4. STRING (str)

# ============================================================

# A string is a sequence of characters.

# Strings can be written using:

# Single quotes

# Double quotes

# Triple quotes

name = "Jaya"
city = 'Ahmedabad'
message = """Welcome to Python!"""

print(name)
print(city)
print(message)

print(type(name))

# ============================================================

# 5. BOOLEAN (bool)

# ============================================================

# Boolean has only two possible values:

# True

# False

is_student = True
is_logged_in = False

print(is_student)
print(is_logged_in)

print(type(is_student))

# ============================================================

# 6. LIST

# ============================================================

# A list stores multiple values.

# Lists are ordered and mutable.

fruits = ["Apple", "Banana", "Mango"]

print(fruits)
print(type(fruits))

print(fruits[0])
print(fruits[1])
print(fruits[2])

# Lists can contain different data types.

student = ["Jaya", 25, 85.5, True]

print(student)

# Lists can be modified.

fruits.append("Orange")

print(fruits)

# ============================================================

# 7. TUPLE

# ============================================================

# A tuple stores multiple values.

# Tuples are ordered but immutable.

coordinates = (10, 20)

print(coordinates)
print(type(coordinates))

print(coordinates[0])
print(coordinates[1])

# ============================================================

# 8. SET

# ============================================================

# A set stores unique values.

# Sets are unordered and do not allow duplicates.

numbers = {10, 20, 30, 20, 10}

print(numbers)
print(type(numbers))

# Duplicate values are automatically removed.

# ============================================================

# 9. DICTIONARY

# ============================================================

# A dictionary stores data in key-value pairs.

student = {
"name": "Jaya",
"age": 25,
"course": "Python"
}

print(student)
print(type(student))

print(student["name"])
print(student["age"])
print(student["course"])

# ============================================================

# 10. NONE TYPE

# ============================================================

# None represents the absence of a value.

result = None

print(result)
print(type(result))

# ============================================================

# 11. CHECKING DATA TYPES

# ============================================================

name = "Jaya"
age = 25
salary = 75000.50
is_employee = True
skills = ["Python", "FastAPI", "AI"]

print(type(name))
print(type(age))
print(type(salary))
print(type(is_employee))
print(type(skills))

# ============================================================

# 12. MULTIPLE DATA TYPES

# ============================================================

person = {
"name": "Alex",
"age": 30,
"salary": 85000.50,
"is_employee": True,
"skills": ["Python", "SQL", "AI"]
}

print(person)

# ============================================================

# 13. MUTABLE VS IMMUTABLE

# ============================================================

# Mutable objects can be changed after creation.

#

# Examples:

# list

# dictionary

# set

# Immutable objects cannot be changed after creation.

#

# Examples:

# int

# float

# string

# tuple

# bool

# Mutable example

numbers = [10, 20, 30]

print(numbers)

numbers.append(40)

print(numbers)

# Immutable example

name = "Jaya"

print(name)

# A new string is created when we change the value.

name = "Alex"

print(name)

# ============================================================

# 14. TYPE CONVERSION - PREVIEW

# ============================================================

# Python allows us to convert values from one type to another.

age = "25"

print(age)
print(type(age))

age = int(age)

print(age)
print(type(age))

price = 100

price = float(price)

print(price)
print(type(price))

number = 500

number = str(number)

print(number)
print(type(number))

# ============================================================

# 15. REAL-WORLD EXAMPLE - STUDENT

# ============================================================

student_name = "Rahul"                 # str
student_age = 22                      # int
student_percentage = 88.5             # float
is_passed = True                      # bool
subjects = ["Python", "SQL", "AI"]     # list

print("Name:", student_name)
print("Age:", student_age)
print("Percentage:", student_percentage)
print("Passed:", is_passed)
print("Subjects:", subjects)

# ============================================================

# 16. REAL-WORLD EXAMPLE - E-COMMERCE

# ============================================================

product_name = "Laptop"               # str
product_price = 85000.00              # float
quantity = 2                           # int
is_available = True                    # bool
categories = ["Electronics", "Laptop"] # list

print("Product:", product_name)
print("Price:", product_price)
print("Quantity:", quantity)
print("Available:", is_available)
print("Categories:", categories)

# ============================================================

# 17. REAL-WORLD EXAMPLE - EMPLOYEE

# ============================================================

employee = {
"id": 101,
"name": "Jaya",
"department": "AI",
"salary": 90000.00,
"is_active": True
}

print("Employee ID:", employee["id"])
print("Employee Name:", employee["name"])
print("Department:", employee["department"])
print("Salary:", employee["salary"])
print("Active:", employee["is_active"])

# ============================================================

# 18. REAL-WORLD EXAMPLE - AI APPLICATION

# ============================================================

model_name = "GPT"
temperature = 0.7
max_tokens = 1000
supported_models = ["GPT", "Gemini", "Claude"]
model_config = {
"temperature": 0.7,
"max_tokens": 1000
}
is_production = False

print("Model:", model_name)
print("Temperature:", temperature)
print("Max Tokens:", max_tokens)
print("Supported Models:", supported_models)
print("Configuration:", model_config)
print("Production:", is_production)

# ============================================================

# 19. PRACTICE

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

# 20. MINI CHALLENGE

# ============================================================

# Create a product record using a dictionary.

#

# Store:

# product name

# price

# quantity

# availability

# categories

#

# Then print each value and its data type.

product = {
"name": "Wireless Mouse",
"price": 1500.50,
"quantity": 10,
"available": True,
"categories": ["Electronics", "Accessories"]
}

print("Product:", product)

print("Name:", product["name"])
print("Price:", product["price"])
print("Quantity:", product["quantity"])
print("Available:", product["available"])
print("Categories:", product["categories"])

print(type(product["name"]))
print(type(product["price"]))
print(type(product["quantity"]))
print(type(product["available"]))
print(type(product["categories"]))

# ============================================================

# END

# ============================================================

print("Data Types lesson completed successfully!")
