# my_string1 = "PythonProgramming"
# for ch in my_string1:
#     print(ch)

# my_string2 = "JavaProgramming"
# for ch in my_string2:
#     if(ch == 'P'):
#         print("Found")
# print("END")

# else cannot be used if for loop has break statement
# my_string3 = "GolangProgramming"
# for ch in my_string3:
#     if(ch == 'P'):
#         print("Found")
# else:
#     print("END")

# for ch in my_string2:
#     if(ch == 'P'):
#         print("Found")
#         break
# print("END")

# Problem 1 => Create an empty list, get the values from user and then print those values using for loop
# my_new_list = []
# my_new_list.insert(0, int(input("Enter number:")))
# my_new_list.insert(1, int(input("Enter number:")))
# my_new_list.insert(2, int(input("Enter number:")))
# my_new_list.insert(3, int(input("Enter number:")))
# my_new_list.insert(4, int(input("Enter number:")))
# my_new_list.append(int(input("Enter number:")))
# print(my_new_list)
# for element in my_new_list:
#     print(element)
# else:
#     print("END")

# Problem 1 => Create an empty tuple, get the values from user and then print those values using for loop
# my_new_tuple = []
# my_new_tuple.insert(0, int(input("Enter number:")))
# my_new_tuple.insert(1, int(input("Enter number:")))
# my_new_tuple.insert(2, int(input("Enter number:")))
# my_new_tuple.insert(3, int(input("Enter number:")))
# my_new_tuple.insert(4, int(input("Enter number:")))
# my_new_tuple.append(int(input("Enter number:")))
# print(my_new_tuple)
# for element in my_new_tuple:
#     print(element)
# Use else only when for loop does not have break statement
# else:
#     print("END")
# num = 5
# for value in my_new_tuple:
#     if(value == num):
#         print("FOUND")
# print("END")

# Range function => starts always from 0, ends at the specified position, step size for increment is 1, all these by default,
# Syntax of Range function is => range(start?, stop, stepSize?) where stop is mandatory
# sequence = range(12)
# for val in sequence:
#     print(val)
# for i in range(1, 12):
#     print(i)
# for j in range(0, 12, 1):
#     print(j)

# Print all even numbers from 1 to 100, both inclusive,
# for el in range(2, 101, 2):
#     print(el)
# 
# Print all odd numbers from 1 to 100, both inclusive,
# for ele in range(1, 100, 2):
#     print(ele)

# Print table of given number n
# num = int(input("Enter the number: "))
# for value in range(1,11):
#     print(f"{num} * {value} = ", (num * value))/

# Using pass in loops or conditional statements, essentially pass will not do anything.
# for i in range(7):
#     # empty => loop will not do anything
#     pass
# if (i > 5):
#     # empty => conditional will have no action here
#     pass

# Find sum of n numbers using while loop,
# n = int(input("Enter number: "))
# sum = 0
# i = 1
# while i <= n:
#     sum = sum + i
#     i += 1
# print("Sum = ", sum)

# Find factorial of a given number,
n = int(input("Enter number: "))
factorial = 1
for val in range(n, 0, -1):
    factorial *= val
print("Factorial = ", factorial)

