#write a menu-driven python program for a banking using a class
#account to perform the following operation:
#1.create an account
#2.withdraw money
#3.deposit money
#4.display balance
#5.exit


#store account details in alist and search account using the account number
#display "Account Not Found" if the account does not exist.
class Account:
    def __init__(self):
        self.accountno=int(input("enter acc no:"))
        self.accountname=input("enter account name:")
        self.balance=int(input("enter amount:"))
    def withdraw(self):
        self.amount = int(input("enter withdraw amount:"))
        self.balance-=self.amount
    def deposit(self):
        self.amount = int(input('enter deposit amount:'))
        self.balance+=self.amount
    def showbalance(self):
        print("current balance:",self.balance)
l=[]
while(1):
    print("Menu Driven Program")
    print("1. Create an Account")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Display Money")
    print("5. Exit")
    ch=int(input("Enter your choice :"))
    if ch==1:
        a=Account()
        l.append(a)

    if ch==2:
        num=int(input("Enter your Account number"))
        for i in l:
            if i.accountno==num:
                i.withdraw()
                i.showbalance()
                break
            else:
                print("Account not Found" )
    if ch==3:
        num = int(input("Enter your Account number"))
        for i in l:
            if i.accountno==num:
                i.deposit()
                i.showbalance()
                break
            else:
                print("Account not Found")

    if ch==4:
        num = int(input("Enter your Account number"))
        for i in l:
            if i.accountno==num:
                i.showbalance()
                break
            else:
                print("Account not Found")
    if ch==5:
        the 
        exit()