# # # # for i in range(50):
# # # #     print("hello")
# # # #     i=1
# # # #     while i<=5:
# # # #         print("RCB")
# # # def great():
# # #     print("RCB")
# # #     print("NICE")
# # # great()
# # # def add(a,b):
# # #     result = a + b
# # #     print(result)
# # # add(10,20)
# # students=["nibba","nibbi","tutti","Frutti"]
# # students.append("Punga")
# # students.remove("nibbi")
# # print(students)
# # student_details=("nibba",23,85.5,True)
# # print(student_details[0])
# # student={
# #     "name":"shiva",
# #     "age":20,
# #     "marks":89,
# #     "passed":True

# # }
# # student["course"]="python programming"
# # student["marks"]=90
# # print(student["name"],student["course"])
# # print(student["course"])
# # print(student["marks"])0
# class student:
#      def display(self):
#          print("welcome to python prog")
# s1=student()  
# s1.display()
class student:
    def __init__(self,age,name,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
            print("name:",self.name)
            print("marks",self.marks)
            print("age",self.age)
s1=student("shiva",20,89)
s1.display()

