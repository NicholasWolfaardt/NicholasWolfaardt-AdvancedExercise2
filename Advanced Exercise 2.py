# -------------------------------------------
# Advanced Python Challenge: Exercise 02 Operators and Conditionals
# -------------------------------------------

# Overview:
# This exercise challenges your understanding of Python operators, conditionals, and input handling.
# Complete each section with the required logic, using good variable names and adding comments where necessary.

# -------------------------------------------
# Question 1: Multi-Step Arithmetic Operations
# -------------------------------------------

# Task:
# Use compound arithmetic operators to modify values of a, b, and c.
# Then calculate the square root of the sum of their squares.
# Tip: Use the math module.

import math

# Start with some base values
a = 5
b = 10
c = 7

# TODO: Add 3 to a using +=
a += 3

# TODO: Multiply b by 2 using *=
b *= 2

# TODO: Modulo c by 4 using %=
c %= 4

# TODO: Calculate the square root of (a^2 + b^2 + c^2)
result = a^2 + b^2 + c^2
result = math.sqrt(result)

# TODO: Print the final result rounded to 2 decimal places
print(round(result, 2))

# -------------------------------------------
# Question 2: Complex Conditional Evaluation
# -------------------------------------------

# Task:
# Ask the user to input three integers (x, y, z).
# Then evaluate and print whether:
# - x is even
# - y is positive
# - z is between 10 and 50
# Use logical operators to combine the conditions.

# Tip: Use and/or to join conditions.

# TODO: Input x, y, z
x = int(input("Type in a number for x: "))
y = int(input("Type in a number for y: "))
z = int(input("Type in a number for z: "))

# TODO: Create conditions:
#   is_even = True if x is even
is_even = x % 2 == 0

#   is_positive = True if y > 0
is_positive = y > 0

#   is_in_range = True if z between 10 and 50
is_in_range = 10 < z < 50

# TODO: Create final_condition = is_even and is_positive and is_in_range
final_condition = is_even and is_positive and is_in_range

# TODO: Print final_condition
print(final_condition)

# -------------------------------------------
# Question 3: Grading with Adjustments
# -------------------------------------------

# Task:
# Ask the user for their base score, then apply:
# - bonus points (+5)
# - late penalty (-10)
# Final score must not exceed 100 or drop below 0.
# Then assign a grade.

# Tip: Use min() and max() to constrain the score.

# TODO: Input score from user
score = int(input("Type in your base score: "))

# TODO: Apply adjustments
score += 5
score -= 10

# TODO: Clamp score between 0 and 100
if 0 < score > 100:
  print("Your final score exceeds 100 or is below 0")

# TODO: Use if-elif-else to determine grade and print it
if score > 100:
  print("Your final score exceeds 100")
elif 90 <= score < 100:
  print("Your grade is A")
elif 80 <= score < 90:
  print("Your grade is B")
elif 70 <= score < 80:
  print("Your grade is C")
elif 60 <= score < 70:
  print("Your grade is D")
elif score < 60:
  print("Your grade is F")
elif score < 0:
  print("Your final score is below 0")
  

# -------------------------------------------
# Question 4: Advanced Calculator
# -------------------------------------------

# Task:
# Ask the user to input two numbers and an operation (+, -, *, /, %, **).
# Handle division/modulus by zero with error checking.
# Perform the operation and print the result.

# Tip: Use try-except and elif branches for each operation.

# TODO: Input num1, num2
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("That's not a number. Try again.")

num1 = get_number("Type in a number for num1: ")
num2 = get_number("Type in a number for num2: ")


# TODO: Input operation
operation = input("Choose an operation (+, -, *, /, %, **): ")
while operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "%" and operation != "**":
  operation = input("Please choose an operation from the list in the brackets (+, -, *, /, %, **): ")

# TODO: Match operation using if-elif
def result(num1, num2, operation):
  if operation == "+":
    result = num1 + num2
  elif operation == "-":
    result = num1 - num2
  elif operation == "*":
    result = num1 * num2
  elif operation == "/":
    result = num1 / num2
  elif operation == "%":
     result = num1 % num2
  elif operation == "**":
     result = num1 ** num2
  return result

# TODO: Handle division/modulus by zero with try-except
try:
  result = result(num1, num2, operation)
except ZeroDivisionError:
  result = "You cannot divide by 0."

# TODO: Print result
print(result)

