import math

# Variables and Data Types
num1 = 10
num2 = 3.14
name = "John Doe"

print("Values and types of variables:")
print("num1:", num1, "Type:", type(num1))
print("num2:", num2, "Type:", type(num2))
print("name:", name, "Type:", type(name))
print()

# User Input
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
elif 18 <= age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
print()

# Conditional Statements
def check_number(num):
    if num > 0:
        print("Positive number.")
    elif num < 0:
        print("Negative number.")
    else:
        print("Zero.")

print("Checking numbers:")
check_number(5)
check_number(-3)
check_number(0)
print()

# Loops
print("Even numbers from 0 to 20:")
for i in range(0, 21, 2):
    print(i)
print()

# Functions
def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

print("Calculating circle areas:")
radii = [1.0, 2.5, 3.0]
for r in radii:
    area = calculate_circle_area(r)
    print("Radius:", r, "Area:", area)
