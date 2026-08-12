
# ============================================================
# 02_Loops.py
# Python Control Flow - Loops
# ============================================================


# ============================================================
# 1. WHAT ARE LOOPS?
# ============================================================

# Loops allow us to execute the same block of code
# multiple times.

# Python provides two main loops:
#
# 1. for loop
# 2. while loop


# ============================================================
# 2. BASIC FOR LOOP
# ============================================================

# A for loop is commonly used to iterate over a collection
# or a sequence of values.

for number in [1, 2, 3, 4, 5]:
    print(number)


# ============================================================
# 3. FOR LOOP WITH STRINGS
# ============================================================

name = "Python"

for character in name:
    print(character)


# ============================================================
# 4. FOR LOOP WITH A LIST
# ============================================================

fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)


# ============================================================
# 5. RANGE()
# ============================================================

# range() generates a sequence of numbers.

for number in range(5):
    print(number)

# Output:
# 0
# 1
# 2
# 3
# 4


# ============================================================
# 6. RANGE WITH START AND STOP
# ============================================================

for number in range(1, 6):
    print(number)


# ============================================================
# 7. RANGE WITH STEP
# ============================================================

for number in range(0, 11, 2):
    print(number)

# Output:
# 0
# 2
# 4
# 6
# 8
# 10


# ============================================================
# 8. COUNTING BACKWARDS
# ============================================================

for number in range(10, 0, -1):
    print(number)


# ============================================================
# 9. FOR LOOP WITH CONDITIONAL STATEMENT
# ============================================================

for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")


# ============================================================
# 10. PRINT ODD NUMBERS
# ============================================================

for number in range(1, 11):
    if number % 2 != 0:
        print(f"{number} is odd")


# ============================================================
# 11. SUM OF NUMBERS
# ============================================================

total = 0

for number in range(1, 11):
    total += number

print(f"Total: {total}")


# ============================================================
# 12. MULTIPLICATION TABLE
# ============================================================

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# ============================================================
# 13. LOOP THROUGH DICTIONARY
# ============================================================

student = {
    "name": "Jaya",
    "age": 25,
    "course": "Python"
}

for key in student:
    print(key)


# ============================================================
# 14. DICTIONARY KEYS AND VALUES
# ============================================================

for key, value in student.items():
    print(f"{key}: {value}")


# ============================================================
# 15. WHILE LOOP
# ============================================================

# A while loop continues running as long as
# its condition is True.

counter = 1

while counter <= 5:
    print(counter)
    counter += 1


# ============================================================
# 16. WHILE LOOP COUNTDOWN
# ============================================================

counter = 5

while counter >= 1:
    print(counter)
    counter -= 1


# ============================================================
# 17. WHILE LOOP WITH CONDITION
# ============================================================

number = 1

while number <= 10:
    if number % 2 == 0:
        print(number)

    number += 1


# ============================================================
# 18. INFINITE LOOP WARNING
# ============================================================

# Be careful with while loops.
#
# This creates an infinite loop:
#
# counter = 1
#
# while counter <= 5:
#     print(counter)
#
# counter never changes.

# Correct:

counter = 1

while counter <= 5:
    print(counter)
    counter += 1


# ============================================================
# 19. BREAK STATEMENT
# ============================================================

# break immediately stops the loop.

for number in range(1, 11):
    if number == 5:
        break

    print(number)


# ============================================================
# 20. CONTINUE STATEMENT
# ============================================================

# continue skips the current iteration
# and moves to the next iteration.

for number in range(1, 11):
    if number == 5:
        continue

    print(number)


# ============================================================
# 21. PASS STATEMENT
# ============================================================

# pass does nothing.
# It is used as a placeholder.

for number in range(5):
    if number == 3:
        pass

    print(number)


# ============================================================
# 22. NESTED LOOPS
# ============================================================

# A loop inside another loop is called a nested loop.

for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")


# ============================================================
# 23. STAR PATTERN
# ============================================================

for i in range(1, 6):
    print("*" * i)


# ============================================================
# 24. NUMBER PATTERN
# ============================================================

for i in range(1, 6):
    print(str(i) * i)


# ============================================================
# 25. NESTED LOOP - MULTIPLICATION TABLES
# ============================================================

for number in range(1, 4):
    print(f"\nTable of {number}")

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


# ============================================================
# 26. LOOP THROUGH LIST
# ============================================================

students = [
    "Jaya",
    "Rahul",
    "Alex",
    "Priya"
]

for student in students:
    print(f"Student: {student}")


# ============================================================
# 27. LOOP WITH INDEX
# ============================================================

students = [
    "Jaya",
    "Rahul",
    "Alex"
]

for index in range(len(students)):
    print(f"{index}: {students[index]}")


# ============================================================
# 28. ENUMERATE()
# ============================================================

# enumerate() provides both index and value.

students = [
    "Jaya",
    "Rahul",
    "Alex"
]

for index, student in enumerate(students):
    print(f"{index}: {student}")


# Starting index from 1:

for index, student in enumerate(students, start=1):
    print(f"{index}. {student}")


# ============================================================
# 29. LOOP WITH STRING
# ============================================================

message = "Python"

for character in message:
    if character == "o":
        print("Found letter o")


# ============================================================
# 30. COUNT VOWELS
# ============================================================

word = "programming"

vowels = "aeiou"
count = 0

for character in word:
    if character in vowels:
        count += 1

print(f"Number of vowels: {count}")


# ============================================================
# 31. FIND LARGEST NUMBER
# ============================================================

numbers = [10, 25, 5, 80, 45]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(f"Largest: {largest}")


# ============================================================
# 32. FIND SMALLEST NUMBER
# ============================================================

numbers = [10, 25, 5, 80, 45]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print(f"Smallest: {smallest}")


# ============================================================
# 33. CALCULATE AVERAGE
# ============================================================

marks = [80, 90, 75, 85, 95]

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print(f"Total: {total}")
print(f"Average: {average:.2f}")


# ============================================================
# 34. REAL-WORLD EXAMPLE - STUDENTS
# ============================================================

students = [
    "Jaya",
    "Rahul",
    "Alex",
    "Priya"
]

print("\n========== STUDENTS ==========")

for index, student in enumerate(students, start=1):
    print(f"{index}. {student}")


# ============================================================
# 35. REAL-WORLD EXAMPLE - SHOPPING CART
# ============================================================

prices = [1000, 2500, 500, 750]

total = 0

for price in prices:
    total += price

print("\n========== SHOPPING CART ==========")
print(f"Total: ₹{total:,.2f}")


# ============================================================
# 36. REAL-WORLD EXAMPLE - EMPLOYEE SALARIES
# ============================================================

salaries = [50000, 65000, 75000, 90000]

total_salary = 0

for salary in salaries:
    total_salary += salary

average_salary = total_salary / len(salaries)

print("\n========== SALARIES ==========")
print(f"Total Salary: ₹{total_salary:,.2f}")
print(f"Average Salary: ₹{average_salary:,.2f}")


# ============================================================
# 37. REAL-WORLD EXAMPLE - AI TOKENS
# ============================================================

token_usage = [500, 750, 1200, 450, 900]

total_tokens = 0

for tokens in token_usage:
    total_tokens += tokens

print("\n========== AI TOKEN USAGE ==========")
print(f"Total Tokens: {total_tokens:,}")


# ============================================================
# 38. FIND TOKEN USAGE ABOVE LIMIT
# ============================================================

token_limit = 1000

for tokens in token_usage:
    if tokens > token_limit:
        print(
            f"Warning: {tokens} tokens exceeded the limit."
        )


# ============================================================
# 39. SEARCH USING BREAK
# ============================================================

users = [
    "Jaya",
    "Rahul",
    "Alex",
    "Priya"
]

search_name = "Alex"

for user in users:
    if user == search_name:
        print(f"User {search_name} found.")
        break


# ============================================================
# 40. SKIP VALUES USING CONTINUE
# ============================================================

numbers = range(1, 11)

for number in numbers:
    if number % 2 != 0:
        continue

    print(f"Even number: {number}")


# ============================================================
# 41. WHILE LOOP - LOGIN ATTEMPTS
# ============================================================

correct_password = "python123"

attempts = 0
max_attempts = 3

# Demo value instead of input.
password = "python123"

while attempts < max_attempts:
    attempts += 1

    if password == correct_password:
        print("Login successful.")
        break

    print("Incorrect password.")
else:
    print("Maximum login attempts reached.")


# ============================================================
# 42. WHILE LOOP - BANK ACCOUNT
# ============================================================

balance = 50000
withdrawal = 10000

while withdrawal > 0:

    if withdrawal <= balance:
        balance -= withdrawal

        print(
            f"Withdrawal successful. "
            f"Balance: ₹{balance:,.2f}"
        )

        break

    print("Insufficient balance.")
    break


# ============================================================
# 43. PRACTICE - FACTORIAL
# ============================================================

number = 5

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"{number}! = {factorial}")


# ============================================================
# 44. PRACTICE - REVERSE STRING
# ============================================================

word = "Python"

reversed_word = ""

for character in word:
    reversed_word = character + reversed_word

print(f"Original: {word}")
print(f"Reversed: {reversed_word}")


# ============================================================
# 45. MINI CHALLENGE - NUMBER ANALYZER
# ============================================================

# Given a list of numbers:
#
# 1. Count even numbers
# 2. Count odd numbers
# 3. Calculate total
# 4. Calculate average
# 5. Find the largest number
# 6. Find the smallest number

numbers = [10, 25, 30, 45, 50, 65, 80]

even_count = 0
odd_count = 0
total = 0
largest = numbers[0]
smallest = numbers[0]

for number in numbers:

    total += number

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

average = total / len(numbers)

print("\n========================================")
print("           NUMBER ANALYZER")
print("========================================")

print(f"Numbers     : {numbers}")
print(f"Even Count  : {even_count}")
print(f"Odd Count   : {odd_count}")
print(f"Total       : {total}")
print(f"Average     : {average:.2f}")
print(f"Largest     : {largest}")
print(f"Smallest    : {smallest}")


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Loops lesson completed successfully!")
print("=" * 50)
