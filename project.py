import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    auth_plugin = "mysql_native_password",
    database = "govind")

mycursor=mydb.cursor(buffered=True)

def AccInsert():
    while True:
         L=[]
         Accno=int(input("Enter the Account number : "))
         L.append(Accno)
         name=input("Enter the Customer Name: ").lower
         L.append(name)
         age=int(input("Enter Age of Customer : "))
         L.append(age)
         Occup=input("Enter the Customer Occupation : ").lower()
         L.append( Occup)
         Address=input("Enter the Address of the Customer : ").lower()
         L.append(Address)
         mobileno=int(input("Enter the Mobile number : "))
         L.append(mobileno)
         Aadharno=int(input("Enter the Aadhar number : "))
         L.append(Aadharno)
         amount=float(input("Enter the Money Deposited : "))
         L.append(amount)
         AccType=input("Enter the Account Type (Saving/RD/PPF/Current) : ").lower()
         L.append(AccType)
         cust=(L)
         sql='''Insert into account(Accno ,Name,Age, occu,Address,Mobileno,Adharno,amount,AccType)
              values(%s,%s,%s, %s,%s,%s, %s,%s,%s)'''
         mycursor.execute(sql,cust)
         mydb.commit()
         ch = input('want to add more record y/n: ')
         if(ch.lower()=='n'):
             break
def AccView():
    print('select the sarch criteria:')
    print('1 account number:')
    print('2 name:')
    print('3 mobile number:')
    print('4 adhar number:')
    print('5 view all detial')

    ch = int(input('Enter the choies: '))

    if(ch==1):
        s = int(input('enter the account number'))
        rl =(s,)
        sql = "select * from account where Accno = %s"
        mycursor.execute(sql,rl)
    elif(ch==2):
        s= input('enter the name : ')
        rl=(s,)
        sql = "select * from account where Name = %s "
        mycursor.execute(sql,rl)
    elif (ch == 3):
        s = int(input('enter the mobile number : '))
        rl = (s,)
        sql = "select * from account where mobileno= %s "
        mycursor.execute(sql, rl)
    elif(ch==4):
        s=int(input('enter the adhar number: '))
        rl=(s,)
        sql = "select * from account where Adharno=%s"
        mycursor.execute(sql,rl)
    elif(ch==5):
        sql ="select * from govind.account "
        mycursor.execute(sql)
    res = mycursor.fetchall()
    print("%15s %15s %15s %15s %15s %15s %15s %15s %15s" %('AcNo', 'Name', 'Age', 'Occn', 'Add', 'Mob', 'Aadh', 'Amt', 'AccTy'))
    for i in res:
        for j in i:
            print("%15s" %j,end=' ')
        print()
def Dispsort():
    print('select the sort criteria:')
    print('1 sort by account number:')
    print('2 sort by name:')
    print('3 sort by balance:')


    ch = int(input('Enter the choies 1/2/3: '))

    if(ch==1):
        s=input('sort by asc/desc: ')
        if(s.lower()=='asc'):
            sql = "select * from account order by Accno"
        if(s.lower()=='desc') :
            sql = "select * from account order by Accno desc"

        mycursor.execute(sql)
    elif(ch==2):
        s = input('sort by asc/desc: ')
        if (s.lower() == 'asc'):
            sql = "select * from account order by Name"
        if (s.lower() == 'desc'):
            sql = "select * from account order by Name desc"
        mycursor.execute(sql)
    elif (ch == 3):
        s = input('sort by asc/desc: ')
        if (s.lower() == 'asc'):
            sql = "select * from account order by amount"
        if (s.lower() == 'desc'):
            sql = "select * from account order by amount desc"
        mycursor.execute(sql)
    res = mycursor.fetchall()
    print("%15s %15s %15s %15s %15s %15s %15s %15s %15s" %('AcNo', 'Name', 'Age', 'Occn', 'Add', 'Mob', 'Aadh', 'Amt', 'AccTy'))
    for i in res:
        for j in i:
            print("%15s" %j,end=' ')
        print()
def closeAcc():
    Accno=int(input("Enter the Account number of the Customer to be closed : "))
    rl=(Accno,)
    sql="Delete from account where Accno=%s"
    mycursor.execute(sql,rl)
    sql="Delete from account where Accno=%s"
    mydb.commit()
def updateAcc():

    sql = "select * from account"
    mycursor.execute(sql)
    A = int(input("Enter the Account number whose detail to be changed: "))
    for i in mycursor:
        i=list(i)
        if i[0]==A:
            ch = input(f"current Name is {i[1]}  want to change Name(y/n): ").lower()
            if(ch=='y'):
                 i[1]=input(f"enter name you change:").lower()
            ch = input(f"current Age is {i[2]}  want to change (y/n):").lower()
            if (ch == 'y'):
                i[2] = int(input("enter age you change: "))
            ch = input(f"current occupation is {i[3]}  want to update (y/n): ").lower()
            if (ch == 'y'):
                i[3] = input("enter occutions is you change: ").lower()
            ch = input(f"current Address is {i[4]}  want to change (y/n): ").lower()
            if (ch == 'y'):
                i[4] = input("enter your new Address : ").lower()
            ch = input(f"current mobile no. is {i[5]}  want to update(y/n): ").lower()
            if (ch == 'y'):
                i[5] = int(input("enter your new mobile no. : "))
            ch = input(f"current adhar no. is {i[6]}  want to update (y/n): ").lower()
            if (ch == 'y'):
                i[6] = int(input("enter your new adhar no. : "))
            ch =input(f"current amount is {i[7]}  want to update (y/n): ").lower()
            if (ch == 'y'):
                i[7] = float(input("enter your new Amount : "))
            ch = input(f"current account type is {i[8]}  want to change (y/n): ").lower()
            if (ch == 'y'):
                i[8] = input("enter your new account type saving/current/RD : ").lower()

            sql= " update account set Name= %s,Age=%s ,occu= %s ,Address= %s, mobileno= %s,adharno= %s,amount= %s,Acctype= %s where Accno= %s "
            val = (i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[0])
            mycursor.execute(sql,val)
            mydb.commit()
            print('account update')
            break


def accView():

    sql="select * from account"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    print("%15s %15s %15s %15s %15s %15s %15s %15s %15s" % (
    'AcNo', 'Name', 'Age', 'Occn', 'Add', 'Mob', 'Aadh', 'Amt', 'AccTy'))
    for i in res:
        for j in i:
            print("%15s" % j, end=' ')
        print()


    mydb.commit()

def MenuSet():
    print("Enter 1 : To Add Customer")
    print("Enter 2 : To sarch Customer ")
    print("Enter 3 : To sort criteria ")
    print("Enter 4 : To Close Account")
    print("Enter 5 : To Update Account")
    print("Enter 6 : To View All Customer Details")

    try:
        userInput = int(input("Please Select An Above Option: "))
    except ValueError:
        exit("\nHy! That's Not A Number")
    else:
        print("\n")
        if(userInput == 1):
            AccInsert()
        elif (userInput==2):
            AccView()
        elif (userInput==3):
            Dispsort()
        elif (userInput==4):
            closeAcc()
        elif (userInput==5):
            updateAcc()
        elif (userInput==6):
            accView()
        else:
            print("Enter correct choice. . . ")

MenuSet()
def runAgain():
    runAgn = input("\nwant To Run Again Y/n: ")
    while(runAgn.lower() == 'y'):

        MenuSet()

runAgain()
