"""
Variable is a reference to an object in memory” 

Key rules
>  need to declare type
> Can change type anytime (danger + power)
> Names must be meaningful
"""

# Basic variable assignment
name = "Alish"
age = 10
is_student = True

print("Name:", name)
print("Age:", age)
print("Student:", is_student)

# Variable reassignment
age = age + 1
print("Age after one year:", age)

# Multiple assignment
city, country = "Kathmandu", "Nepal"
print("Location:", city, country)

# Swapping variables (Python-specific power)
a = 5
b = 10
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
