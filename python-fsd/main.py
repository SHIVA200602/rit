
# # # # class Student:
# # # #     def __init__(self, usn, name, marks):
# # # #         self.usn = usn
# # # #         self.name = name
# # # #         self.marks = marks

# # # #     def display(self):
# # # #         print("USN:", self.usn)
# # # #         print("Name:", self.name)
# # # #         print("Marks:", self.marks)
# # # #         print("-------------------")

# # # # class StudentManagement:
# # # #     def __init__(self):
# # # #         self.students = []

# # # #     def add_student(self):
# # # #         usn = input("Enter USN: ")

# # # #         for student in self.students:
# # # #             if student.usn == usn:
# # # #                 print("USN already exists!")
# # # #                 return

# # # #         name = input("Enter student name: ")
# # # #         marks = float(input("Enter marks: "))

# # # #         new_student = Student(usn, name, marks)
# # # #         self.students.append(new_student)

# # # #         print("Student added successfully!")

# # # #     def view_student(self):
# # # #         if len(self.students) == 0:
# # # #             print("No students found!")
# # # #             return

# # # #         for student in self.students:
# # # #             student.display()

# # # #     def search_student(self):
# # # #         usn = input("Enter USN to search: ")

# # # #         for student in self.students:
# # # #             if student.usn == usn:
# # # #                 print("Student found!")
# # # #                 student.display()
# # # #                 return

# # # #         print("Student not found!")

# # # #     def delete_student(self):
# # # #         usn = input("Enter USN to delete: ")

# # # #         for student in self.students:
# # # #             if student.usn == usn:
# # # #                 self.students.remove(student)
# # # #                 print("Student deleted!")
# # # #                 return

# # # #         print("Student not found!")

# # # # app = StudentManagement()

# # # # while True:
# # # #     print("\n======= Student Management System =======")
# # # #     print("1. Add Student")
# # # #     print("2. View Students")
# # # #     print("3. Search Student")
# # # #     print("4. Delete Student")
# # # #     print("5. Exit")

# # # #     choice = input("Enter your choice: ")

# # # #     if choice == "1":
# # # #         app.add_student()

# # # #     elif choice == "2":
# # # #         app.view_student()

# # # #     elif choice == "3":
# # # #         app.search_student()

# # # #     elif choice == "4":
# # # #         app.delete_student()

# # # #     elif choice == "5":
# # # #         print("Thank you for using the application!")
# # # #         break

# # # #     else:  
# # # #         print("Invalid choice! Try again.")
# # # class student:
# # #     def __init__(self):
# # #         self.__marks=0
# # #     def set_marks(self,marks):
# # #         self.__marks=marks
# # #     def show_marks(self):
# # #         print("student marks:",self.__marks)
# # #         s1=student()
# # #         s1.set_marks(85.5)
# # #         s1.show_marks()
# # # class grandfather:
# # #     def land(self):
# # #         print("grandfather has land")
# # # class father(grandfather):
# # #     def house(self):
# # #         print("father has a house")
# # # class uncle(grandfather):
# # #     def car(self):
# # #         print("uncle has a car")
# # # f=father()
# # # u=uncle()
# # # f.house()
# # # f.land()
# # # u.land()
# # # u.car()
# # class Father():
# #     def house(self):
# #         print("Father has a house")
# # class Mother():
# #     def gold(self):
# #         print("Mother has gold")
# # class son(Father,Mother):
# #     pass
# # s=son()
# # s.house()
# # s.gold()
# class dog():
#     def sound(self):
#         print("dog makes a sound as bow bow")
# class cat():
#     def sound(self):
#         print("cat makes a sound as meow")
# class cow():
#     def sound(self):      
#         print("cow makes sound as moo")
# d=dog()
# c=cat()
# co=cow()
# d.sound()
# c.sound()
# co.sound()
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(Animal):
    def sound(self):
        print("the dog barks")
d=dog()
d.sound()

