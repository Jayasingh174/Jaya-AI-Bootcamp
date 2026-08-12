# 06_File_Pointer
# 06_File_Pointer.py
# File Pointer in Python


# 1. Tell Pointer Position

file = open("data.txt", "r")

print(file.tell())

file.close()


# 2. Read Data

file = open("data.txt", "r")

print(file.read(5))

print(file.tell())

file.close()


# 3. Move Pointer with seek()

file = open("data.txt", "r")

file.seek(0)

print(file.read())

file.close()


# 4. Read Again

file = open("data.txt", "r")

print(file.read(5))

file.seek(0)

print(file.read(5))

file.close()


# 5. Real-World Example

file = open("students.txt", "r")

print(file.read(10))

print("Position:", file.tell())

file.seek(0)

print("After reset:", file.tell())

file.close()


# Key Point:
#
# tell() → Shows current pointer position
# seek() → Moves pointer to a position
#
# Example:
#
# file.seek(0)
# → Moves pointer to the beginning.


# 6. Practice

# Create data.txt with some text.
#
# 1. Read first 5 characters.
# 2. Print the pointer position.
# 3. Use seek(0).
# 4. Read the file again.