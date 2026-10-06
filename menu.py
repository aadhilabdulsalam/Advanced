
def file_read():
    file_name=input("Enter The filename")
    f=open(file_name,"r")
    content=f.read()
    print(content)
def file_write():
    name=input("enter the file name:")
    f=open(name,'w')
    content=input("enter the content to write:")
    f.write(content)

def file_append():
    name=input("enter the file name:")
    f=open(name,'a')
    content=input("enter the content to write:")
    f.write(content)

def file_search():
    name=input("enter the file name:")
    f=open(name,"r")
    content=f.read()
    se=input("enter the word:")
    if se in content:
        print("present")
    else:
        print("not present")

def file_remove():
    import os
    name=input("enter the file name:")
    os.remove(name)
while(1):
    print("Menu Driven-File Operation")
    print('1.File Read')
    print('2.File Write')
    print('3.File Append')
    print('4.File Search')
    print('5.File Remove')
    print('6.Exit')

    bu=int(input("enter your choice"))
    if bu==1:
        file_read()
    elif bu==2:
        file_write()
    elif bu==3:
        file_append()
    elif bu==4:
        file_search()
    elif bu==5:
        file_remove()
    else:
        exit()
