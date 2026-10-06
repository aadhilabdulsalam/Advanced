#sum of two numbers
try:
    n1=int(input("enter 1st number"))
    n2=int(input("enter 2nd number"))
    r=n1/n2
    print(r)
except:
    print("Zero division Error")

else:
    print("No exception in normal block")
finally:
    print("Finised")