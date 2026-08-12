# 03_Write_File
# 03_Write_File.py
# Writing Files in Python


# 1. Write Text

file = open("data.txt", "w")

file.write("Hello Python!")

file.close()


# 2. Write Multiple Lines

file = open("students.txt", "w")

file.write("Jaya\n")
file.write("Rahul\n")
file.write("Alex\n")

file.close()


# 3. Write a List

students = [
    "Jaya",
    "Rahul",
    "Alex"
]

file = open("students.txt", "w")

for student in students:
    file.write(student + "\n")

file.close()


# 4. Real-World Example

file = open("employee.txt", "w")

file.write("Name: Jaya\n")
file.write("Role: AI Engineer\n")
file.write("Department: AI\n")

file.close()


# Key Point:
#
# "w" → Write mode
#
# Important:
# "w" replaces existing file content.


# 5. Practice

# Create products.txt.
#
# Write:
# Laptop
# Mouse
# Keyboard
#
# Then close the file.