
# ============================================================
# 04_Data_Structures.py
# Python Data Structures
# ============================================================


# ============================================================
# 1. WHAT ARE DATA STRUCTURES?
# ============================================================

# Data structures are used to store and organize data.

# Common Python data structures:
#
# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary


# ============================================================
# 2. LIST
# ============================================================

# A list:
# - Is ordered
# - Is mutable
# - Allows duplicate values
# - Uses square brackets []

students = [
    "Jaya",
    "Rahul",
    "Alex",
    "Priya"
]

print(students)


# ============================================================
# 3. LIST INDEXING
# ============================================================

print(students[0])
print(students[1])
print(students[-1])


# ============================================================
# 4. LIST SLICING
# ============================================================

print(students[0:2])
print(students[:3])
print(students[2:])
print(students[::-1])


# ============================================================
# 5. MODIFY LIST
# ============================================================

students[0] = "Jaya Patel"

print(students)


# ============================================================
# 6. APPEND()
# ============================================================

students.append("Sam")

print(students)


# ============================================================
# 7. INSERT()
# ============================================================

students.insert(1, "David")

print(students)


# ============================================================
# 8. REMOVE()
# ============================================================

students.remove("David")

print(students)


# ============================================================
# 9. POP()
# ============================================================

removed_student = students.pop()

print(f"Removed: {removed_student}")
print(students)


# ============================================================
# 10. SORT()
# ============================================================

numbers = [50, 10, 80, 20, 40]

numbers.sort()

print(numbers)


# ============================================================
# 11. SORT DESCENDING
# ============================================================

numbers.sort(reverse=True)

print(numbers)


# ============================================================
# 12. REVERSE()
# ============================================================

students.reverse()

print(students)


# ============================================================
# 13. LEN()
# ============================================================

print(f"Number of students: {len(students)}")


# ============================================================
# 14. IN OPERATOR
# ============================================================

if "Jaya Patel" in students:
    print("Student found.")


# ============================================================
# 15. LOOP THROUGH LIST
# ============================================================

for student in students:
    print(student)


# ============================================================
# 16. LIST OF NUMBERS
# ============================================================

marks = [
    85,
    90,
    75,
    92,
    88
]

print(f"Total marks: {sum(marks)}")
print(f"Highest marks: {max(marks)}")
print(f"Lowest marks: {min(marks)}")
print(f"Average marks: {sum(marks) / len(marks):.2f}")


# ============================================================
# 17. LIST COMPREHENSION
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = [
    number ** 2
    for number in numbers
]

print(squares)


# ============================================================
# 18. LIST COMPREHENSION WITH CONDITION
# ============================================================

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)


# ============================================================
# 19. TUPLE
# ============================================================

# A tuple:
# - Is ordered
# - Is immutable
# - Allows duplicates
# - Uses parentheses ()

coordinates = (10, 20)

print(coordinates)


# ============================================================
# 20. TUPLE INDEXING
# ============================================================

print(coordinates[0])
print(coordinates[1])


# ============================================================
# 21. TUPLE UNPACKING
# ============================================================

x, y = coordinates

print(f"X: {x}")
print(f"Y: {y}")


# ============================================================
# 22. TUPLE METHODS
# ============================================================

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
print(numbers.index(20))


# ============================================================
# 23. SET
# ============================================================

# A set:
# - Stores unique values
# - Does not allow duplicates
# - Uses curly braces {}

numbers = {
    1,
    2,
    3,
    3,
    4,
    4
}

print(numbers)


# ============================================================
# 24. ADD TO SET
# ============================================================

numbers.add(5)

print(numbers)


# ============================================================
# 25. REMOVE FROM SET
# ============================================================

numbers.remove(5)

print(numbers)


# ============================================================
# 26. DISCARD FROM SET
# ============================================================

numbers.discard(100)

# discard() does not raise an error
# if the value does not exist.


# ============================================================
# 27. SET UNION
# ============================================================

python_students = {
    "Jaya",
    "Rahul",
    "Alex"
}

ai_students = {
    "Alex",
    "Priya",
    "Sam"
}

all_students = python_students.union(ai_students)

print(all_students)


# ============================================================
# 28. SET INTERSECTION
# ============================================================

common_students = python_students.intersection(
    ai_students
)

print(common_students)


# ============================================================
# 29. SET DIFFERENCE
# ============================================================

only_python = python_students.difference(
    ai_students
)

print(only_python)


# ============================================================
# 30. DICTIONARY
# ============================================================

# Dictionary stores data as:
#
# key -> value
#
# Uses curly braces {}

student = {
    "name": "Jaya",
    "age": 25,
    "course": "AI",
    "score": 92
}

print(student)


# ============================================================
# 31. ACCESS DICTIONARY VALUES
# ============================================================

print(student["name"])
print(student["age"])
print(student["course"])


# ============================================================
# 32. GET()
# ============================================================

print(student.get("name"))
print(student.get("email"))

# get() returns None if the key doesn't exist.


# ============================================================
# 33. MODIFY DICTIONARY
# ============================================================

student["score"] = 95

print(student)


# ============================================================
# 34. ADD DICTIONARY VALUE
# ============================================================

student["email"] = "jaya@example.com"

print(student)


# ============================================================
# 35. REMOVE DICTIONARY VALUE
# ============================================================

student.pop("email")

print(student)


# ============================================================
# 36. DICTIONARY KEYS
# ============================================================

print(student.keys())


# ============================================================
# 37. DICTIONARY VALUES
# ============================================================

print(student.values())


# ============================================================
# 38. DICTIONARY ITEMS
# ============================================================

print(student.items())


# ============================================================
# 39. LOOP THROUGH DICTIONARY
# ============================================================

for key, value in student.items():
    print(f"{key}: {value}")


# ============================================================
# 40. DICTIONARY CHECK
# ============================================================

if "name" in student:
    print("Name exists.")


# ============================================================
# 41. NESTED DICTIONARY
# ============================================================

employee = {
    "id": 101,
    "name": "Alex",
    "department": {
        "name": "Artificial Intelligence",
        "manager": "Jaya"
    }
}

print(employee["department"]["name"])
print(employee["department"]["manager"])


# ============================================================
# 42. LIST OF DICTIONARIES
# ============================================================

employees = [
    {
        "id": 101,
        "name": "Jaya",
        "salary": 90000
    },
    {
        "id": 102,
        "name": "Rahul",
        "salary": 80000
    },
    {
        "id": 103,
        "name": "Alex",
        "salary": 75000
    }
]

for employee in employees:
    print(
        f"{employee['name']} - "
        f"₹{employee['salary']:,.2f}"
    )


# ============================================================
# 43. REAL-WORLD EXAMPLE - STUDENT MANAGEMENT
# ============================================================

students = [
    {
        "id": 1,
        "name": "Jaya",
        "age": 25,
        "marks": 92
    },
    {
        "id": 2,
        "name": "Rahul",
        "age": 23,
        "marks": 85
    },
    {
        "id": 3,
        "name": "Alex",
        "age": 24,
        "marks": 78
    }
]

print("\n========== STUDENTS ==========")

for student in students:
    print(
        f"ID: {student['id']} | "
        f"Name: {student['name']} | "
        f"Marks: {student['marks']}"
    )


# ============================================================
# 44. FIND STUDENT
# ============================================================

search_name = "Rahul"

for student in students:

    if student["name"] == search_name:

        print(
            f"Student found: {student}"
        )

        break


# ============================================================
# 45. REAL-WORLD EXAMPLE - SHOPPING CART
# ============================================================

cart = [
    {
        "product": "Laptop",
        "price": 85000,
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

total = 0

for item in cart:

    item_total = (
        item["price"] *
        item["quantity"]
    )

    total += item_total

    print(
        f"{item['product']}: "
        f"₹{item_total:,.2f}"
    )

print(f"Cart Total: ₹{total:,.2f}")


# ============================================================
# 46. REAL-WORLD EXAMPLE - AI CONFIGURATION
# ============================================================

ai_config = {
    "model": "GPT",
    "temperature": 0.7,
    "max_tokens": 2000,
    "streaming": True
}

print("\n========== AI CONFIG ==========")

for key, value in ai_config.items():
    print(f"{key}: {value}")


# ============================================================
# 47. REAL-WORLD EXAMPLE - API RESPONSE
# ============================================================

api_response = {
    "status": "success",
    "status_code": 200,
    "data": {
        "user_id": 101,
        "name": "Jaya",
        "role": "AI Engineer"
    }
}

print(
    f"Status: {api_response['status']}"
)

print(
    f"User: {api_response['data']['name']}"
)

print(
    f"Role: {api_response['data']['role']}"
)


# ============================================================
# 48. CONVERT LIST TO SET
# ============================================================

skills = [
    "Python",
    "AI",
    "Python",
    "FastAPI",
    "AI"
]

unique_skills = set(skills)

print(unique_skills)


# ============================================================
# 49. CONVERT SET TO LIST
# ============================================================

unique_skills_list = list(unique_skills)

print(unique_skills_list)


# ============================================================
# 50. CONVERT LIST TO TUPLE
# ============================================================

skills_tuple = tuple(skills)

print(skills_tuple)


# ============================================================
# 51. CONVERT TUPLE TO LIST
# ============================================================

skills_list = list(skills_tuple)

print(skills_list)


# ============================================================
# 52. DICTIONARY COMPREHENSION
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)


# ============================================================
# 53. FILTER DICTIONARY DATA
# ============================================================

employees = {
    "Jaya": 90000,
    "Rahul": 80000,
    "Alex": 70000,
    "Priya": 95000
}

high_salary_employees = {
    name: salary
    for name, salary in employees.items()
    if salary >= 80000
}

print(high_salary_employees)


# ============================================================
# 54. PRACTICE - COUNT FREQUENCY
# ============================================================

numbers = [
    1,
    2,
    2,
    3,
    3,
    3,
    4
]

frequency = {}

for number in numbers:

    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print(frequency)


# ============================================================
# 55. PRACTICE - REMOVE DUPLICATES
# ============================================================

numbers = [
    10,
    20,
    10,
    30,
    20,
    40
]

unique_numbers = list(set(numbers))

print(unique_numbers)


# ============================================================
# 56. MINI CHALLENGE
# ============================================================

# Build a simple Employee Management Data Structure.
#
# Store at least 5 employees.
#
# Each employee should contain:
# - ID
# - Name
# - Department
# - Salary
#
# Then:
#
# 1. Print all employees.
# 2. Find employees earning more than ₹80,000.
# 3. Calculate total salary.
# 4. Calculate average salary.
# 5. Find the highest-paid employee.


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
        "salary": 80000
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
        "salary": 75000
    },
    {
        "id": 105,
        "name": "Sam",
        "department": "DevOps",
        "salary": 85000
    }
]


print("\n========================================")
print("          EMPLOYEE MANAGEMENT")
print("==========================================")


total_salary = 0
highest_paid = employees[0]


for employee in employees:

    print(
        f"{employee['id']} | "
        f"{employee['name']} | "
        f"{employee['department']} | "
        f"₹{employee['salary']:,.2f}"
    )

    total_salary += employee["salary"]

    if employee["salary"] > 80000:

        print(
            f"High Salary Employee: "
            f"{employee['name']}"
        )

    if employee["salary"] > highest_paid["salary"]:
        highest_paid = employee


average_salary = total_salary / len(employees)


print("\n========== SUMMARY ==========")

print(
    f"Total Salary: ₹{total_salary:,.2f}"
)

print(
    f"Average Salary: ₹{average_salary:,.2f}"
)

print(
    f"Highest Paid: "
    f"{highest_paid['name']} "
    f"- ₹{highest_paid['salary']:,.2f}"
)


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Data Structures lesson completed successfully!")
print("=" * 50)
