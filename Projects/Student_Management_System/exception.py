# ============================================================
# TOPIC: CUSTOM EXCEPTIONS
# ============================================================
# Custom exceptions allow us to create our own error types.
#
# We create custom exceptions by inheriting from Exception.
#
# Exception
#    │
#    ├── StudentNotFoundError
#    └── DuplicateStudentError
# ============================================================


# ------------------------------------------------------------
# CUSTOM EXCEPTION 1
# ------------------------------------------------------------
# Raised when a student cannot be found.
#
# Example:
# Searching for student ID 105 when ID 105 does not exist.
# ------------------------------------------------------------
class StudentNotFoundError(Exception):
    pass


# ------------------------------------------------------------
# CUSTOM EXCEPTION 2
# ------------------------------------------------------------
# Raised when we try to add a student whose ID already exists.
#
# Example:
# Student ID 101 already exists, but we try to add another
# student with ID 101.
# ------------------------------------------------------------
class DuplicateStudentError(Exception):
    pass