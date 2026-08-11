# 05_Practice
# ============================================================
# 05_Practice.py
# Day 2 - Control Flow Practice
# Conditions + Loops + Functions + Data Structures
# ============================================================


# ============================================================
# PRACTICE 1 - EVEN AND ODD NUMBERS
# ============================================================

numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = []
odd_numbers = []

for number in numbers:

    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)


# ============================================================
# PRACTICE 2 - NUMBER ANALYSIS FUNCTION
# ============================================================

def analyze_numbers(numbers):

    total = sum(numbers)
    average = total / len(numbers)

    return {
        "total": total,
        "average": average,
        "maximum": max(numbers),
        "minimum": min(numbers)
    }


numbers = [10, 20, 30, 40, 50]

result = analyze_numbers(numbers)

print("\n========== NUMBER ANALYSIS ==========")

for key, value in result.items():
    print(f"{key}: {value}")


# ============================================================
# PRACTICE 3 - STUDENT GRADING SYSTEM
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

    else:
        return "F"


students = [
    {
        "name": "Jaya",
        "marks": 92
    },
    {
        "name": "Rahul",
        "marks": 78
    },
    {
        "name": "Alex",
        "marks": 65
    },
    {
        "name": "Priya",
        "marks": 35
    }
]

print("\n========== STUDENT GRADES ==========")

for student in students:

    grade = calculate_grade(student["marks"])

    print(
        f"{student['name']} | "
        f"Marks: {student['marks']} | "
        f"Grade: {grade}"
    )


# ============================================================
# PRACTICE 4 - PASS / FAIL
# ============================================================

def check_result(marks):

    if marks >= 40:
        return "Pass"

    return "Fail"


print("\n========== PASS / FAIL ==========")

for student in students:

    result = check_result(student["marks"])

    print(
        f"{student['name']}: {result}"
    )


# ============================================================
# PRACTICE 5 - FIND HIGHEST MARKS
# ============================================================

highest_student = students[0]

for student in students:

    if student["marks"] > highest_student["marks"]:
        highest_student = student


print("\n========== TOP STUDENT ==========")

print(
    f"Name: {highest_student['name']}"
)

print(
    f"Marks: {highest_student['marks']}"
)


# ============================================================
# PRACTICE 6 - SHOPPING CART
# ============================================================

cart = [
    {
        "product": "Laptop",
        "price": 80000,
        "quantity": 1
    },
    {
        "product": "Mouse",
        "price": 1500,
        "quantity": 2
    },
    {
        "product": "Keyboard",
        "price": 2500,
        "quantity": 1
    }
]


def calculate_cart_total(cart):

    total = 0

    for item in cart:

        item_total = (
            item["price"] *
            item["quantity"]
        )

        total += item_total

    return total


cart_total = calculate_cart_total(cart)

print("\n========== SHOPPING CART ==========")

for item in cart:

    print(
        f"{item['product']} - "
        f"₹{item['price']:,.2f} x "
        f"{item['quantity']}"
    )

print(
    f"Total: ₹{cart_total:,.2f}"
)


# ============================================================
# PRACTICE 7 - DISCOUNT SYSTEM
# ============================================================

def calculate_discount(total):

    if total >= 100000:
        return 20

    elif total >= 50000:
        return 15

    elif total >= 10000:
        return 10

    elif total >= 5000:
        return 5

    return 0


discount_percentage = calculate_discount(
    cart_total
)

discount_amount = (
    cart_total *
    discount_percentage /
    100
)

final_amount = (
    cart_total -
    discount_amount
)

print("\n========== BILL ==========")

print(
    f"Subtotal: ₹{cart_total:,.2f}"
)

print(
    f"Discount: {discount_percentage}%"
)

print(
    f"Discount Amount: "
    f"₹{discount_amount:,.2f}"
)

print(
    f"Final Amount: "
    f"₹{final_amount:,.2f}"
)


# ============================================================
# PRACTICE 8 - EMPLOYEE MANAGEMENT
# ============================================================

employees = [
    {
        "id": 101,
        "name": "Jaya",
        "department": "AI",
        "salary": 90000
    },
    {
        "id": 102,
        "name": "Rahul",
        "department": "Backend",
        "salary": 75000
    },
    {
        "id": 103,
        "name": "Alex",
        "department": "AI",
        "salary": 95000
    },
    {
        "id": 104,
        "name": "Priya",
        "department": "Frontend",
        "salary": 70000
    }
]


def calculate_average_salary(employees):

    total = 0

    for employee in employees:
        total += employee["salary"]

    return total / len(employees)


print("\n========== EMPLOYEES ==========")

for employee in employees:

    print(
        f"{employee['id']} | "
        f"{employee['name']} | "
        f"{employee['department']} | "
        f"₹{employee['salary']:,.2f}"
    )


average_salary = calculate_average_salary(
    employees
)

print(
    f"Average Salary: "
    f"₹{average_salary:,.2f}"
)


# ============================================================
# PRACTICE 9 - HIGH SALARY EMPLOYEES
# ============================================================

salary_limit = 80000

print("\n========== HIGH SALARY EMPLOYEES ==========")

for employee in employees:

    if employee["salary"] > salary_limit:

        print(
            f"{employee['name']} - "
            f"₹{employee['salary']:,.2f}"
        )


# ============================================================
# PRACTICE 10 - SEARCH EMPLOYEE
# ============================================================

def find_employee(employees, name):

    for employee in employees:

        if employee["name"].lower() == name.lower():
            return employee

    return None


employee = find_employee(
    employees,
    "Alex"
)

print("\n========== EMPLOYEE SEARCH ==========")

if employee:

    print("Employee found:")
    print(employee)

else:

    print("Employee not found.")


# ============================================================
# PRACTICE 11 - AI TOKEN USAGE
# ============================================================

token_usage = [
    {
        "user": "Jaya",
        "tokens": 5000
    },
    {
        "user": "Rahul",
        "tokens": 1200
    },
    {
        "user": "Alex",
        "tokens": 8500
    },
    {
        "user": "Priya",
        "tokens": 900
    }
]


def calculate_total_tokens(token_usage):

    total = 0

    for user in token_usage:
        total += user["tokens"]

    return total


total_tokens = calculate_total_tokens(
    token_usage
)

print("\n========== AI TOKEN USAGE ==========")

for user in token_usage:

    print(
        f"{user['user']}: "
        f"{user['tokens']:,} tokens"
    )

print(
    f"Total Tokens: {total_tokens:,}"
)


# ============================================================
# PRACTICE 12 - TOKEN LIMIT CHECK
# ============================================================

token_limit = 5000

print("\n========== TOKEN LIMIT CHECK ==========")

for user in token_usage:

    if user["tokens"] > token_limit:

        print(
            f"WARNING: {user['user']} "
            f"exceeded the token limit."
        )

    else:

        print(
            f"{user['user']} is within the limit."
        )


# ============================================================
# PRACTICE 13 - COUNT WORDS
# ============================================================

def count_words(text):

    words = text.split()

    return len(words)


text = "Python is powerful for AI development"

print("\n========== WORD COUNTER ==========")

print(
    f"Text: {text}"
)

print(
    f"Word Count: {count_words(text)}"
)


# ============================================================
# PRACTICE 14 - COUNT CHARACTERS
# ============================================================

def count_characters(text):

    count = 0

    for character in text:

        if character != " ":
            count += 1

    return count


print(
    f"Character Count: "
    f"{count_characters(text)}"
)


# ============================================================
# PRACTICE 15 - PALINDROME
# ============================================================

def is_palindrome(text):

    text = text.lower()

    return text == text[::-1]


words = [
    "madam",
    "level",
    "python",
    "racecar"
]

print("\n========== PALINDROME CHECK ==========")

for word in words:

    if is_palindrome(word):
        print(f"{word}: Palindrome")

    else:
        print(f"{word}: Not Palindrome")


# ============================================================
# PRACTICE 16 - LOGIN SYSTEM
# ============================================================

def login(username, password):

    correct_username = "admin"
    correct_password = "python123"

    if username == correct_username:

        if password == correct_password:
            return True

    return False


username = "admin"
password = "python123"

if login(username, password):

    print("\nLogin successful.")

else:

    print("\nInvalid username or password.")


# ============================================================
# PRACTICE 17 - ATM
# ============================================================

def withdraw_money(balance, amount):

    if amount <= 0:
        return balance, "Invalid amount."

    if amount > balance:
        return balance, "Insufficient balance."

    balance -= amount

    return balance, "Withdrawal successful."


balance = 50000

balance, message = withdraw_money(
    balance,
    10000
)

print("\n========== ATM ==========")

print(message)

print(
    f"Balance: ₹{balance:,.2f}"
)


# ============================================================
# PRACTICE 18 - NESTED DATA
# ============================================================

company = {
    "name": "AI Technologies",
    "departments": [
        {
            "name": "AI",
            "employees": 20
        },
        {
            "name": "Backend",
            "employees": 15
        },
        {
            "name": "Frontend",
            "employees": 10
        }
    ]
}

print("\n========== COMPANY ==========")

print(
    f"Company: {company['name']}"
)

for department in company["departments"]:

    print(
        f"{department['name']}: "
        f"{department['employees']} employees"
    )


# ============================================================
# PRACTICE 19 - FIND DEPARTMENT
# ============================================================

def find_department(company, department_name):

    for department in company["departments"]:

        if (
            department["name"].lower()
            == department_name.lower()
        ):
            return department

    return None


department = find_department(
    company,
    "AI"
)

print("\n========== DEPARTMENT SEARCH ==========")

if department:

    print(department)

else:

    print("Department not found.")


# ============================================================
# PRACTICE 20 - COMBINED CHALLENGE
# ============================================================

# Build a Student Management Analyzer.
#
# Requirements:
#
# 1. Store students using a list of dictionaries.
#
# 2. Each student must have:
#    - ID
#    - Name
#    - Marks
#
# 3. Create a function to calculate grade.
#
# 4. Print every student's:
#    - Name
#    - Marks
#    - Grade
#
# 5. Calculate:
#    - Total marks
#    - Average marks
#
# 6. Find:
#    - Highest scorer
#    - Lowest scorer
#
# 7. Count:
#    - Number of passed students
#    - Number of failed students


students = [
    {
        "id": 1,
        "name": "Jaya",
        "marks": 92
    },
    {
        "id": 2,
        "name": "Rahul",
        "marks": 78
    },
    {
        "id": 3,
        "name": "Alex",
        "marks": 65
    },
    {
        "id": 4,
        "name": "Priya",
        "marks": 38
    },
    {
        "id": 5,
        "name": "Sam",
        "marks": 88
    }
]


def get_grade(marks):

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

    else:
        return "F"


total_marks = 0
passed_students = 0
failed_students = 0

highest_scorer = students[0]
lowest_scorer = students[0]


print("\n==========================================")
print("       STUDENT MANAGEMENT ANALYZER")
print("==========================================")


for student in students:

    marks = student["marks"]

    grade = get_grade(marks)

    total_marks += marks

    if marks >= 40:
        passed_students += 1

    else:
        failed_students += 1

    if marks > highest_scorer["marks"]:
        highest_scorer = student

    if marks < lowest_scorer["marks"]:
        lowest_scorer = student

    print(
        f"{student['id']} | "
        f"{student['name']} | "
        f"Marks: {marks} | "
        f"Grade: {grade}"
    )


average_marks = (
    total_marks / len(students)
)


print("\n========== SUMMARY ==========")

print(
    f"Total Marks: {total_marks}"
)

print(
    f"Average Marks: {average_marks:.2f}"
)

print(
    f"Passed Students: {passed_students}"
)

print(
    f"Failed Students: {failed_students}"
)

print(
    f"Highest Scorer: "
    f"{highest_scorer['name']} "
    f"({highest_scorer['marks']})"
)

print(
    f"Lowest Scorer: "
    f"{lowest_scorer['name']} "
    f"({lowest_scorer['marks']})"
)


# ============================================================
# FINAL INTERVIEW-STYLE CHALLENGE
# ============================================================

# Create a function called:
#
# analyze_students(students)
#
# The function should return a dictionary containing:
#
# {
#     "total_students": ...,
#     "average_marks": ...,
#     "passed": ...,
#     "failed": ...,
#     "highest_scorer": ...,
#     "lowest_scorer": ...
# }
#
# Try solving this independently before looking
# at any solution.


# ============================================================
# END
# ============================================================

print("\n" + "=" * 55)
print("Day 2 Practice completed successfully!")
print("=" * 55)