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

def search_element_index(list, element):
    for index in range(len(list)):
        if(list[index] == element):
            return f"FOUND at index {index}"
    return "NOT FOUND"

print(search_element_index(list, 5))
print(search_element_index(list, 10))