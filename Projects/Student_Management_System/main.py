# ============================================================
# FILE: main.py
# ============================================================
#
# TOPICS COVERED:
# 1. User Input
# 2. input() function
# 3. Type Casting
# 4. int()
# 5. float()
# 6. String Input
# 7. while loop
# 8. if / elif / else
# 9. try / except
# 10. ValueError
# 11. Custom Exceptions
# 12. Function Calls
# 13. Menu-Driven Program
# ============================================================


from manager import StudentManager

from exception import (
    StudentNotFoundError,
    DuplicateStudentError
)


# ============================================================
# CREATE MANAGER OBJECT
# ============================================================

manager = StudentManager()


# ============================================================
# MENU FUNCTION
# ============================================================

def show_menu():

    print("\n" + "=" * 50)
    print("        STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    print("=" * 50)


# ============================================================
# ADD STUDENT
# ============================================================

def add_student():

    try:

        # ----------------------------------------------------
        # TOPIC: INPUT
        # input() takes data from the user.
        #
        # input() always returns a string.
        # ----------------------------------------------------

        student_id = int(
            input("Enter Student ID: ")
        )

        # String input
        name = input(
            "Enter Student Name: "
        )

        # Convert string input to integer
        age = int(
            input("Enter Student Age: ")
        )

        # String input
        course = input(
            "Enter Course: "
        )

        # Convert string input to float
        marks = float(
            input("Enter Marks: ")
        )


        # ----------------------------------------------------
        # Send user input to StudentManager
        # ----------------------------------------------------

        manager.add_student(
            student_id,
            name,
            age,
            course,
            marks
        )


    # --------------------------------------------------------
    # TOPIC: EXCEPTION HANDLING
    #
    # If user enters:
    # abc instead of 101
    #
    # int("abc") causes ValueError.
    # --------------------------------------------------------

    except ValueError:

        print(
            "Invalid input. Please enter valid numbers."
        )


    # --------------------------------------------------------
    # TOPIC: CUSTOM EXCEPTION
    # --------------------------------------------------------

    except DuplicateStudentError as error:

        print("Error:", error)


# ============================================================
# SEARCH STUDENT
# ============================================================

def search_student():

    try:

        # ----------------------------------------------------
        # TOPIC: INPUT + TYPE CASTING
        # ----------------------------------------------------

        student_id = int(
            input("Enter Student ID: ")
        )

        manager.search_student(student_id)


    except ValueError:

        print("Student ID must be a number.")


    except StudentNotFoundError as error:

        print("Error:", error)


# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student():

    try:

        # ----------------------------------------------------
        # TOPIC: INPUT + TYPE CASTING
        # ----------------------------------------------------

        student_id = int(
            input("Enter Student ID to delete: ")
        )

        manager.delete_student(student_id)


    except ValueError:

        print("Student ID must be a number.")


    except StudentNotFoundError as error:

        print("Error:", error)


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():

    # --------------------------------------------------------
    # TOPIC: WHILE LOOP
    #
    # Menu keeps running until user chooses 5.
    # --------------------------------------------------------

    while True:

        show_menu()

        # ----------------------------------------------------
        # TOPIC: USER INPUT
        # ----------------------------------------------------

        choice = input(
            "Enter your choice (1-5): "
        )


        # ----------------------------------------------------
        # TOPIC: CONDITIONAL STATEMENTS
        # ----------------------------------------------------

        if choice == "1":

            add_student()


        elif choice == "2":

            manager.view_students()


        elif choice == "3":

            search_student()


        elif choice == "4":

            delete_student()


        elif choice == "5":

            print("Thank you for using the system.")

            break


        else:

            print(
                "Invalid choice. Please choose 1-5."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()