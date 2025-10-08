class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}"
    
student1 = Student("Alice", 20, "S12345")
student2 = Student("Bob", 22, "S67890")
student3 = Student("Charlie", 23, "S54321")

print(student1.display_info())
print(student2.display_info())
print(student3.display_info())