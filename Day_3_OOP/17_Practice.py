# ============================================================
# 17_Practice.py
# Day 3 - OOP Practice
# ============================================================


# ============================================================
# 1. BASIC CLASS + OBJECT
# ============================================================

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


student = Student("Jaya", 90)

student.show()


# ============================================================
# 2. CLASS VARIABLE
# ============================================================

class Employee:

    company = "JHEX"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(
            f"{self.name} - "
            f"₹{self.salary}"
        )


employee = Employee("Jaya", 90000)

employee.show()

print(employee.company)


# ============================================================
# 3. INSTANCE METHOD
# ============================================================

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print(
            f"Balance: ₹{self.balance}"
        )


account = BankAccount(50000)

account.deposit(10000)
account.withdraw(5000)

account.show_balance()


# ============================================================
# 4. INHERITANCE
# ============================================================

class Person:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")


class Developer(Person):

    def code(self):
        print("Developer is coding.")


developer = Developer("Rahul")

developer.show_name()
developer.code()


# ============================================================
# 5. METHOD OVERRIDING
# ============================================================

class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Dog says Woof")


class Cat(Animal):

    def sound(self):
        print("Cat says Meow")


animals = [
    Dog(),
    Cat()
]

for animal in animals:
    animal.sound()


# ============================================================
# 6. POLYMORPHISM
# ============================================================

class Email:

    def send(self):
        print("Sending Email")


class SMS:

    def send(self):
        print("Sending SMS")


messages = [
    Email(),
    SMS()
]

for message in messages:
    message.send()


# ============================================================
# 7. ENCAPSULATION
# ============================================================

class SecureAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


secure_account = SecureAccount(50000)

secure_account.deposit(10000)

print(
    f"Balance: ₹"
    f"{secure_account.get_balance()}"
)


# ============================================================
# 8. STATIC METHOD
# ============================================================

class Validator:

    @staticmethod
    def is_positive(number):
        return number > 0


print(
    Validator.is_positive(10)
)

print(
    Validator.is_positive(-5)
)


# ============================================================
# 9. FINAL CHALLENGE
# ============================================================

# Build a simple Employee Management System.
#
# Requirements:
#
# 1. Create an Employee class.
#
# 2. Store:
#    - name
#    - salary
#    - department
#
# 3. Add:
#    - show_details()
#    - increase_salary()
#
# 4. Create Developer and Manager classes.
#
# 5. Both should inherit Employee.
#
# 6. Override a method called work().
#
# 7. Use encapsulation for salary.
#
# 8. Create multiple employees.
#
# 9. Display all employee information.


class Employee:

    company = "JHEX"

    def __init__(
        self,
        name,
        salary,
        department
    ):
        self.name = name
        self.__salary = salary
        self.department = department

    def get_salary(self):
        return self.__salary

    def increase_salary(self, amount):

        if amount > 0:
            self.__salary += amount

    def work(self):
        print(
            f"{self.name} is working."
        )

    def show_details(self):

        print(
            f"Name: {self.name}"
        )

        print(
            f"Department: {self.department}"
        )

        print(
            f"Salary: ₹{self.__salary}"
        )


class Developer(Employee):

    def work(self):
        print(
            f"{self.name} is writing code."
        )


class Manager(Employee):

    def work(self):
        print(
            f"{self.name} is managing the team."
        )


# ============================================================
# CREATE OBJECTS
# ============================================================

developer = Developer(
    "Jaya",
    90000,
    "AI"
)

manager = Manager(
    "Rahul",
    100000,
    "Management"
)


# ============================================================
# DISPLAY DEVELOPER DETAILS
# ============================================================

print("\n========== DEVELOPER ==========")

developer.show_details()
developer.work()


# ============================================================
# DISPLAY MANAGER DETAILS
# ============================================================

print("\n========== MANAGER ==========")

manager.show_details()
manager.work()


# ============================================================
# INCREASE SALARY
# ============================================================

developer.increase_salary(10000)

print(
    f"\nUpdated Salary: "
    f"₹{developer.get_salary()}"
)


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Day 3 OOP Practice Completed!")
print("=" * 50)