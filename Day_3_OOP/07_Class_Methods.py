# 07_Class_Methods
# ============================================================
# 07_Class_Methods.py
# Class Methods in Python
# ============================================================


# ============================================================
# WHAT ARE CLASS METHODS?
# ============================================================

# A class method is a method that works with the class
# rather than a specific object.
#
# Class methods use:
#
# @classmethod
#
# The first parameter is usually:
#
# cls
#
# "cls" refers to the class itself.
#
# Class methods can access and modify class variables.


# ============================================================
# 1. BASIC CLASS METHOD
# ============================================================

class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(f"School: {cls.school}")


# Call the class method using the class name
Student.show_school()


# ============================================================
# 2. CLASS METHOD USING AN OBJECT
# ============================================================

# A class method can also be called using an object.
#
# However, class methods are normally called
# using the class name because they work with
# class-level data.


student1 = Student()

student1.show_school()


# ============================================================
# 3. MODIFY CLASS VARIABLE
# ============================================================

class Employee:

    company = "JHEX"

    @classmethod
    def change_company(cls, new_company):
        # Modify the class variable
        cls.company = new_company

    @classmethod
    def show_company(cls):
        print(f"Company: {cls.company}")


# Display the original company
Employee.show_company()

# Change the class variable
Employee.change_company("AI Technologies")

# Display the updated company
Employee.show_company()


# ============================================================
# 4. CLASS METHOD WITH INSTANCE VARIABLES
# ============================================================

# Class methods work with class-level data.
#
# They cannot directly access instance variables
# because they do not receive "self".


class Car:

    total_cars = 0

    def __init__(self, brand):
        self.brand = brand

        # Increase the shared class variable
        Car.total_cars += 1

    @classmethod
    def show_total_cars(cls):
        print(f"Total Cars: {cls.total_cars}")


# Create Car objects
car1 = Car("Toyota")
car2 = Car("BMW")
car3 = Car("Honda")

# Display total number of cars
Car.show_total_cars()


# ============================================================
# 5. REAL-WORLD EXAMPLE - BANK
# ============================================================

class Bank:

    bank_name = "ABC Bank"
    branch_count = 10

    @classmethod
    def show_bank_info(cls):
        print(f"Bank: {cls.bank_name}")
        print(f"Branches: {cls.branch_count}")

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name


# Display bank information
Bank.show_bank_info()

# Change bank name
Bank.change_bank_name("Global Bank")

# Display updated information
Bank.show_bank_info()


# ============================================================
# 6. CLASS METHOD AS AN ALTERNATIVE CONSTRUCTOR
# ============================================================

# A class method can also be used to create objects
# in different ways.
#
# This is called an alternative constructor.


class StudentRecord:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    @classmethod
    def from_string(cls, data):
        # Example data:
        # "Jaya,25"

        name, age = data.split(",")

        # Create and return a new object
        return cls(name, int(age))


# Normal object creation
student1 = StudentRecord("Rahul", 23)

student1.show_details()


# Object creation using class method
student2 = StudentRecord.from_string("Jaya,25")

student2.show_details()


# ============================================================
# 7. INSTANCE METHOD VS CLASS METHOD
# ============================================================

# Instance Method:
#
# - Uses self
# - Works with object data
# - Can access instance variables
# - Can modify instance variables
#
#
# Class Method:
#
# - Uses cls
# - Uses @classmethod
# - Works with class data
# - Can access class variables
# - Can modify class variables


class Example:

    class_variable = "Class Data"

    def __init__(self, instance_data):
        self.instance_data = instance_data

    # Instance method
    def show_instance_data(self):
        print(f"Instance Data: {self.instance_data}")

    # Class method
    @classmethod
    def show_class_data(cls):
        print(f"Class Data: {cls.class_variable}")


example = Example("Object Data")

example.show_instance_data()

Example.show_class_data()


# ============================================================
# 8. REAL-WORLD EXAMPLE - EMPLOYEE COUNTER
# ============================================================

class EmployeeRecord:

    company = "JHEX"
    employee_count = 0

    def __init__(self, name):
        self.name = name

        # Increase employee count
        EmployeeRecord.employee_count += 1

    @classmethod
    def show_employee_count(cls):
        print(
            f"Total Employees: "
            f"{cls.employee_count}"
        )


# Create employees
employee1 = EmployeeRecord("Jaya")
employee2 = EmployeeRecord("Rahul")
employee3 = EmployeeRecord("Alex")

# Display total employees
EmployeeRecord.show_employee_count()


# ============================================================
# KEY POINT
# ============================================================

# Remember:
#
# self -> refers to the current object
#
# cls  -> refers to the current class
#
#
# Instance method:
#
# def method(self):
#     ...
#
#
# Class method:
#
# @classmethod
# def method(cls):
#     ...


# ============================================================
# 9. PRACTICE
# ============================================================

# Create a BankAccount class.
#
# Class variables:
#
# - bank_name = "ABC Bank"
# - total_accounts = 0
#
# Instance variables:
#
# - owner
# - balance
#
# Methods:
#
# 1. __init__()
#    - Store owner and balance
#    - Increase total_accounts
#
# 2. show_details()
#    - Display owner and balance
#
# 3. @classmethod
#    show_total_accounts()
#    - Display total accounts
#
# 4. @classmethod
#    change_bank_name()
#    - Change the bank name
#
#
# Create at least three accounts
# and test all methods.


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Class Methods lesson completed successfully!")
print("=" * 50)