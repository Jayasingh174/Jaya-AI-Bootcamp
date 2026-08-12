# 01_Open_File
# 01_Open_File.py
# Opening Files in Python


# 1. Create/Open a File

file = open("data.txt", "w")

file.write("Hello Python")

file.close()


# 2. Open for Reading

file = open("data.txt", "r")

print(file.read())

file.close()


# 3. File Modes

# "r" → Read
# "w" → Write
# "a" → Append
# "x" → Create new file


# 4. Check File Name

file = open("data.txt", "r")

print(file.name)

file.close()


# 5. Check File Mode

file = open("data.txt", "r")

print(file.mode)

file.close()


# 6. Real-World Example

file = open("user.txt", "w")

file.write("Name: Jaya\n")
file.write("Role: AI Engineer")

file.close()


# Key Point:
#
# open()  → Opens a file
# close() → Closes a file
#
# Example:
#
# file = open("data.txt", "r")
# file.close()


# 7. Practice

# Create a file called students.txt.
#
# Open it in write mode.
# Add 3 student names.
# Close the file.