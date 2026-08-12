
# ============================================================
# 02_Objects.py
# Objects in Python
# ============================================================


# ============================================================
# 1. CREATE A CLASS
# ============================================================

# A class is a blueprint for creating objects.
#
# Here, Student is a class.
# The show() method defines the behavior of the object.


class Student:

    def show(self):
        print("Student object")


# ============================================================
# 2. CREATE AN OBJECT
# ============================================================

# An object is an instance of a class.
#
# Here, student1 is an object of the Student class.

student1 = Student()

# Calling the show() method using the object
student1.show()


# ============================================================
# 3. MULTIPLE OBJECTS
# ============================================================

# We can create multiple objects
# from the same class.

student2 = Student()

# student2 is a separate object
student2.show()


# ============================================================
# 4. OBJECT ATTRIBUTES
# ============================================================

# Objects can store their own data.
#
# In this example:
# name and role are object attributes.


class Employee:

    def show(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")


# Create the first Employee object
employee1 = Employee()

# Add attributes to employee1
employee1.name = "Jaya"
employee1.role = "AI Engineer"

# Display employee1 details
employee1.show()


# ============================================================
# 5. DIFFERENT OBJECTS HAVE DIFFERENT DATA
# ============================================================

# Every object can contain different attribute values.
#
# employee1 and employee2 are created from the
# same Employee class, but they contain different data.


employee2 = Employee()

employee2.name = "Rahul"
employee2.role = "Python Developer"

# Display employee2 details
employee2.show()


# ============================================================
# 6. REAL-WORLD EXAMPLE - CAR
# ============================================================

# A class can represent a real-world entity.
#
# Here, Car represents a car.
# The brand attribute stores the car's brand.


class Car:

    def drive(self):
        print(f"{self.brand} is driving.")


# Create a Car object
car1 = Car()

# Add brand information
car1.brand = "Toyota"

# Call the drive() method
car1.drive()


# ============================================================
# 7. CHECK OBJECT TYPE
# ============================================================

# type() tells us the type/class of an object.

print(type(car1))

# isinstance() checks whether an object
# belongs to a particular class.

print(isinstance(car1, Car))


# ============================================================
# 8. PRACTICE
# ============================================================

# Create a Product class.
#
# Add:
#
# - name
# - price
# - category
#
# Create two Product objects
# and display their details.
#
#
# Example structure:
#
# class Product:
#
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Price: ₹{self.price}")
#         print(f"Category: {self.category}")
#
#
# Then create:
#
# product1 = Product()
# product2 = Product()
#
# Give each product different values
# and call show_details().


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Objects lesson completed successfully!")
print("=" * 50)
