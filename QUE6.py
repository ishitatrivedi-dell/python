# Create a Person class and a Student class that inherits from it. Person should have name and age. Student should add grade and override a __str__ method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    

Student_1 = Student("Alice", 20, "A")
print(Student_1)  # Output: Name: Alice, Age: 20, Grade: A