# By default input will always be of type string,
subject = input("Enter the subject: ")
print(type(subject), subject)
total_marks = input("Enter Total marks: ")
print(type(total_marks), total_marks)
marks_obtained = input("Enter marks obtained: ")
print(type(marks_obtained), marks_obtained)

# Type casting
subject = input("Enter the subject: ")
print(type(subject), subject)
total_marks = int(input("Enter Total marks: "))
print(type(total_marks), total_marks)
marks_obtained = float(input("Enter marks obtained: "))
print(type(marks_obtained), marks_obtained)

# Get two numbers using input() and find their sum,
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
sum = num1 + num2
print("The sum is:", sum)

# Input side of a square and print its area,
side = float(input("Enter side of square:"))
side **= 2
print("Area of square:", side)

# Get two float numbers using input() and find their avg,
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
avg = (num1 + num2) / 2
print("The average is:", avg)

# Get two numbers using input() and compare them,
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print(a>=b)

