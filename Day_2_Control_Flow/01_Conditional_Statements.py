# ============================================================
# 01_Conditional_Statements.py
# Python Control Flow - Conditional Statements
# ============================================================


# ============================================================
# 1. WHAT ARE CONDITIONAL STATEMENTS?
# ============================================================

# Conditional statements allow a program to make decisions.

# Python mainly uses:
# if
# elif
# else


# ============================================================
# 2. SIMPLE IF STATEMENT
# ============================================================

age = 20

if age >= 18:
    print("You are an adult.")


# ============================================================
# 3. IF CONDITION IS FALSE
# ============================================================

age = 15

if age >= 18:
    print("You are an adult.")

# Nothing is printed because the condition is False.


# ============================================================
# 4. IF-ELSE
# ============================================================

age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")


# ============================================================
# 5. IF-ELIF-ELSE
# ============================================================

marks = 75

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# ============================================================
# 6. MULTIPLE CONDITIONS
# ============================================================

age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")
else:
    print("Entry denied.")


# ============================================================
# 7. USING OR
# ============================================================

is_student = True
is_employee = False

if is_student or is_employee:
    print("You are eligible for access.")
else:
    print("Access denied.")


# ============================================================
# 8. USING NOT
# ============================================================

is_logged_in = False

if not is_logged_in:
    print("Please log in first.")


# ============================================================
# 9. COMPARISON OPERATORS
# ============================================================

number = 10

if number == 10:
    print("Number is 10.")

if number != 20:
    print("Number is not 20.")

if number > 5:
    print("Number is greater than 5.")

if number < 20:
    print("Number is less than 20.")

if number >= 10:
    print("Number is greater than or equal to 10.")

if number <= 10:
    print("Number is less than or equal to 10.")


# ============================================================
# 10. NESTED IF
# ============================================================

age = 25
has_license = True

if age >= 18:
    print("You are an adult.")

    if has_license:
        print("You can drive.")
    else:
        print("You need a driving license.")
else:
    print("You are not eligible to drive.")


# ============================================================
# 11. NESTED IF - LOGIN
# ============================================================

username = "admin"
password = "12345"

if username == "admin":
    if password == "12345":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Unknown username.")


# ============================================================
# 12. CHECK POSITIVE / NEGATIVE / ZERO
# ============================================================

number = -10

if number > 0:
    print("Positive number.")
elif number < 0:
    print("Negative number.")
else:
    print("Zero.")


# ============================================================
# 13. EVEN OR ODD
# ============================================================

number = 25

if number % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")


# ============================================================
# 14. VOTING ELIGIBILITY
# ============================================================

age = 22

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")


# ============================================================
# 15. STUDENT PASS OR FAIL
# ============================================================

marks = 72

if marks >= 40:
    print("Student passed.")
else:
    print("Student failed.")


# ============================================================
# 16. STUDENT GRADE
# ============================================================

marks = 86

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")


# ============================================================
# 17. AGE CATEGORY
# ============================================================

age = 35

if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior Citizen"

print(f"Category: {category}")


# ============================================================
# 18. TEMPERATURE CHECK
# ============================================================

temperature = 35

if temperature >= 40:
    print("Very Hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Normal")
elif temperature >= 10:
    print("Cold")
else:
    print("Very Cold")


# ============================================================
# 19. SHOPPING DISCOUNT
# ============================================================

purchase_amount = 7500

if purchase_amount >= 10000:
    discount = 20
elif purchase_amount >= 5000:
    discount = 10
elif purchase_amount >= 2000:
    discount = 5
else:
    discount = 0

print(f"Discount: {discount}%")


# ============================================================
# 20. CALCULATE FINAL PRICE
# ============================================================

price = 7500

if price >= 5000:
    discount = 10
else:
    discount = 5

discount_amount = price * discount / 100
final_price = price - discount_amount

print(f"Original Price: ₹{price:,.2f}")
print(f"Discount: {discount}%")
print(f"Discount Amount: ₹{discount_amount:,.2f}")
print(f"Final Price: ₹{final_price:,.2f}")


# ============================================================
# 21. LOGIN SYSTEM
# ============================================================

correct_username = "admin"
correct_password = "python123"

entered_username = "admin"
entered_password = "python123"

if entered_username == correct_username:
    if entered_password == correct_password:
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Incorrect username.")


# ============================================================
# 22. ATM WITHDRAWAL
# ============================================================

balance = 50000
withdrawal = 10000

if withdrawal <= 0:
    print("Invalid withdrawal amount.")
elif withdrawal > balance:
    print("Insufficient balance.")
else:
    balance -= withdrawal
    print("Withdrawal successful.")
    print(f"Remaining balance: ₹{balance:,.2f}")


# ============================================================
# 23. EMPLOYEE BONUS
# ============================================================

salary = 80000
performance = 90

if performance >= 90:
    bonus_percentage = 20
elif performance >= 75:
    bonus_percentage = 10
elif performance >= 60:
    bonus_percentage = 5
else:
    bonus_percentage = 0

bonus = salary * bonus_percentage / 100

print(f"Bonus Percentage: {bonus_percentage}%")
print(f"Bonus Amount: ₹{bonus:,.2f}")


# ============================================================
# 24. AI MODEL ACCESS
# ============================================================

user_type = "premium"
tokens_requested = 5000

if user_type == "premium":

    if tokens_requested <= 10000:
        print("AI request approved.")
    else:
        print("Token limit exceeded.")

elif user_type == "free":

    if tokens_requested <= 1000:
        print("AI request approved.")
    else:
        print("Free user token limit exceeded.")

else:
    print("Unknown user type.")


# ============================================================
# 25. TERNARY CONDITIONAL EXPRESSION
# ============================================================

age = 22

status = "Adult" if age >= 18 else "Minor"

print(status)


# ============================================================
# 26. TERNARY EXAMPLE - RESULT
# ============================================================

marks = 85

result = "Pass" if marks >= 40 else "Fail"

print(f"Result: {result}")


# ============================================================
# 27. CHECK EMPTY STRING
# ============================================================

name = "Jaya"

if name:
    print(f"Hello, {name}!")
else:
    print("Name is empty.")


# ============================================================
# 28. CHECK NONE
# ============================================================

data = None

if data is None:
    print("No data available.")
else:
    print("Data is available.")


# ============================================================
# 29. PRACTICE PROGRAM
# ============================================================

# Determine whether a customer gets free shipping.

# Order amount >= ₹1000 -> Free shipping
# Otherwise -> ₹100 shipping charge

order_amount = 1500

if order_amount >= 1000:
    shipping = 0
else:
    shipping = 100

print(f"Order Amount: ₹{order_amount:,.2f}")
print(f"Shipping: ₹{shipping:,.2f}")


# ============================================================
# 30. MINI CHALLENGE
# ============================================================

# Build a simple employee eligibility checker.

# Requirements:
# Age must be >= 18
# Experience must be >= 2 years
# Technical score must be >= 70

# If all conditions are satisfied:
# "Employee is eligible."

# Otherwise:
# "Employee is not eligible."

employee_age = 25
experience = 3
technical_score = 85

if (
    employee_age >= 18
    and experience >= 2
    and technical_score >= 70
):
    print("Employee is eligible.")
else:
    print("Employee is not eligible.")


# ============================================================
# END
# ============================================================

print("=" * 50)
print("Conditional Statements lesson completed!")
print("=" * 50)
