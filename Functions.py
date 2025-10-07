list = [1,2,3,4,5,6]

def search_element(list, element)->str:
    for value in list:
        if(value == element):
            return "FOUND"
    return "NOT FOUND"

print(search_element(list, 5))
print(search_element(list, 10))

def search_element_in_list(list, element):
    for value in list:
        if(value == element):
            return "FOUND"
    return "NOT FOUND"

print(search_element_in_list(list, 5))
print(search_element_in_list(list, 10))

# Function to search element index in the list, if found return index else return NOT FOUND
def search_element_index(list, element):
    for index in range(len(list)):
        if(list[index] == element):
            return f"FOUND at index {index}"
    return "NOT FOUND"

print(search_element_index(list, 5))
print(search_element_index(list, 10))

print("First Value", end=" ") # end is used to avoid new line after print statement
print("Second Value", end=" ")
print("Third Value", end=" ")
print("")

def calculate_factorial(number)->int:
    factorial = 1
    for value in range(1, number+1):
        factorial = factorial * value
    return factorial
print(calculate_factorial(5))
print(calculate_factorial(6))
print(calculate_factorial(7))

def calculate_factorial_recursively(number)->int:
    if(number == 0 or number ==1):
        return 1
    return number * calculate_factorial_recursively(number - 1)
print(calculate_factorial_recursively(5))

def convert_inr_to_usd(inr)->float:
    usd = inr * 0.012
    return round(usd, 2)
print(convert_inr_to_usd(1000))
print(convert_inr_to_usd(2500))
print(convert_inr_to_usd(5000))

def convert_usd_to_inr(usd)->float:
    inr = usd * 82.0
    return round(inr, 2)
print(convert_usd_to_inr(12))
print(convert_usd_to_inr(25))
print(convert_usd_to_inr(50))

def is_even_or_odd(number)->str:
    if(number % 2 == 0):
        return "EVEN"
    else:
        return "ODD"
print(is_even_or_odd(5))
print(is_even_or_odd(10))
print(is_even_or_odd(15))
