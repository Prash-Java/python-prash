str = "hello"
print(str[1])
# Strings are immutable,
# str[1] = "y" Cannot reassign

list = ["Java", 25, "Python", "3.13"]
print(list[0])
# Lists are mutable, Can reassign,
list[3] = "3.15" 
print(len(list))
# List slicing,
print(list[0:len(list)])
print(list[:len(list)])
print(list[0:])
print(list[-4:])
# List methods,
list1 = [5,3,9,7,11,15]
list1.append(25)
print(list1)
# returns None
list1.sort() 
print(list1)
# returns None
list1.sort(reverse=True)
print(list1)
# returns None
list1.reverse()
print(list1)
list1.insert(2, 35)
print(list1)
# returns None
list1.remove(35)
print(list1)
# returns None
list1.pop(5)
print(list1)
