# Dictionary having list as value
dict = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal"
}
print("Dictionary:", dict)

# Sets demonstration in python
subjects_set = {"Java", "Python", "Javascript", "C++", "C", "Java", "Python", "Javascript", "C++", "C"}
print("Subjects Set:", subjects_set)  # Duplicate values are removed
print("Length of Subjects Set:", len(subjects_set))  # Length of set}

# Dictionary problems
# Problem 1: Create a dictionary to store student marks and print it.
student_marks = {}
student_marks["Java"] = (int(input("Enter marks for Java: ")))
student_marks["Python"] = (int(input("Enter marks for Python: ")))
student_marks["C++"] = (int(input("Enter marks for C++: ")))
print("Student Marks Dictionary:", student_marks)

# Set problems
# Problem 2: Create a set to store 9 and 9.0 and check its length.
number_set = {"9", "9.0"}
print("Number Set:", number_set)
print("Length of Number Set:", len(number_set))  # Length of set