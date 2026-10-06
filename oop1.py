#define a class named student with the following details
#data members
#sname,roll no,class,mark1,mark2,mark3
#member functions
#calculate() calculate the total and average
#studentdetails() display the details of a student with average mark
#create one object for the class and call the above member methods


class students:
    def __init__(self):
        self.name=input("enter your name")
        self.rollno=int(input("enter your roll no:"))
        self.sclass=int(input("enter your class"))
        self.mark1=int(input("enter the mark1"))
        self.mark2=int(input("enter the mark2"))
        self.mark3=int(input("enter the mark3"))