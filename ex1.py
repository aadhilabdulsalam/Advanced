# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input
# import math
#
# try:
#     n1=int(input("enter a number"))
#     r=math.factorial(n1)
#     print(r)
# except ValueError:
#     print("Invalid input")



# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.
# while(1):
#     print("Menu Driven Program")
#     print("1. ADDITION")
#     print("2.SUBSTRACTION  ")
#     print("3.MULTIPLICATION")
#     print("4. DIVISION")
#     print("5. Exit")
#     ch = int(input("Enter your choice :"))
#     try:
#         num1=int(input("Enter first number:"))
#         num2=int(input("Enter second number:"))
#     except:
#         print("Enter Integers only")
#     else:
#         if ch==1:
#             print(f"Sum:{num1+num2}")
#         elif ch==2:
#             print(f"Difference:{num1-num2}")
#         elif ch==3:
#             print(f"Product:{num1*num2}")
#         elif ch==4:
#             try:
#                 print(f"Division:{num1/num2}")
#             except:
#                 print("Zero division error")
#         elif ch==5:
#             exit()





# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist
try:
    f=open("abc.txt","r")
    print(f.read())
except:
    print("File does not exist")