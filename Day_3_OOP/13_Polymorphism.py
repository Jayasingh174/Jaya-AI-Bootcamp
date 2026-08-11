# 13_Polymorphism
# ============================================================
# 13_Polymorphism.py
# Polymorphism in Python
# ============================================================


# ============================================================
# WHAT IS POLYMORPHISM?
# ============================================================

# Polymorphism means:
#
# "One interface, different behavior."
#
# The same method or function can behave differently
# depending on the object that uses it.
#
# Example:
#
# dog.sound()
# cat.sound()
#
# Same method name → Different behavior.


# ============================================================
# 1. SAME METHOD, DIFFERENT CLASSES
# ============================================================

# Dog has a sound() method.

class Dog:

    def sound(self):
        print("Dog says: Woof")


# Cat also has a sound() method.

class Cat:

    def sound(self):
        print("Cat says: Meow")


# Create objects
dog = Dog()
cat = Cat()


# Same method name
# but different behavior

dog.sound()
cat.sound()


# ============================================================
# 2. POLYMORPHISM WITH FUNCTION
# ============================================================

# The function does not need to know
# which specific class the object belongs to.
#
# It only expects the object to have
# a sound() method.


def make_sound(animal):
    animal.sound()


# Pass Dog object
make_sound(dog)

# Pass Cat object
make_sound(cat)


# ============================================================
# 3. REAL-WORLD EXAMPLE - MESSAGE SYSTEM
# ============================================================

# Email has a send() method.

class Email:

    def send(self):
        print("Sending Email")


# SMS also has a send() method.

class SMS:

    def send(self):
        print("Sending SMS")


# WhatsApp also has a send() method.

class WhatsApp:

    def send(self):
        print("Sending WhatsApp message")


# Store different objects in one list.

messages = [
    Email(),
    SMS(),
    WhatsApp()
]


# Same method call for every object.
#
# Each object provides different behavior.

for message in messages:
    message.send()


# ============================================================
# 4. AI EXAMPLE
# ============================================================

# OpenAI model has generate().

class OpenAI:

    def generate(self):
        print("Generating response using OpenAI")


# Gemini model also has generate().

class Gemini:

    def generate(self):
        print("Generating response using Gemini")


# Store different AI model objects
# in the same list.

models = [
    OpenAI(),
    Gemini()
]


# Same method call.
#
# Each model provides its own implementation.

for model in models:
    model.generate()


# ============================================================
# 5. BUILT-IN POLYMORPHISM
# ============================================================

# Python's built-in len() function
# works with different types of objects.

print(len("Python"))

print(len([10, 20, 30]))

print(len({"name": "Jaya"}))


# The same len() function works
# differently with different objects.
#
# String    → Number of characters
# List      → Number of elements
# Dictionary → Number of keys


# ============================================================
# 6. POLYMORPHISM WITH ANIMAL CLASSES
# ============================================================

class Bird:

    def sound(self):
        print("Bird is chirping")


class Cow:

    def sound(self):
        print("Cow says: Moo")


class Lion:

    def sound(self):
        print("Lion says: Roar")


animals = [
    Bird(),
    Cow(),
    Lion()
]


# Same sound() method
# with different behavior.

for animal in animals:
    animal.sound()


# ============================================================
# KEY POINT
# ============================================================

# Polymorphism allows the same method
# or function to work with different objects.
#
#
# Example:
#
# object1.sound()
# object2.sound()
#
#
# Same method name
#       ↓
# Different behavior
#
#
# Polymorphism is commonly used for:
#
# - Flexible code
# - Reusable code
# - Multiple implementations
# - AI model integrations
# - Payment systems
# - Notification systems
# - Database systems


# ============================================================
# 7. PRACTICE
# ============================================================

# Create:
#
# class Dog:
#
#     def sound(self):
#         print("Dog says: Woof")
#
#
# class Cat:
#
#     def sound(self):
#         print("Cat says: Meow")
#
#
# class Cow:
#
#     def sound(self):
#         print("Cow says: Moo")
#
#
# Store all objects in a list:
#
# animals = [
#     Dog(),
#     Cat(),
#     Cow()
# ]
#
#
# Use a loop:
#
# for animal in animals:
#     animal.sound()
#
#
# Expected output:
#
# Dog says: Woof
# Cat says: Meow
# Cow says: Moo


# ============================================================
# END
# ============================================================

print("\n" + "=" * 50)
print("Polymorphism lesson completed successfully!")
print("=" * 50)