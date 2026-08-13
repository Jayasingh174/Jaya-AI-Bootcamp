# ============================================================
# PROJECT: Student Management System
# TOPICS COVERED:
# 1. Classes and Objects
# 2. __init__ Constructor
# 3. Instance Variables
# 4. self Keyword
# 5. Methods
# 6. Conditional Statements (if / elif / else)
# 7. Comparison Operators
# 8. Dictionaries
# 9. return Statement
# 10. f-strings
# 11. Encapsulation / Data Organization
# ============================================================


# ------------------------------------------------------------
# TOPIC: Class
# A class is a blueprint for creating objects.
# ------------------------------------------------------------
class Student:

    # --------------------------------------------------------
    # TOPIC: Constructor (__init__)
    # __init__ runs automatically when a Student object
    # is created.
    #
    # TOPIC: self
    # self refers to the current object.
    # --------------------------------------------------------
    def __init__(self, student_id, name, age, course, marks):

        # ----------------------------------------------------
        # TOPIC: Instance Variables
        # Each Student object gets its own data.
        # ----------------------------------------------------
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    # --------------------------------------------------------
    # TOPIC: Instance Method
    # A method is a function defined inside a class.
    #
    # This method calculates the student's grade.
    # --------------------------------------------------------
    def calculate_grade(self):

        # ----------------------------------------------------
        # TOPIC: Conditional Statements
        # if / elif / else
        #
        # TOPIC: Comparison Operators
        # >= means "greater than or equal to"
        # ----------------------------------------------------

        if self.marks >= 90:
            return "A"

        elif self.marks >= 80:
            return "B"

        elif self.marks >= 70:
            return "C"

        elif self.marks >= 60:
            return "D"

        else:
            return "F"

    # --------------------------------------------------------
    # TOPIC: Dictionary
    #
    # This method converts the Student object's data
    # into a dictionary.
    #
    # TOPIC: return statement
    # --------------------------------------------------------
    def to_dict(self):

        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,

            # Calling another method from the same class
            "grade": self.calculate_grade()
        }

    # --------------------------------------------------------
    # TOPIC: Instance Method
    #
    # display() prints the student's information.
    # --------------------------------------------------------
    def display(self):

        # ----------------------------------------------------
        # TOPIC: String Multiplication
        # "-" * 40 creates 40 hyphens.
        # ----------------------------------------------------
        print("-" * 40)

        # ----------------------------------------------------
        # TOPIC: f-string
        # f-strings allow us to insert variables into strings.
        # ----------------------------------------------------
        print(f"ID      : {self.student_id}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Course  : {self.course}")
        print(f"Marks   : {self.marks}")
        print(f"Grade   : {self.calculate_grade()}")


# ============================================================
# CREATING OBJECTS
# ============================================================
# TOPIC: Objects
#
# A class is the blueprint.
# An object is an actual instance created from the class.
# ============================================================

student1 = Student(
    101,
    "Rahul",
    20,
    "Python",
    92
)

student2 = Student(
    102,
    "Priya",
    21,
    "Generative AI",
    85
)


# ============================================================
# CALLING METHODS
# ============================================================

# TOPIC: Object Method Calling
student1.display()

student2.display()


# ============================================================
# CALCULATING GRADE
# ============================================================

# Calling calculate_grade() directly
print("\nStudent 1 Grade:", student1.calculate_grade())
print("Student 2 Grade:", student2.calculate_grade())


# ============================================================
# CONVERTING OBJECT DATA INTO DICTIONARY
# ============================================================

# TOPIC: Dictionary
student_data = Student.to_dict
student_data1 = student2.to_dict()
print("\nStudent Dictionary:")
print(student_data)
print(student_data1)