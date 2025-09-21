# Sets are always unique and unordered collections of items. They are mutable, but the items contained within must be immutable.
# Sets are unordered, mutable with unique items.
# Sets do not allow duplicate values.
# Sets never stores Lists or Dictionaries as they are mutable.

collection = {1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, "hello", (1, 2, 3), 3.14, True, False, 1}  # Duplicate values will be removed
print(collection) # Duplicate values are removed
print(type(collection))
print(len(collection))  # Length of set
# Creating an empty set
empty_set = set()  # Using set() to create an empty set, as {} creates an empty dictionary
print(empty_set)
print(type(empty_set))
print(len(empty_set))
empty_set.add(1)  # Adding an item to the set
empty_set.add(2)  # Adding another item to the set
empty_set.add(2)  # Adding duplicate item, will not be added
print(empty_set)
print("Length of set after additions:", len(empty_set))
print("Is 1 in set?", 1 in empty_set)  # Checking membership
print("Is 3 in set?", 3 in empty_set)  # Checking membership
empty_set.remove(2)  # Removing an item from the set, will raise KeyError
print(empty_set)
empty_set.discard(3)  # Removing an item that doesn't exist, will not raise error
print(empty_set)
empty_set.add((1, 2))  # Adding a tuple, which is immutable
empty_set.add("world")  # Adding a string, which is immutable
empty_set.add(3.14)  # Adding a float, which is immutable
empty_set.add(False)  # Adding a boolean, which is immutable
empty_set.add(2)  # Adding back an item
empty_set.add(3)  # Adding another item
print(empty_set)
print(empty_set.pop())  # Removing and returning an arbitrary item
empty_set.clear()  # Clearing the set
print("Cleared set:", empty_set)
print("Length of cleared set:", len(empty_set))

# Union of two sets like mathematics,
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)  # Using union() method
print("Union using union():", union_set)
union_set2 = set1 | set2  # Using | operator
print("Union using | operator:", union_set2)
print("Set1 remains unchanged:", set1)
print("Set2 remains unchanged:", set2)

# Intersection of two sets like mathematics
intersection_set = set1.intersection(set2)  # Using intersection() method
print("Intersection using intersection():", intersection_set)
intersection_set2 = set1 & set2  # Using & operator
print("Intersection using & operator:", intersection_set2)
print("Set1 remains unchanged:", set1)
print("Set2 remains unchanged:", set2)


