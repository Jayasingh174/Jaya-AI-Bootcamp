# 04_Operators
# 04_Operators.py

# Python Basics - Operators

# ============================================================

# 1. WHAT ARE OPERATORS?

# ============================================================

# Operators are symbols or keywords used to perform

# operations on values and variables.

# ============================================================

# 2. ARITHMETIC OPERATORS

# ============================================================

# Arithmetic operators are used for mathematical calculations.

a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# ============================================================

# 3. UNDERSTANDING DIVISION

# ============================================================

a = 10
b = 3

print("Normal Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)

# ============================================================

# 4. EXPONENT OPERATOR

# ============================================================

# ** is used for powers.

number = 2

print("2 squared:", number ** 2)
print("2 cubed:", number ** 3)
print("2 power 10:", number ** 10)

# ============================================================

# 5. COMPARISON OPERATORS

# ============================================================

# Comparison operators compare two values.

# The result is always True or False.

x = 10
y = 20

print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater Than or Equal:", x >= y)
print("Less Than or Equal:", x <= y)

# ============================================================

# 6. COMPARISON EXAMPLES

# ============================================================

age = 25

print(age == 25)
print(age != 30)
print(age > 18)
print(age < 18)
print(age >= 21)
print(age <= 25)

# ============================================================

# 7. LOGICAL OPERATORS

# ============================================================

# Logical operators are used to combine conditions.

# and

# or

# not

# AND

age = 25
has_id = True

print(age >= 18 and has_id)

# OR

is_student = True
is_employee = False

print(is_student or is_employee)

# NOT

is_logged_in = True

print(not is_logged_in)

# ============================================================

# 8. LOGICAL AND

# ============================================================

# and returns True only when BOTH conditions are True.

age = 25
has_license = True

can_drive = age >= 18 and has_license

print("Can Drive:", can_drive)

# ============================================================

# 9. LOGICAL OR

# ============================================================

# or returns True when AT LEAST ONE condition is True.

has_credit_card = False
has_debit_card = True

can_make_payment = has_credit_card or has_debit_card

print("Can Make Payment:", can_make_payment)

# ============================================================

# 10. LOGICAL NOT

# ============================================================

# not reverses the Boolean value.

is_raining = False

print("Is Raining:", is_raining)
print("Not Raining:", not is_raining)

# ============================================================

# 11. ASSIGNMENT OPERATORS

# ============================================================

# Assignment operators are used to assign or update values.

x = 10

print("Initial:", x)

x += 5
print("After +=:", x)

x -= 3
print("After -=:", x)

x *= 2
print("After *=:", x)

x /= 4
print("After /=:", x)

x //= 2
print("After //=:", x)

x %= 3
print("After %=:", x)

x **= 2
print("After **=:", x)

# ============================================================

# 12. MEMBERSHIP OPERATORS

# ============================================================

# Membership operators check whether a value exists

# inside a collection.

# in

# not in

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)

print("Orange" not in fruits)

# ============================================================

# 13. MEMBERSHIP WITH STRINGS

# ============================================================

message = "Python is easy to learn"

print("Python" in message)
print("Java" in message)

print("Java" not in message)

# ============================================================

# 14. IDENTITY OPERATORS

# ============================================================

# Identity operators compare whether two variables

# refer to the SAME object in memory.

# is

# is not

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)

print(a == c)
print(a is c)

# == checks whether values are equal.

# is checks whether they are the same object.

# ============================================================

# 15. IS NOT

# ============================================================

x = None

print(x is None)
print(x is not None)

# ============================================================

# 16. BITWISE OPERATORS

# ============================================================

# Bitwise operators work with binary representations

# of integers.

a = 5
b = 3

print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

# ============================================================

# 17. OPERATOR PRECEDENCE

# ============================================================

# Python follows an order when evaluating expressions.

result = 10 + 5 * 2

print(result)

# Multiplication happens before addition.

result = (10 + 5) * 2

print(result)

# Parentheses can change the order.

# ============================================================

# 18. PRACTICAL EXAMPLE - SHOPPING CART

# ============================================================

product_price = 1000
quantity = 3

subtotal = product_price * quantity

print("Subtotal:", subtotal)

# ============================================================

# 19. PRACTICAL EXAMPLE - DISCOUNT

# ============================================================

price = 5000
discount_percentage = 10

discount_amount = price * discount_percentage / 100
final_price = price - discount_amount

print("Original Price:", price)
print("Discount:", discount_amount)
print("Final Price:", final_price)

# ============================================================

# 20. PRACTICAL EXAMPLE - ELIGIBILITY

# ============================================================

age = 22
has_degree = True

eligible = age >= 18 and has_degree

print("Eligible:", eligible)

# ============================================================

# 21. PRACTICAL EXAMPLE - LOGIN

# ============================================================

username = "admin"
password = "12345"

entered_username = "admin"
entered_password = "12345"

login_successful = (
username == entered_username
and password == entered_password
)

print("Login Successful:", login_successful)

# ============================================================

# 22. PRACTICAL EXAMPLE - STUDENT RESULT

# ============================================================

marks = 85

passed = marks >= 40
excellent = marks >= 80

print("Passed:", passed)
print("Excellent:", excellent)

# ============================================================

# 23. PRACTICAL EXAMPLE - AI APPLICATION

# ============================================================

tokens_used = 750
max_tokens = 1000

remaining_tokens = max_tokens - tokens_used

print("Tokens Used:", tokens_used)
print("Maximum Tokens:", max_tokens)
print("Remaining Tokens:", remaining_tokens)

# ============================================================

# 24. OPERATOR SUMMARY

# ============================================================

# Arithmetic:

# +   -   *   /   //   %   **

# Comparison:

# ==  !=  >  <  >=  <=

# Logical:

# and  or  not

# Assignment:

# =  +=  -=  *=  /=  //=  %=  **=

# Membership:

# in  not in

# Identity:

# is  is not

# Bitwise:

# &  |  ^  ~  <<  >>

# ============================================================

# 25. MINI CHALLENGE

# ============================================================

# A customer purchases 4 products.

#

# Product price = 2500

# Quantity = 4

# Discount = 15%

#

# Calculate:

# 1. Total price

# 2. Discount amount

# 3. Final price

# 4. Whether the customer gets a discount

# (discount must be greater than 0)

product_price = 2500
quantity = 4
discount = 15

total_price = product_price * quantity
discount_amount = total_price * discount / 100
final_price = total_price - discount_amount

has_discount = discount > 0

print("Total Price:", total_price)
print("Discount Amount:", discount_amount)
print("Final Price:", final_price)
print("Has Discount:", has_discount)

# ============================================================

# END

# ============================================================

print("Operators lesson completed successfully!")
