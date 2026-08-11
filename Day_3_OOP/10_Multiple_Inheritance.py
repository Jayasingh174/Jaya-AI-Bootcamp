# 10_Multiple_Inheritance
# ============================================================
# 10_Multiple_Inheritance.py
# Multiple Inheritance in Python
# ============================================================


# ============================================================
# WHAT IS MULTIPLE INHERITANCE?
# ============================================================

# Multiple inheritance means that one child class
# inherits from more than one parent class.
#
# Syntax:
#
# class Child(Parent1, Parent2):
#     pass
#
# The child class can access methods from both
# parent classes.


# ============================================================
# 1. BASIC EXAMPLE
# ============================================================

# Father is the first parent class.


class Father:

    def father_skill(self):
        print("Father: Driving")


# Mother is the second parent class.


class Mother:

    def mother_skill(self):
        print("Mother: Cooking")


# Child inherits from both Father and Mother.


class Child(Father, Mother):

    def child_skill(self):
        print("Child: Coding")


# Create Child object
child = Child()

# Method inherited from Father
child.father_skill()

# Method inherited from Mother
child.mother_skill()

# Method defined in Child
child.child_skill()


# ============================================================
# 2. REAL-WORLD EXAMPLE
# ============================================================

# Employee provides work-related behavior.


class Employee:

    def work(self):
        print("Employee is working.")


# Developer provides coding-related behavior.


class Developer:

    def code(self):
        print("Developer is coding.")


# AIEngineer inherits from both Employee and Developer.


class AIEngineer(Employee, Developer):

    def build_ai(self):
        print("AI Engineer is building AI.")


# Create AIEngineer object
engineer = AIEngineer()

# Method inherited from Employee
engineer.work()

# Method inherited from Developer
engineer.code()

# Method defined in AIEngineer
engineer.build_ai()


# ============================================================
# 3. MULTIPLE INHERITANCE WITH CONSTRUCTORS
# ============================================================

# Person contains a constructor that initializes name.


class Person:

    def __init__(self, name):
        self.name = name


# Employee provides the show_role() method.


class Employee:

    def show_role(self):
        print("Employee")


# Manager inherits from both Person and Employee.


class Manager(Person, Employee):

    def __init__(self, name):

        # Call the Person constructor
        super().__init__(name)

    def show(self):
        print(f"Name: {self.name}")


# Create Manager object
manager = Manager("Jaya")

# Display manager name
manager.show()

# Call inherited method from Employee
manager.show_role()


# ============================================================
# 4. METHOD RESOLUTION ORDER (MRO)
# ============================================================

# MRO stands for:
#
# Method Resolution Order
#
# When a class inherits from multiple classes,
# Python needs to determine which parent class
# should be searched first.


class A:

    def show(self):
        print("A")


class B:

    def show(self):
        print("B")


# C inherits from A first and B second.


class C(A, B):
    pass


# Create C object
obj = C()

# Python searches A before B,
# so A.show() is called.
obj.show()

# Display the Method Resolution Order
print(C.mro())


# Python checks parent classes according
# to the Method Resolution Order.
#
# For C(A, B), the order is approximately:
#
# C -> A -> B -> object


# ============================================================
# KEY POINT
# ============================================================

# Multiple Inheritance:
#
# One child -> Multiple parents
#
#
# Example:
#
# class Child(Parent1, Parent2):
#     pass
#
#
# The child can access methods from
# both parent classes.


# ============================================================
# 5. PRACTICE
# ============================================================

# Create:
#
# class Camera:
#
#     def take_photo(self):
#         print("Taking photo.")
#
#
# class Phone:
#
#     def make_call(self):
#         print("Making a call.")
#
#
# class Smartphone(Camera, Phone):
#
#     def use_apps(self):
#         print("Using apps.")
#
#
# Create a Smartphone object and
# call all three methods:
#
# 1. take_photo()
# 2. make_call()
# 3. use_apps()
#
#
# Expected structure:
#
# smartphone = Smartphone()
#
# smartphone.take_photo()
# smartphone.make_call()
# smartphone.use_apps()


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Multiple Inheritance lesson completed successfully!")
print("=" * 50)