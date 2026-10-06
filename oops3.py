#define a class book with the following description:
#data members
#book name
#author id
#book id
#author name
#price
#book title
#functons: member methods
#get authorid(),getauthorname(),getbooktitle(),getprice(),setauthorname(),setbooktitle(),setprice(),set
# class book:
#     def __init__(self):
#         self.bname=input("enter the book name : ")
#         self.bid=input("enter the book id :")
#         self.aid=input("enter the author id")
#         self.aname=input("enter the author name :")
#         self.price=int(input("enter the price"))
#         self.btitle=input("enter the book title :")
#     def getauthorid(self):
#         print("author id :",self.aid)
#     def getauthorname(self):
#         print("author name :",self.aname)class Course:
#
#     def __init__(self,course_name,instructor,duration):
#
#       self.course_name=course_name
#
#       self.instructor=instructor
#
#       self.duration=duration
#
#
#
#     def show_course(self):
#
#          print('coursename:',self.course_name)
#
#          print('instructor:',self.instructor)
#
#          print('duration:',self.duration)
#
#
#
# class Student(Course):
#
#
#
#     def __init__(self,course_name,instructor,duration,name,rollno,marks):
#
#        super().__init__(course_name,instructor,duration)
#
#        self.name=name
#
#        self.rollno=rollno
#
#        self.marks=marks
#
#
#
#     def show_student(self):
#
#        super().show_course()
#
#        print('studentname:',self.name)
#
#        print('rollno',self.rollno)
#
#        print('marks',self.marks)
#
#
#
#     def get_results(self):
#
#         if self.marks>=50:
#
#             print('pass',self.marks)
#
#         else:
#
#             print('fail',self.marks)
#
#
#
# # c=Course(course_name='python',instructor='anu',duration='2')
#
# # c.show_course()
#
# s=Student(name='shilpa',rollno=1,marks=55,course_name='python',instructor='anu',duration=2)
#
# s.show_student()
#
# s.get_results()
#     def getbooktitle(self):
#         print("book title is :",self.bname)
#     def getprice(self):
#         print("price :",self.price)
#     def setauthorname(self):
#         self.aname=input("Enter the new author name:")
#         self.getauthorname()
#     def setbooktitle(self):
#         self.btitle=input("Enter  the new book title :")
#         self.getbooktitle()
#     def setprice(self):
#         self.price=input("enter the new price")
#         self.getprice()
# b=book()
# b.setauthorname()
# b.setbooktitle()
# b.setprice()
#


class Course:

    def __init__(self, course_name, instructor, duration):
        self.course_name = course_name

        self.instructor = instructor

        self.duration = duration

    def show_course(self):
        print('coursename:', self.course_name)

        print('instructor:', self.instructor)

        print('duration:', self.duration)


class Student(Course):

    def __init__(self, course_name, instructor, duration, name, rollno, marks):

        super().__init__(course_name, instructor, duration)

        self.name = name

        self.rollno = rollno

        self.marks = marks

    def show_student(self):

        super().show_course()

        print('studentname:', self.name)

        print('rollno', self.rollno)

        print('marks', self.marks)

    def get_results(self):

        if self.marks >= 50:

            print('pass', self.marks)

        else:

            print('fail', self.marks)


# c=Course(course_name='python',instructor='anu',duration='2')

# c.show_course()

s = Student(name='shilpa', rollno=1, marks=55, course_name='python', instructor='anu', duration=2)

s.show_student()

s.get_results()
