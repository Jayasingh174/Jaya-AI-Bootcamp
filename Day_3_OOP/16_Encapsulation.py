# ============================================================
# 16_Encapsulation.py
# Encapsulation in Python
# ============================================================


# ============================================================
# WHAT IS ENCAPSULATION?
# ============================================================

# Encapsulation means protecting data
# and controlling how it is accessed.
#
# It allows us to keep internal data
# inside a class and provide controlled
# access through methods.
#
# Python commonly uses:
#
# Public    → self.name
# Protected → self._name
# Private   → self.__name


# ============================================================
# 1. BASIC ENCAPSULATION
# ============================================================

class BankAccount:

    def __init__(self, balance):
        # __balance is a private variable.
        self.__balance = balance

    def show_balance(self):
        print(f"Balance: ₹{self.__balance}")


# Create object
account = BankAccount(50000)

# Access balance through a method
account.show_balance()


# __balance is private.
#
# Direct access like:
#
# account.__balance
#
# is not recommended and will raise
# an AttributeError.


# ============================================================
# 2. PRIVATE VARIABLE
# ============================================================

class Student:

    def __init__(self, marks):
        # Private instance variable
        self.__marks = marks

    def get_marks(self):
        # Controlled access to private data
        return self.__marks


student = Student(90)

print(
    f"Marks: {student.get_marks()}"
)


# ============================================================
# 3. GETTER AND SETTER
# ============================================================

class Employee:

    def __init__(self, salary):
        self.__salary = salary

    # Getter
    # Used to read private data.

    def get_salary(self):
        return self.__salary

    # Setter
    # Used to update private data.

    def set_salary(self, salary):

        # Only allow a positive salary.
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be greater than 0.")


employee = Employee(80000)

# Get salary
print(
    f"Salary: ₹{employee.get_salary():,.2f}"
)

# Change salary
employee.set_salary(90000)

# Get updated salary
print(
    f"Updated Salary: ₹{employee.get_salary():,.2f}"
)


# ============================================================
# 4. REAL-WORLD EXAMPLE - BANK ACCOUNT
# ============================================================

class BankAccount:

    def __init__(self, balance):

        # Private balance
        self.__balance = balance

    def deposit(self, amount):

        # Deposit only positive amounts.
        if amount > 0:
            self.__balance += amount
            print(
                f"Deposited: ₹{amount:,.2f}"
            )
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):

        # Check that the amount is positive
        # and does not exceed the balance.
        if 0 < amount <= self.__balance:
            self.__balance -= amount

            print(
                f"Withdrawn: ₹{amount:,.2f}"
            )

        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        # Getter for balance
        return self.__balance


account = BankAccount(50000)

account.deposit(10000)

account.withdraw(5000)

print(
    f"Balance: ₹{account.get_balance():,.2f}"
)


# ============================================================
# 5. PUBLIC, PROTECTED AND PRIVATE
# ============================================================

class User:

    def __init__(self):

        # Public variable
        self.name = "Jaya"

        # Protected variable
        # Conventionally treated as internal data.
        self._email = "jaya@example.com"

        # Private variable
        self.__password = "python123"


user = User()

# Public variable can be accessed directly.
print(user.name)

# Protected variable can technically
# be accessed, but the underscore indicates
# that it is intended for internal use.
print(user._email)

# Private variable cannot normally
# be accessed directly using __password.
#
# print(user.__password)
#
# This would raise an AttributeError.


# ============================================================
# 6. CONTROLLED ACCESS
# ============================================================

class Account:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):

        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")


account = Account(10000)

print(
    f"Balance: ₹{account.get_balance():,.2f}"
)

account.set_balance(15000)

print(
    f"Updated Balance: ₹{account.get_balance():,.2f}"
)

account.set_balance(-500)


# ============================================================
# 7. REAL-WORLD EXAMPLE - USER
# ============================================================

class UserAccount:

    def __init__(self, username, password):

        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def change_password(self, new_password):

        if len(new_password) >= 6:
            self.__password = new_password
            print("Password changed successfully.")
        else:
            print(
                "Password must contain at least 6 characters."
            )


user = UserAccount(
    "jaya",
    "python123"
)

print(
    f"Username: {user.get_username()}"
)

user.change_password("newpass")

user.change_password("123")


# ============================================================
# 8. WHY ENCAPSULATION IS IMPORTANT
# ============================================================

# Encapsulation helps us:
#
# 1. Protect internal data.
#
# 2. Control how data is modified.
#
# 3. Validate data before changing it.
#
# 4. Prevent accidental changes.
#
# 5. Keep code organized.
#
#
# Example:
#
# Instead of:
#
# account.balance = -50000
#
# We can use:
#
# account.set_balance(-50000)
#
# The method can validate the value
# before changing the data.


# ============================================================
# KEY POINT
# ============================================================

# PUBLIC
#
# self.name
#
# Public data can normally be accessed
# directly from outside the class.


# PROTECTED
#
# self._name
#
# A single underscore indicates that the
# variable is intended for internal use.
#
# It is a convention in Python,
# not strict access protection.


# PRIVATE
#self.__name
#
# Double underscore triggers Python's
# name-mangling mechanism.
#
# It is commonly used to make direct
# external access harder.


# ============================================================
# ENCAPSULATION FLOW
# ============================================================

# Private Data
#      ↓
# Getter / Setter
#      ↓
# Validation / Control
#      ↓
# Outside Code


# ============================================================
# 9. PRACTICE
# ============================================================

# Create a class User.
#
#
# Private variables:
#
# - __username
# - __password
#
#
# Methods:
#
# - get_username()
# - change_password()
#
#
# Requirements:
#
# 1. get_username() should return the username.
#
# 2. change_password() should accept
#    a new password.
#
# 3. Only allow the password to change
#    when the new password has at least
#    6 characters.
#
#
# Example:
#
# user = User("jaya", "python123")
#
# print(user.get_username())
#
# user.change_password("newpassword")
#
# user.change_password("123")
#
#
# Expected output:
#
# jaya
# Password changed successfully.
# Password must contain at least 6 characters.


# ============================================================
# INTERVIEW QUESTIONS
# ============================================================

# Q1. What is encapsulation?
#
# Answer:
# Encapsulation is the process of protecting data
# and controlling how that data is accessed
# or modified.


# Q2. What is a private variable in Python?
#
# Answer:
# A variable beginning with double underscores,
# such as self.__balance, is treated as private
# through Python's name-mangling mechanism.


# Q3. What is a getter?
#
# Answer:
# A getter is a method used to read
# or retrieve private data.


# Q4. What is a setter?
#
# Answer:
# A setter is a method used to modify
# private data, often with validation.


# Q5. What is the difference between
# _name and __name?
#
# Answer:
#
# _name:
# Conventionally indicates protected/internal use.
#
# __name:
# Uses name mangling and makes direct
# external access more difficult.


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Encapsulation lesson completed successfully!")
print("=" * 50)
