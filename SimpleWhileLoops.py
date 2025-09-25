# Print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1
print(i)

# Print numbers from 100 to 1
j = 100
while j >= 1:
    print(j)
    j -= 1
print(j)

# Print table of number n
n = int(input("Enter a number to print its table: "))
multiplier = 1
while multiplier <= 10:
    print(f"{n} x {multiplier} = {n * multiplier}")
    multiplier += 1
print("Table printed successfully!")


# Print elements of a list using while loop
# [1,4,9,16,25,36,49,64,81,100]
my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
index = 0
while index <= len(my_list) - 1:
    print(my_list[index])
    index += 1
print("List printed successfully!")

# Print elements of a tuple using while loop
# (1,4,9,16,25,36,49,64,81,100)
my_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
index = 0
while index <= len(my_tuple) - 1:
    print(my_tuple[index])
    index += 1
print("Tuple printed successfully!")

# Print sum of first n natural numbers
n = int(input("Enter value of n: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i;
    i += 1
print(f"Sum of first {n} natural numbers is: {sum}")

# Print factorial of a number
n = int(input("Enter a number to find its factorial: "))
factorial = 1
i = 1
while i <= n:
    factorial = factorial * i
    i += 1
print(f"Factorial of {n} is: {factorial}")

# Search for a given number in a tuple
my_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
n = int(input("Enter a number to search in the tuple: "))
index = 0
found = False
while index <= len(my_tuple) - 1:
    if my_tuple[index] == n:
        found = True
        break
    index += 1
if found:
    print(f"{n} is present in the tuple.")
else:
    print(f"{n} is not present in the tuple.")

# Search for a given number in a list
my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
n = int(input("Enter a number to search in the list: "))
index = 0
found = False
while index <= len(my_list) - 1:
    if my_list[index] == n:
        found = True
        break
    index += 1
if found:
    print(f"{n} is present in the list.")
else:
    print(f"{n} is not present in the list.")


