# 08_Practice
# 08_Practice.py
# Day 5 - File Handling Practice

import os


# 1. Write a File

with open("students.txt", "w") as file:
    file.write("Jaya\n")
    file.write("Rahul\n")
    file.write("Alex\n")


# 2. Read the File

with open("students.txt", "r") as file:

    for student in file:
        print(student.strip())


# 3. Append Data

with open("students.txt", "a") as file:
    file.write("Priya\n")


# 4. Check File

if os.path.exists("students.txt"):
    print("File exists.")


# 5. File Information

file = open("students.txt", "r")

print("Name:", file.name)
print("Mode:", file.mode)

file.close()


# 6. File Pointer

file = open("students.txt", "r")

print("Position:", file.tell())

file.read(5)

print("Position:", file.tell())

file.seek(0)

print("Reset:", file.tell())

file.close()


# 7. Create Folder

folder = "Student_Data"

if not os.path.exists(folder):
    os.mkdir(folder)

print("Folder ready.")


# 8. FINAL CHALLENGE
#
# Create a Student File Manager.
#
# Requirements:
#
# 1. Create students.txt
# 2. Add 5 student names
# 3. Read and display students
# 4. Append one new student
# 5. Check if the file exists
# 6. Create a folder called Student_Data
#
# Use:
# - open()
# - read()
# - write()
# - append()
# - with
# - os


print("\nDay 5 Practice Completed!")