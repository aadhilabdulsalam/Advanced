#read

f=open("k.wrt","r")
#if file does not exist it shows error
# f.read()
# content=f.read()
# content=f.readlines()
# print(content)
#1write a program to read a text file and displays the number of lines in a file
# content=f.readlines()
# print(len(content))

#write a program to display the number of words in a file
# content=f.read()
# # print(len(content.split()))
# f.close()

#write a program to update the second line in a file
# f=open("k.wrt","r")
# content=f.readlines()
# content[1]="css\n"
# f.close()
# f=open("k.wrt","w")
# f.writelines(content)
# f.close()

#write a program to display the last 5 lines in a file
# print(content[-5:])

#program to search a particular word in a file
# f=open("k.wrt","r")
# content=f.read()
# if("python" in content):
#     print('found')
# else:
#     print("not found")
# f.close()
#find the number of letters,digits,and spaces in a file
# f=open("k.wrt","r")
# content=f.read()
#
# l_count=0
# d_count=0
# s_count=0
#
# for i  in content:
#     if(i.isalpha()):
#         l_count+=1
#     elif(i.isalnum()):
#         d_count+=1
#     elif(i.isspace()):
#         s_count+=1
#     else:
#         pass
# print("numbers of string",l_count)
# print("number of digit",d_count)
# print("number of space",s_count)
f=open('total_students.txt','r')
content=f.readlines()
print('total list:',content)

u=open('passed_students.txt','r')
content=u.readlines()
print('passed list:',content)

i=open('failed_students.txt','r')
content=i.readlines()
print('failed_students:',content)
