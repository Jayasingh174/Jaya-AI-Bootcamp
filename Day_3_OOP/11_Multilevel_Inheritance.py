# ============================================================
# 11_Multilevel_Inheritance.py
# Multilevel Inheritance in Python
# ============================================================


# ============================================================
# WHAT IS MULTILEVEL INHERITANCE?
# ============================================================

# Multilevel inheritance means inheritance
# happens through multiple levels.
#
# Example:
#
# Grandparent → Parent → Child
#
#
# In Python:
#
# class A:
#     ...
#
# class B(A):
#     ...
#
# class C(B):
#     ...
#
# C can access methods from both B and A.


# ============================================================
# 1. BASIC EXAMPLE
# ============================================================

# Animal is the first level (grandparent).

class Animal:

    def eat(self):
        print("Animal is eating.")


# Dog inherits from Animal.
#
# Dog is the second level (parent).

class Dog(Animal):

    def bark(self):
        print("Dog is barking.")


# Puppy inherits from Dog.
#
# Puppy is the third level (child).

class Puppy(Dog):

    def play(self):
        print("Puppy is playing.")


# Create Puppy object

puppy = Puppy()

# Method inherited from Animal
puppy.eat()

# Method inherited from Dog
puppy.bark()

# Method defined inside Puppy
puppy.play()


# ============================================================
# 2. REAL-WORLD EXAMPLE
# ============================================================

# Person is the base class.

class Person:

    def introduce(self):
        print("I am a person.")


# Employee inherits from Person.

class Employee(Person):

    def work(self):
        print("I am working.")


# AIEngineer inherits from Employee.
#
# Therefore, AIEngineer can access methods from:
#
# AIEngineer
# Employee
# Person

class AIEngineer(Employee):

    def build_model(self):
        print("I am building an AI model.")


# Create AIEngineer object

engineer = AIEngineer()

# Method inherited from Person
engineer.introduce()

# Method inherited from Employee
engineer.work()

# Method defined in AIEngineer
engineer.build_model()


# ============================================================
# 3. MULTILEVEL INHERITANCE WITH CONSTRUCTOR
# ============================================================

# Person contains the first constructor.

class Person:

    def __init__(self, name):
        self.name = name


# Employee MUST inherit from Person.
#
# Employee has its own constructor and
# calls the parent constructor using super().

class Employee(Person):

    def __init__(self, name, salary):

        # Call Person constructor
        super().__init__(name)

        # Employee's own instance variable
        self.salary = salary


# Manager inherits from Employee.

class Manager(Employee):

    def __init__(self, name, salary, department):

        # Call Employee constructor
        super().__init__(name, salary)

        # Manager's own instance variable
        self.department = department

    def show(self):
        print(f"Name: {self.name}")
        print(f"Salary: ₹{self.salary}")
        print(f"Department: {self.department}")


# Create Manager object

manager = Manager(
    "Jaya",
    100000,
    "AI"
)

# Display manager details

manager.show()


# ============================================================
# INHERITANCE FLOW
# ============================================================

# Person
#    ↓
# Employee
#    ↓
# Manager
#
#
# Manager inherits from Employee.
#
# Employee inherits from Person.
#
# Therefore, Manager can access
# attributes and methods from all levels.


# ============================================================
# 4. HOW super() WORKS
# ============================================================

# In the example above:
#
# Manager.__init__()
#        ↓
# Employee.__init__()
#        ↓
# Person.__init__()
#
#
# Each class initializes its own data
# and passes control to the parent class.


# ============================================================
# 5. KEY POINT
# ============================================================

# Multilevel inheritance:
#
# Grandparent → Parent → Child
#
#
# Example:
#
# Person
#    ↓
# Employee
#    ↓
# Manager
#
#
# The child can access methods and variables
# inherited from all levels of the hierarchy.


# ============================================================
# 6. PRACTICE
# ============================================================

# Create:
#
# Animal
#    ↓
# Dog
#    ↓
# Puppy
#
#
# Animal should contain:
#
# eat()
#
#
# Dog should contain:
#
# bark()
#
#
# Puppy should contain:
#
# play()
#
#
# Create a Puppy object and call:
#
# puppy.eat()
# puppy.bark()
# puppy.play()
#
#
# Expected output:
#
# Animal is eating.
# Dog is barking.
# Puppy is playing.


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Multilevel Inheritance lesson completed successfully!")
print("=" * 50)