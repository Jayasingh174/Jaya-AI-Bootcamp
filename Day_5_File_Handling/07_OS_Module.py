# 07_OS_Module
# 07_OS_Module.py
# OS Module in Python

import os


# 1. Current Directory

print(os.getcwd())


# 2. List Files and Folders

print(os.listdir())


# 3. Check if File Exists

if os.path.exists("data.txt"):
    print("File exists.")
else:
    print("File not found.")


# 4. Create Folder

if not os.path.exists("Students"):
    os.mkdir("Students")

print("Folder ready.")


# 5. Rename File

if os.path.exists("old.txt"):
    os.rename("old.txt", "new.txt")


# 6. Delete File

if os.path.exists("temp.txt"):
    os.remove("temp.txt")


# 7. Real-World Example

folder = "Reports"

if not os.path.exists(folder):
    os.mkdir(folder)

print(f"{folder} folder created.")


# Key Point:
#
# os.getcwd()   → Current folder
# os.listdir()  → List files/folders
# os.path.exists() → Check existence
# os.mkdir()    → Create folder
# os.rename()   → Rename
# os.remove()   → Delete file


# 8. Practice

# Create a folder called "Projects".
#
# Check whether it exists.
#
# If it does not exist, create it.