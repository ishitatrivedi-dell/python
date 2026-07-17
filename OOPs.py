

# # def a(n,a,r):
# #     name = None 
# #     age = None 
# #     roll = None 
# #     return {name : n , age : a , roll : r}

# # print(a("x", 10 , 1))

# ## que : create a class by takin input and auto assign the roll no to it 

# # class Student:
# #     roll_no = 0  # Class variable to keep track of the roll number
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #         Student.roll_no += 1  # Increment the roll number for each new student
# #         self.roll_no = Student.roll_no  # Assign the current roll number to the student

# class Student:
#     roll_no = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.roll_no += 1
#         self.roll_no = Student.roll_no

#     def display(self):
#         print(f"Roll No: {self.roll_no}")
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print()


# n = int(input("Enter the number of students: "))

# students = []

# for i in range(n):
#     print(f"\nEnter details of Student {i+1}")
#     name = input("Name: ")
#     age = int(input("Age: "))

#     s = Student(name, age)
#     students.append(s)

# print("\nStudent Details")
# for student in students:
#     student.display()


class Rai_University: 
    def __init__(self, name,age, course):
        self.name = name
        self.age = age
        self.course = course

class Coding_Gita(Rai_University):
    def __init__(self,name,age,course, mentor,attendence):
        super().__init__(name,age,course)   
        self.mentor = mentor
        self.attendence = attendence

# class College_Dekho(Rai_University, Coding_Gita):
#     def __init__(self,ac_status):
#         self.ac_status = ac_status


CG_Student_1 = Coding_Gita("Ishita", 20, "Btech", "xyz", 10)
print(CG_Student_1.name)  # Output: Ishita
print(CG_Student_1.age)  # Output: 20
print(CG_Student_1.course)  # Output: Btech
print(CG_Student_1.mentor)  # Output: xyz
print(CG_Student_1.attendence)  # Output: 10

    

class Student : 
    def __init__(self, name, roll_no):

        self.name = name
        self.roll_no = roll_no

class Employee: 
    def __init__(self, salary, emp_id):
        self.salary = salary
        self.emp_id = emp_id


class TA(Student, Employee):
    def __init__(self, name, roll_no, salary, emp_id):
        super().__init__(name, roll_no)
        Student.__init__(self, name, roll_no)
        Employee.__init__(self, salary, emp_id)