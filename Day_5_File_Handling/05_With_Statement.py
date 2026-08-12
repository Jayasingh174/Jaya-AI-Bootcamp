# 05_With_Statement
# 05_With_Statement.py
# with Statement in Python


# 1. Write File

with open("data.txt", "w") as file:

    file.write("Hello Python")


# 2. Read File

with open("data.txt", "r") as file:

    data = file.read()

print(data)


# 3. Multiple Lines

with open("students.txt", "w") as file:

    file.write("Jaya\n")
    file.write("Rahul\n")
    file.write("Alex\n")


# 4. Read Line by Line

with open("students.txt", "r") as file:

    for student in file:
        print(student.strip())


# 5. Append Data

with open("students.txt", "a") as file:

    file.write("Priya\n")


# Key Point:
#
# with open(...) as file:
#     ...
#
# The file is automatically closed
# after the block finishes.


# 6. Real-World Example

with open("log.txt", "a") as file:

    file.write("User logged in\n")


# 7. Practice

# Create tasks.txt using with.
#
# Write:
# Task 1
# Task 2
# Task 3
#
# Then read and print all tasks.