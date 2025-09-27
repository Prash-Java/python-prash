# Find a number
k = 0
while k <= 10:
    if(k == 5):
        print('Found')
        break
    print(k)
    k += 1

# Find if a number is there in a given list
my_list = [2,4,5,6,8,9]
number = 5
index = 0
count = 0
while index < len(my_list):
    if(my_list[index] == number):
        count += 1
        print("Number found at index: ", index)
        break
    index += 1
if(count == 0):
    print("Number not found")

# Find if a number is there in a given tuple
my_tuple = [2,4,5,6,8,9]
number = 5
index = 0
count = 0
while index < len(my_tuple):
    if(my_tuple[index] == number):
        count += 1
        print("Number found at index: ", index)
        break
    index += 1
if(count == 0):
    print("Number not found")
