# Find if a given number is even or odd
num = int(input("Enter the number:"))
if(num % 2 == 0):
    print("Even")
else:
    print("Odd")



# Find the largest of three given numbers
x = int(input("Enter first number:"))
y = int(input("Enter second num:"))
z = int(input("Enter third number:"))
print("First number: ", x)
print("Second number: ", y)
print("Third number: ", z)
if(x >= y and x >=z):
    print("Largest number: ", x)
elif(y > z):
    print("Largest number: ", y)
else:
    print("Largest number: ", z)



# Find if a given number is multiple of 7
num = int(input("Enter the number: "))
if(num % 7 == 0):
    print("Given number is multiple of 7")
else:
    print("Given number is not multiple of 7")