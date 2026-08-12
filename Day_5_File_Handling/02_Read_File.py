# 02_Read_File
# 02_Read_File.py
# Reading Files in Python


# 1. Read Entire File

file = open("data.txt", "r")

data = file.read()

print(data)

file.close()


# 2. Read Specific Characters

file = open("data.txt", "r")

print(file.read(5))

file.close()


# 3. Read One Line

file = open("data.txt", "r")

print(file.readline())

file.close()


# 4. Read All Lines

file = open("data.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# 5. Loop Through File

file = open("data.txt", "r")

for line in file:
    print(line.strip())

file.close()


# 6. Real-World Example

file = open("students.txt", "r")

for student in file:
    print(f"Student: {student.strip()}")

file.close()


# Key Point:
#
# read()      → Reads entire file
# readline()  → Reads one line
# readlines() → Reads all lines as a list


# 7. Practice

# Create students.txt with 3 names.
#
# Read the file and print each
# student name on a separate line.