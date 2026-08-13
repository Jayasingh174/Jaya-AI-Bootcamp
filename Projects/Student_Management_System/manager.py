# ============================================================
# FILE: manager.py
# ============================================================
#
# TOPICS COVERED:
# 1. Importing modules
# 2. Classes and Objects
# 3. Constructor (__init__)
# 4. Instance variables
# 5. Methods
# 6. self keyword
# 7. Lists
# 8. for loops
# 9. if statements
# 10. Comparison operators
# 11. Object creation
# 12. Custom exceptions
# 13. raise keyword
# 14. try / except
# 15. ValueError
# 16. Input validation
# 17. File handling
# 18. JSON persistence
# 19. return statement
# 20. List methods
# ============================================================


from student import Student

from exception import (
    StudentNotFoundError,
    DuplicateStudentError
)

from file import save_students, load_students


# ============================================================
# CLASS: StudentManager
# ============================================================

class StudentManager:

    # ========================================================
    # CONSTRUCTOR
    # ========================================================

    def __init__(self):

        # Instance variable
        self.students = []

        # Load existing data
        self.load_data()


    # ========================================================
    # METHOD: load_data()
    # ========================================================

    def load_data(self):

        # Load student data from JSON
        data = load_students()

        # Loop through loaded data
        for item in data:

            # Create Student object
            student = Student(
                item["student_id"],
                item["name"],
                item["age"],
                item["course"],
                item["marks"]
            )

            # Add Student object to list
            self.students.append(student)


    # ========================================================
    # METHOD: add_student()
    # ========================================================

    def add_student(
        self,
        student_id,
        name,
        age,
        course,
        marks
    ):

        # ----------------------------------------------------
        # TOPIC: INPUT VALIDATION
        # ----------------------------------------------------
        # Check whether student ID is valid.
        # ----------------------------------------------------

        if student_id <= 0:
            raise ValueError(
                "Student ID must be greater than 0."
            )


        # Check age
        if age <= 0:
            raise ValueError(
                "Age must be greater than 0."
            )


        # Check marks
        if marks < 0 or marks > 100:
            raise ValueError(
                "Marks must be between 0 and 100."
            )


        # Check name
        if not name.strip():
            raise ValueError(
                "Name cannot be empty."
            )


        # Check course
        if not course.strip():
            raise ValueError(
                "Course cannot be empty."
            )


        # ----------------------------------------------------
        # TOPIC: FOR LOOP
        # Check duplicate student ID
        # ----------------------------------------------------

        for student in self.students:

            if student.student_id == student_id:

                # ------------------------------------------------
                # TOPIC: CUSTOM EXCEPTION + raise
                # ------------------------------------------------

                raise DuplicateStudentError(
                    "Student ID already exists."
                )


        # ----------------------------------------------------
        # TOPIC: OBJECT CREATION
        # ----------------------------------------------------

        student = Student(
            student_id,
            name,
            age,
            course,
            marks
        )


        # ----------------------------------------------------
        # TOPIC: LIST append()
        # ----------------------------------------------------

        self.students.append(student)


        # ----------------------------------------------------
        # TOPIC: FILE HANDLING
        # ----------------------------------------------------

        save_students(self.students)


        print("Student added successfully.")


    # ========================================================
    # METHOD: view_students()
    # ========================================================

    def view_students(self):

        # ----------------------------------------------------
        # TOPIC: if statement
        # Empty list = False
        # ----------------------------------------------------

        if not self.students:

            print("No students found.")

            return


        # ----------------------------------------------------
        # TOPIC: for loop
        # ----------------------------------------------------

        for student in self.students:

            student.display()


    # ========================================================
    # METHOD: search_student()
    # ========================================================

    def search_student(self, student_id):

        # ----------------------------------------------------
        # TOPIC: INPUT VALIDATION
        # ----------------------------------------------------

        if student_id <= 0:

            raise ValueError(
                "Student ID must be greater than 0."
            )


        # ----------------------------------------------------
        # Search student
        # ----------------------------------------------------

        for student in self.students:

            if student.student_id == student_id:

                student.display()

                return


        # ----------------------------------------------------
        # TOPIC: CUSTOM EXCEPTION
        # ----------------------------------------------------

        raise StudentNotFoundError(
            "Student not found."
        )


    # ========================================================
    # METHOD: delete_student()
    # ========================================================

    def delete_student(self, student_id):

        # ----------------------------------------------------
        # TOPIC: INPUT VALIDATION
        # ----------------------------------------------------

        if student_id <= 0:

            raise ValueError(
                "Student ID must be greater than 0."
            )


        # ----------------------------------------------------
        # Search student
        # ----------------------------------------------------

        for student in self.students:

            if student.student_id == student_id:

                # Remove student
                self.students.remove(student)

                # Save updated data
                save_students(self.students)

                print(
                    "Student deleted successfully."
                )

                return


        # ----------------------------------------------------
        # Student not found
        # ----------------------------------------------------

        raise StudentNotFoundError(
            "Student not found."
        )