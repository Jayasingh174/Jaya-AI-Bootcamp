# 04_Append_File
# 04_Append_File.py
# Appending Data to Files


# 1. Basic Append

file = open("data.txt", "a")

file.write("\nNew data added.")

file.close()


# 2. Append Multiple Lines

file = open("students.txt", "a")

file.write("Jaya\n")
file.write("Rahul\n")
file.write("Alex\n")

file.close()


# 3. Append User Input

name = input("Enter student name: ")

file = open("students.txt", "a")

file.write(name + "\n")

file.close()


# 4. Real-World Example

file = open("employees.txt", "a")

file.write("Jaya - AI Engineer\n")

file.close()


# Key Point:
#
# "a" → Append mode
#
# Append adds new data to the
# existing content.
#
# It does NOT delete old data.


# 5. Practice

# Create a file called tasks.txt.
#
# Add:
# Task 1
# Task 2
#
# Run the program again and add:
# Task 3
#
# Check that all tasks remain in the file.