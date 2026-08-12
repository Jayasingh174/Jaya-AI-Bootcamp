
# ============================================================
# 03_Functions.py
# Python Control Flow - Functions
# ============================================================


# ============================================================
# 1. WHAT IS A FUNCTION?
# ============================================================

# A function is a reusable block of code that performs
# a specific task.

# Functions help us:
# - Avoid duplicate code
# - Organize programs
# - Improve readability
# - Reuse logic


# ============================================================
# 2. BASIC FUNCTION
# ============================================================

def greet():
    print("Hello, welcome to Python!")


# Calling the function
greet()
greet()


# ============================================================
# 3. FUNCTION WITH A PARAMETER
# ============================================================

def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Jaya")
greet_user("Rahul")
greet_user("Alex")


# ============================================================
# 4. PARAMETER VS ARGUMENT
# ============================================================

# Parameter:
# The variable defined inside the function definition.

def greet_person(name):
    print(f"Hello, {name}!")


# Argument:
# The actual value passed to the function.

greet_person("Jaya")


# ============================================================
# 5. MULTIPLE PARAMETERS
# ============================================================

def introduce(name, age, course):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")


introduce("Jaya", 25, "AI Engineering")


# ============================================================
# 6. RETURN VALUE
# ============================================================

def add(a, b):
    return a + b


result = add(10, 20)

print(f"Result: {result}")


# ============================================================
# 7. FUNCTION WITHOUT RETURN
# ============================================================

def print_message():
    print("Hello Python!")


result = print_message()

print(f"Returned value: {result}")

# A function without return automatically returns None.


# ============================================================
# 8. MULTIPLE RETURN VALUES
# ============================================================

def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


result = calculate(20, 5)

print(result)


# Unpacking the returned values

addition, subtraction, multiplication = calculate(20, 5)

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")


# ============================================================
# 9. DEFAULT PARAMETERS
# ============================================================

def greet(name="Guest"):
    print(f"Hello, {name}!")


greet("Jaya")
greet()


# ============================================================
# 10. DEFAULT PARAMETER - REAL WORLD
# ============================================================

def create_user(name, role="user"):
    print(f"Name: {name}")
    print(f"Role: {role}")


create_user("Jaya")
create_user("Admin", "administrator")


# ============================================================
# 11. KEYWORD ARGUMENTS
# ============================================================

def student_info(name, age, course):
    print(
        f"Name: {name}, "
        f"Age: {age}, "
        f"Course: {course}"
    )


student_info(
    name="Jaya",
    age=25,
    course="Python"
)

# Keyword arguments can be provided in any order.

student_info(
    course="AI",
    name="Rahul",
    age=23
)


# ============================================================
# 12. POSITIONAL ARGUMENTS
# ============================================================

def employee(name, department, salary):
    print(
        f"{name} works in {department} "
        f"and earns ₹{salary:,.2f}."
    )


employee("Jaya", "AI", 90000)


# ============================================================
# 13. MIXING POSITIONAL AND KEYWORD ARGUMENTS
# ============================================================

employee(
    "Jaya",
    department="AI",
    salary=90000
)


# ============================================================
# 14. *ARGS
# ============================================================

# *args allows a function to accept
# any number of positional arguments.

def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print(add_numbers(10))
print(add_numbers(10, 20))
print(add_numbers(10, 20, 30, 40))


# ============================================================
# 15. *ARGS - AVERAGE
# ============================================================

def calculate_average(*numbers):

    if not numbers:
        return 0

    total = sum(numbers)

    return total / len(numbers)


print(calculate_average(80, 90, 70))
print(calculate_average(85, 90, 95, 88))


# ============================================================
# 16. **KWARGS
# ============================================================

# **kwargs allows a function to accept
# any number of keyword arguments.

def show_details(**details):

    for key, value in details.items():
        print(f"{key}: {value}")


show_details(
    name="Jaya",
    age=25,
    course="AI"
)


# ============================================================
# 17. *ARGS AND **KWARGS TOGETHER
# ============================================================

def display_data(*args, **kwargs):

    print("Positional arguments:")

    for value in args:
        print(value)

    print("Keyword arguments:")

    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_data(
    10,
    20,
    30,
    name="Jaya",
    course="Python"
)


# ============================================================
# 18. DOCSTRINGS
# ============================================================

def calculate_square(number):
    """
    Return the square of a number.
    """
    return number ** 2


print(calculate_square(5))

print(calculate_square.__doc__)


# ============================================================
# 19. TYPE HINTS
# ============================================================

def add_numbers(a: int, b: int) -> int:
    return a + b


result = add_numbers(10, 20)

print(result)


# ============================================================
# 20. FUNCTION WITH STRING
# ============================================================

def format_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"

    return full_name.title()


name = format_name("jaya", "patel")

print(name)


# ============================================================
# 21. FUNCTION WITH CONDITIONAL LOGIC
# ============================================================

def check_age(age):

    if age >= 18:
        return "Adult"

    return "Minor"


print(check_age(25))
print(check_age(15))


# ============================================================
# 22. FUNCTION - EVEN OR ODD
# ============================================================

def is_even(number):
    return number % 2 == 0


print(is_even(10))
print(is_even(7))


# ============================================================
# 23. FUNCTION - MAXIMUM NUMBER
# ============================================================

def find_maximum(numbers):

    largest = numbers[0]

    for number in numbers:

        if number > largest:
            largest = number

    return largest


numbers = [10, 50, 25, 90, 40]

print(f"Largest: {find_maximum(numbers)}")


# ============================================================
# 24. FUNCTION - MINIMUM NUMBER
# ============================================================

def find_minimum(numbers):

    smallest = numbers[0]

    for number in numbers:

        if number < smallest:
            smallest = number

    return smallest


print(f"Smallest: {find_minimum(numbers)}")


# ============================================================
# 25. FUNCTION - COUNT VOWELS
# ============================================================

def count_vowels(text):

    vowels = "aeiou"

    count = 0

    for character in text.lower():

        if character in vowels:
            count += 1

    return count


print(
    f"Vowels: {count_vowels('Python Programming')}"
)


# ============================================================
# 26. FUNCTION - REVERSE STRING
# ============================================================

def reverse_string(text):
    return text[::-1]


print(reverse_string("Python"))


# ============================================================
# 27. FUNCTION - PALINDROME
# ============================================================

def is_palindrome(text):

    text = text.lower()

    return text == text[::-1]


print(is_palindrome("madam"))
print(is_palindrome("python"))


# ============================================================
# 28. FUNCTION - FACTORIAL
# ============================================================

def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


print(f"5! = {factorial(5)}")


# ============================================================
# 29. FUNCTION - SIMPLE CALCULATOR
# ============================================================

def calculator(a, b, operator):

    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":

        if b == 0:
            return "Cannot divide by zero."

        return a / b

    else:
        return "Invalid operator."


print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))


# ============================================================
# 30. FUNCTION - STUDENT GRADE
# ============================================================

def calculate_grade(marks):

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

    return "F"


print(calculate_grade(95))
print(calculate_grade(75))
print(calculate_grade(35))


# ============================================================
# 31. FUNCTION - STUDENT RESULT
# ============================================================

def student_result(name, marks):

    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    return {
        "name": name,
        "total": total,
        "average": average,
        "grade": grade
    }


result = student_result(
    "Jaya",
    [85, 90, 92]
)


print("\n========== STUDENT RESULT ==========")

print(f"Name: {result['name']}")
print(f"Total: {result['total']}")
print(f"Average: {result['average']:.2f}")
print(f"Grade: {result['grade']}")


# ============================================================
# 32. REAL-WORLD EXAMPLE - SHOPPING
# ============================================================

def calculate_discount(price, discount_percentage):

    discount = price * discount_percentage / 100

    return price - discount


final_price = calculate_discount(
    10000,
    10
)


print(
    f"Final Price: ₹{final_price:,.2f}"
)


# ============================================================
# 33. REAL-WORLD EXAMPLE - TAX CALCULATION
# ============================================================

def calculate_tax(amount, tax_rate=18):
    return amount * tax_rate / 100


tax = calculate_tax(50000)

print(f"Tax: ₹{tax:,.2f}")


# ============================================================
# 34. REAL-WORLD EXAMPLE - EMPLOYEE SALARY
# ============================================================

def calculate_salary(basic_salary, bonus):
    return basic_salary + bonus


salary = calculate_salary(
    75000,
    10000
)


print(
    f"Total Salary: ₹{salary:,.2f}"
)


# ============================================================
# 35. REAL-WORLD EXAMPLE - BANK ACCOUNT
# ============================================================

def deposit(balance, amount):

    if amount <= 0:
        return balance

    return balance + amount


def withdraw(balance, amount):

    if amount <= 0:
        return balance

    if amount > balance:
        print("Insufficient balance.")
        return balance

    return balance - amount


balance = 50000

balance = deposit(balance, 10000)
balance = withdraw(balance, 5000)


print(
    f"Final Balance: ₹{balance:,.2f}"
)


# ============================================================
# 36. REAL-WORLD EXAMPLE - AI TOKEN CALCULATOR
# ============================================================

def calculate_token_cost(tokens, price_per_1000):
    return (tokens / 1000) * price_per_1000


tokens = 5000
price_per_1000 = 0.002

cost = calculate_token_cost(
    tokens,
    price_per_1000
)


print("\n========== AI TOKEN COST ==========")

print(f"Tokens: {tokens:,}")
print(f"Cost: ${cost:.4f}")


# ============================================================
# 37. FUNCTION - AI REQUEST VALIDATION
# ============================================================

def validate_ai_request(
    user_type,
    tokens_requested
):

    if user_type == "premium":

        if tokens_requested <= 10000:
            return True

    elif user_type == "free":

        if tokens_requested <= 1000:
            return True

    return False


print(
    validate_ai_request("premium", 5000)
)

print(
    validate_ai_request("free", 5000)
)


# ============================================================
# 38. VARIABLE SCOPE - LOCAL VARIABLE
# ============================================================

def example_function():

    message = "Hello from function"

    print(message)


example_function()

# message cannot normally be accessed here because
# it is a local variable.


# ============================================================
# 39. GLOBAL VARIABLE
# ============================================================

company = "AI Technologies"


def show_company():
    print(company)


show_company()


# ============================================================
# 40. LOCAL VS GLOBAL
# ============================================================

name = "Global Jaya"


def show_name():

    name = "Local Jaya"

    print(name)


show_name()

print(name)


# ============================================================
# 41. GLOBAL KEYWORD
# ============================================================

counter = 0


def increment_counter():

    global counter

    counter += 1


increment_counter()
increment_counter()

print(f"Counter: {counter}")


# ============================================================
# 42. LAMBDA FUNCTION
# ============================================================

# A lambda is a small anonymous function.

square = lambda number: number ** 2

print(square(5))


# ============================================================
# 43. LAMBDA WITH SORTING
# ============================================================

students = [
    {"name": "Jaya", "score": 90},
    {"name": "Rahul", "score": 75},
    {"name": "Alex", "score": 85}
]


students.sort(
    key=lambda student: student["score"]
)


print(students)


# ============================================================
# 44. PRACTICE
# ============================================================

# Create a function that accepts a list of numbers
# and returns:
#
# total
# average
# maximum
# minimum


def analyze_numbers(numbers):

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


numbers = [10, 20, 30, 40, 50]

total, average, maximum, minimum = analyze_numbers(
    numbers
)


print("\n========== NUMBER ANALYSIS ==========")

print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")


# ============================================================
# 45. MINI CHALLENGE
# ============================================================

# Build a reusable employee evaluation system.
#
# Create a function:
#
# evaluate_employee(name, performance, experience)
#
# Rules:
#
# Performance >= 90 and experience >= 3
# -> "Excellent"
#
# Performance >= 75 and experience >= 2
# -> "Good"
#
# Performance >= 60
# -> "Average"
#
# Otherwise
# -> "Needs Improvement"


def evaluate_employee(
    name,
    performance,
    experience
):

    if performance >= 90 and experience >= 3:
        rating = "Excellent"

    elif performance >= 75 and experience >= 2:
        rating = "Good"

    elif performance >= 60:
        rating = "Average"

    else:
        rating = "Needs Improvement"

    return {
        "name": name,
        "performance": performance,
        "experience": experience,
        "rating": rating
    }


employee = evaluate_employee(
    "Jaya",
    92,
    4
)


print("\n========== EMPLOYEE EVALUATION ==========")

print(f"Name: {employee['name']}")
print(f"Performance: {employee['performance']}")
print(f"Experience: {employee['experience']} years")
print(f"Rating: {employee['rating']}")


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Functions lesson completed successfully!")
print("=" * 50)
