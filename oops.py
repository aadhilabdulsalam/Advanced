#class classname

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is :",self.name,"age is :",self.age)
p=person('arun',32)
p.display()