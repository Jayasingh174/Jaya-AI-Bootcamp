# 15_Abstraction
# ============================================================
# 16_Abstraction.py
# Abstraction in Python
# ============================================================


# ============================================================
# WHAT IS ABSTRACTION?
# ============================================================

# Abstraction means hiding unnecessary implementation details
# and showing only the essential functionality.
#
# Real-world example:
#
# When we use an ATM:
#
# - We enter our PIN.
# - We select an amount.
# - We receive money.
#
# We do not need to know the internal code
# that communicates with the bank server.
#
# In Python, abstraction is commonly implemented using:
#
# - Abstract classes
# - Abstract methods
# - The abc module


# ============================================================
# 1. IMPORT ABSTRACT CLASS TOOLS
# ============================================================

from abc import ABC, abstractmethod


# ============================================================
# 2. BASIC ABSTRACT CLASS
# ============================================================

# ABC means Abstract Base Class.

class Animal(ABC):

    # Abstract method.
    #
    # A child class must provide
    # its own implementation.

    @abstractmethod
    def sound(self):
        pass


# ============================================================
# 3. CHILD CLASS IMPLEMENTATION
# ============================================================

class Dog(Animal):

    def sound(self):
        print("Dog says: Woof")


class Cat(Animal):

    def sound(self):
        print("Cat says: Meow")


# Create child objects.

dog = Dog()
cat = Cat()


# Call the implemented methods.

dog.sound()
cat.sound()


# ============================================================
# 4. ABSTRACT CLASS CANNOT BE INSTANTIATED
# ============================================================

# The following code would produce an error:
#
# animal = Animal()
#
# Why?
#
# Animal contains an abstract method
# that has not been implemented.


# ============================================================
# 5. REAL-WORLD EXAMPLE - PAYMENT SYSTEM
# ============================================================

# Payment is an abstract concept.
#
# Every payment method should provide
# a pay() method.

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Credit Card implementation

class CreditCardPayment(Payment):

    def pay(self, amount):
        print(
            f"Paid ₹{amount:,.2f} using Credit Card."
        )


# UPI implementation

class UPIPayment(Payment):

    def pay(self, amount):
        print(
            f"Paid ₹{amount:,.2f} using UPI."
        )


# Create payment objects.

credit_card = CreditCardPayment()
upi = UPIPayment()


# Same method name,
# different implementations.

credit_card.pay(5000)
upi.pay(2500)


# ============================================================
# 6. REAL-WORLD AI EXAMPLE
# ============================================================

# Different AI models can have
# a common generate() interface.

class AIModel(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass


# OpenAI implementation

class OpenAIModel(AIModel):

    def generate(self, prompt):
        print(
            f"OpenAI generating response for: {prompt}"
        )


# Gemini implementation

class GeminiModel(AIModel):

    def generate(self, prompt):
        print(
            f"Gemini generating response for: {prompt}"
        )


# Create model objects.

openai_model = OpenAIModel()
gemini_model = GeminiModel()


# Same interface:
#
# generate()
#
# Different implementations.

openai_model.generate(
    "Explain Python."
)

gemini_model.generate(
    "Explain Python."
)


# ============================================================
# 7. ABSTRACT CLASS WITH NORMAL METHOD
# ============================================================

# An abstract class can contain:
#
# - Abstract methods
# - Normal methods
#
# Normal methods can contain
# reusable implementation.

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Vehicle stopped.")


class Car(Vehicle):

    def start(self):
        print("Car started.")


car = Car()

car.start()
car.stop()


# ============================================================
# 8. MULTIPLE ABSTRACT METHODS
# ============================================================

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass


class Developer(Employee):

    def work(self):
        print("Developer is writing code.")

    def get_salary(self):
        return 90000


developer = Developer()

developer.work()

print(
    f"Salary: ₹{developer.get_salary():,.2f}"
)


# ============================================================
# 9. ABSTRACTION + POLYMORPHISM
# ============================================================

# Abstraction defines the common interface.
#
# Polymorphism allows different child classes
# to provide different implementations.

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):

    def send(self, message):
        print(
            f"Email: {message}"
        )


class SMSNotification(Notification):

    def send(self, message):
        print(
            f"SMS: {message}"
        )


class WhatsAppNotification(Notification):

    def send(self, message):
        print(
            f"WhatsApp: {message}"
        )


notifications = [
    EmailNotification(),
    SMSNotification(),
    WhatsAppNotification()
]


for notification in notifications:
    notification.send("Your order has been shipped.")


# ============================================================
# 10. ABSTRACTION VS ENCAPSULATION
# ============================================================

# ABSTRACTION:
#
# Hides implementation details.
#
# Focus:
# "What should the object do?"
#
#
# Example:
#
# payment.pay()
#
# We only care that payment should happen.
#
#
# ENCAPSULATION:
#
# Protects and controls access to data.
#
# Focus:
# "How should the data be protected?"
#
# Example:
#
# self.__balance
#
# Private data is protected inside the class.


# ============================================================
# KEY POINT
# ============================================================

# Abstraction:
#
# - Hides unnecessary implementation details.
# - Shows only essential functionality.
# - Uses abstract classes and abstract methods.
# - Helps create a common interface.
# - Makes large applications easier to maintain.
#
#
# Example:
#
# Abstract Class
#       ↓
#     Payment
#       ↓
# -------------------
# ↓        ↓         ↓
# UPI   CreditCard  PayPal
#
#
# All payment classes implement:
#
# pay()
#
# But each class can implement
# the method differently.


# ============================================================
# 11. PRACTICE
# ============================================================

# Create an abstract class:
#
# class Shape(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
#
# Create two child classes:
#
# Rectangle
# Circle
#
#
# Rectangle should calculate:
#
# area = length * width
#
#
# Circle should calculate:
#
# area = 3.14 * radius * radius
#
#
# Create objects and call:
#
# rectangle.area()
# circle.area()


# ============================================================
# INTERVIEW QUESTIONS
# ============================================================

# Q1. What is abstraction?
#
# Answer:
# Abstraction is the process of hiding unnecessary
# implementation details and exposing only essential
# functionality.
#
#
# Q2. Which module is used for abstraction in Python?
#
# Answer:
# The abc module.
#
#
# Q3. What is an abstract method?
#
# Answer:
# A method declared using @abstractmethod that
# must be implemented by child classes.
#
#
# Q4. Can we create an object of an abstract class?
#
# Answer:
# No. An abstract class containing unimplemented
# abstract methods cannot be instantiated.
#
#
# Q5. What is ABC?
#
# Answer:
# ABC stands for Abstract Base Class.


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Abstraction lesson completed successfully!")
print("=" * 50)