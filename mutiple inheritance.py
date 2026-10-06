


class Hospital():
    def __init__(self):
        self.Hname=input("Enter Hospital Name:")
        self.Location=input("Enter the Location")
    def Showdetails(self):
        print("Hospitals name is ",self.Hname)
        print("Location is ",self.Location)
class Department():
    def __init__(self):
        self.Departmentname=input("Enter Your Department")
        self.Docname=input("Enter Doctor name")
    def Showdeptdetails(self):
        print("Department name :",self.Departmentname)
        print("Doctor name:",self.Docname)
class Patient(Hospital,Department):
    Hospital().__init__()
    Department().__init__()
    def __init__(self):
        self.id=input("Enter your ID:")
        self.name=input("Enter Your name")
        self.gender=input("Enter Your Gender")
        self.place=input("Enter your Place")
        self.admdate=int(input("Enter Your Admission date"))
        self.dischrdate=int(input("Enter Your Discharge date"))
    def fullsummary(self):
        print("patient name:",self.name)
        print("patient ID:",self.id)
        print("Gender :",self.gender)
        print("Place :",self.place)
        print("Adm Date:",self.admdate)
        print("Discharge Date :",self.dischrdate)
p=Patient()
p.fullsummary()


