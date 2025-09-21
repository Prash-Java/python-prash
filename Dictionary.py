
# Dictionary are unordered, mutable with unique keys.
# Key can be anything immutable (string, number, tuple). List cannot be a key as it is mutable.
dict = {
    "name": "Dictionary",
    "description": "A collection of key-value pairs.",
    "age" : 5,
    "is_student": False,
    12 : "twelve",
    (1, 2) : "tuple_key",
    3.14 : "pi"
}

print(dict)
print(type(dict))
print(dict["name"])
print(dict.get("description"))
print(dict.get("non_existent_key", "Default Value"))  # Using get() with default value

# Convert Dictionary keys into a list
keys_list = list(dict.keys())
print(keys_list)
print(type(keys_list))
print(len(keys_list))
print(keys_list[0])


# Dictionaries are mutable.
dict["age"] = 6  # Update value
dict["new_key"] = "New Value"  # Add new key-value pair
print(dict)
print("Keys:", dict.keys())
print("Values:", dict.values())
print("Items:", dict.items())

# Starting with null dictionary
null_dict = {}
null_dict["first_name"] = input("Enter First Name: ")
null_dict["last_name"] = input("Enter Last Name: ")
null_dict["age"] = int(input("Enter Age: "))
print(null_dict)
# Deleting key-value pair
del null_dict["age"]
print(null_dict)
# Checking if key exists
if "first_name" in null_dict:
    print("First Name exists in the dictionary.")
# Looping through dictionary
for key, value in null_dict.items():
    print(f"{key}: {value}")
# Length of dictionary
print("Length of dictionary:", len(null_dict))
# Clearing dictionary
null_dict.clear()
print("Cleared dictionary:", null_dict)
# Copying dictionary
copy_dict = dict.copy()
print("Copied dictionary:", copy_dict)

# Nested dictionary
nested_dict = {
    "person1": {
        "name": "Alice",
        "age": 30
    },
    "person2": {
        "name": "Bob",
        "age": 45
    },
    "person3": {
        "name": "Charlie",
        "age": 35
    }
}
print("Nested Dictionary:", nested_dict)
nested_dict["person1"]["age"] = 31  # Update nested value
print("Updated Nested Dictionary:", nested_dict)
# Practice with Lists and Tuples
list = [input("Enter First Subject: "), input("Enter Second Subject: "), input("Enter Third Subject: ")]
print(list) 
companies = []
companies.append(input("Enter first company: "))
companies.append(input("Enter second company: "))
companies.append(input("Enter third company: "))
print(companies)
