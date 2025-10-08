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


class Employees:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average_marks(self):
        return (self.marks1 + self.marks2 + self.marks3) /3
    
employee = Employees("David", 90, 85, 95)
print(f"Employee Name: {employee.name}, Average Marks: {employee.average_marks()}")


class Emp:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)
    
    @staticmethod
    def hello():
        print("Hello from Emp class")
    
emp = Emp("David", [90, 85, 95])
print(f"Employee Name: {emp.name}, Average Marks: {emp.average_marks()}")
Emp.hello()
