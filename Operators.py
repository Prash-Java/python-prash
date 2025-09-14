# Arithmetic operators (+, -, *, /, %, **)
a = 5
b = 4
print("Sum: ", a + b)
print("Difference: ", a - b)
print("Product: ", a * b)
print("Quotient/Division: ", a / b)
print("Remainder:", a % b)
print("Power/Exponent: ", a ** b)

# Relational operators (>, <, >=, <=, ==)
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Logical operators (and, not, or)
val1 = True
val2 = False
print("And operation:", val1 and val2)
print("Or operation: ", val1 or val2)
print("Not operation", val1 and not val2)

# Assignment operators (=, +=, -=, /=, %=, **=)
p = 5
print(p)
p += 10
print("p + 10:", p)
p -=10
print("p - 10:", p)
p = 90
p /= 10
print("p / 10:", p)
p = 85
p %= 4
print("p % 4:", p)
p = 5
p **= 3
print("p ** 3:", p)

# Type casting
name = "Python"
version = str(3.15)
print("Programming version is:", name + version)

a = 5
b = 4.25
print("Sum:", float(a) + b)

# Input from keyboard
name = input("Enter programming name:")
print(name)