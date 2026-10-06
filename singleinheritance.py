from asyncio import selector_events


#SINGLE INHERITANCE




# class Person:
#     def __init__(self):
#         self.name=input("enter your name")
#         self.age=int(input("enter your age"))
#     def showdetails(self):
#         print("name is :", self.name)
#         print("age is :", self.age)
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input("enter your roll no:"))
#     def studentdetils(self):
#         super().showdetails()
#         print("Roll no:",self.rollno)
# s=Student()
# s.studentdetils()




class Company():
    def __init__(self):
        self.companyname = input("enter your name")
    def showdetails(self):
        print("name is :", self.companyname)
class Employee():
    def __init__(self):
        super().__init__()
        self.Empid=int(input("Enter  the EMPID"))
        self.Designation=input("Enter your Designation")
        self.Salary=int(input("Enter your Salary"))
    def getsalary(self):
        super().getsalary()
        print("salary :",self.Salary)
    def showemployedetails(self):
        # super().showemployedetails()
        print("Employee details:",self.Empid)
        print("Desgination:",self.Designation)
        print("Salary:",self.Salary)
c=Employee()
c.showemployedetails()

