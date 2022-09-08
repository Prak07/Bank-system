import mysql.connector as con      # importing mysql
import random                      # importing random module
mycon=con.connect(host='localhost',user='root',passwd='qwerty',database='class12')      # details of the sql server 
if mycon.is_connected():           # checking the connection
    print("SUCCESSFULLY CONNECTED")
else:
    print("FAILED TO CONNECT")

print('''\n
            * * * * * * * * * * * * * * * * * * * * * * * * *
            * WELCOME TO GRINGOTTS WARZARDING BANK'S PORTAL *
            * * * * * * * * * * * * * * * * * * * * * * * * *
''')

cur=mycon.cursor()                # making cursor variable
print('\n\n')
ans=input("DO YOU HAVE AN A/C IN OUR BANK Y/N:")     # for taking the input
logged=''                                            # empty string
if ans.upper()=='Y':                                 # checking the ans
    print("\nENTER YOUR LOG IN DETAILS BELOW:\n")
    Acnumber=input("PLEASE ENTER YOUR A/C NUMBER:")
    cur.execute("Select Acnumber from ACCOUNT_DETAILS ")
    data=cur.fetchall()
    while (Acnumber,) not in data:                   # using whlie loop 
        print()
        print("!! PLS ENTER THE CORRECT A/C NUMBER !!\n")
        Acnumber=input("ENTER YOUR A/C NUMBER:")
    else:                                            # esle for while loop
        print()
        Pin=int(input("ENTER YOUR 4 DIGIT PIN:"))
        cur.execute("select Pin from ACCOUNT_DETAILS where Acnumber='%s'" %(Acnumber,))
        data=cur.fetchone()
        while Pin not in data:                       # using whlie loop
            print("\n!! WRONG PIN !!\n")
            Pin=int(input("ENTER YOUR 4 DIGIT PIN AGAIN:"))
        else:                                        # esle for while loop
            print('''\n
* * * * * * * * * * * * * *
* SUCCESSFULLY LOGGED IN  *
* * * * * * * * * * * * * * 
''')        
            logged='Y'
elif ans.upper()=='N':                               # elif condition
    ans=input("\nDO YOU WANT TO CREATE AN A/C IN OUR BANK? Y/N:")
    if ans.upper()=='Y':
        print("\nOK ENTER YOUR DETAILS BELOW:")
        name=input("\nENTER YOUR FIRST NAME ONLY:")
        age=int(input("\nENTER YOUR AGE:"))
        if age<18:                                   # user must not be aboe 18
            logged='N'
            print("\n---- SORRY YOU CAN'T OPEN AN ACCOUNT IN OUR BANK IF YOU ARE BELOW 18 !!!! ----")

        else:
            Actype=input("\nCHOOSE YOUR A/C TYPE 1.SAVINGS/2.CURRENT:")
            if Actype=='1':
                Actype='SAVINGS'
            elif Actype=='2':
                Actype='CURRENT'
            else:
                Actype='SAVINGS'
            phnumber=input('\nENTER YOUR 10 DIGIT PHONE NUMBER:')
            cur.execute("Select Phone_no from ACCOUNT_DETAILS")
            data=cur.fetchall()
            while len(phnumber)!=10 or phnumber.isdigit()!=True or (phnumber,) in data:          # cheking two conditions in loop
                print("\n----- INVALID PHONE NUMBER OR A/C WITH THIS PHONE NUMBER ALREADY EXISTS IN OUR BANK----")
                phnumber=input('\nENTER YOUR 10 DIGIT PHONE NUMBER:')
            Pin=int(input("\nENTER A FOUR DIGIT PIN:"))
            while len(str(Pin))!=4:
                print("\n----- INVALID PIN ----")
                Pin=int(input("\nENTER A FOUR DIGIT PIN:"))
            Acnumber=random.randint(10000000000,99999999999)
            print('\nYOUR ACCOUNT NUMBER IS',Acnumber)
            cur.execute("INSERT INTO ACCOUNT_DETAILS VALUES('%s','%s',%s,%s,'%s',%s,%s)" %(Acnumber,name.upper(),age,0,Actype.upper(),phnumber,Pin))
            mycon.commit()                  # updating the table
            print("\n\n -------- CONGRATULATIONS !! YOUR A/C SUCCESSFULLY ADDED IN OUR BANK --------")
            print('''\n
                * * * * * * * * * * * * * * * * * *
                * THANK YOU FOR CHOOSING OUR BANK *
                * * * * * * * * * * * * * * * * * *''')
            logged=input("\nDO YOU WANT TO CONTINUE Y/N:")
    elif ans.upper()=='N':
        logged='N'


if logged.upper()=='Y':     # it will execute when the condition is true
    choice='1'
    while choice!='8':      # Using While loop for taking choice of the user
        print('''
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            *             WELCOME TO GRINGOTTS WARZARDING BANK'S PORTAL             *
            *                                                                       *
            *                                                                       *
            *         * * * * * * *                           * * * * * * * *       *
            *         * 1.DEPOSIT *                           * 2.WITHDRAWL *       *
            *         * * * * * * *                           * * * * * * * *       *
            *                                                                       *
            *                                                                       *
            *       * * * * * * * * *                      * * * * * * * * * * *    *
            *       * 3.A/C DETAILS *                      * 4.TRANSFER MONEY  *    *
            *       * * * * * * * * *                      * * * * * * * * * * *    *
            *                                                                       *
            *                                                                       *
            *       * * * * * * * * *                    * * * * * * * * * * * * *  *
            *       * 5.PIN CHANGE  *                    * 6.PHONE NUMBER CHANGE *  *
            *       * * * * * * * * *                    * * * * * * * * * * * * *  *
            *                                                                       *
            *                        * * * * * * * * * * *                          *
            *                        * 7.REMOVE YOUR A/C *                          *
            *                        * * * * * * * * * * *                          *
            *                                                                8.EXIT *
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
''')

        choice=input('''
* * * * * * * * * * * * * * *
* PLEASE ENTER YOUR CHOICE  *
* * * * * * * * * * * * * * *
HERE;''')
        if choice=='1':             # choice for depositing the amount
            print('''
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            * YOU CAN ONLY DEPOSIT 100 , 500 AND 2000 RUPEES NOTES  * 
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * *''' )
            Hundred_Note=int(input("\nHOW MANY 100 RUPEES NOTES:"))
            FiveHundred_Note=int(input("\nHOW MANY 500 RUPEES NOTES:"))
            Twothousand_Note=int(input("\nHOW MANY 2000 RUPEES NOTES:"))
            print()  
            print("100 * ",Hundred_Note," = " ,Hundred_Note*100)
            print("500 * ",FiveHundred_Note," = " ,FiveHundred_Note* 500)
            print("2000 * ", Twothousand_Note, " = ", Twothousand_Note*2000)
            sum_amount=Hundred_Note*100+FiveHundred_Note* 500 +Twothousand_Note*2000
            print('''
-----------------------
TOTAL AMOUNT  IS :''',sum_amount,'''
-----------------------
''')
            print('''
            * * * * * * * * * * * * * * * * * *
            * YOUR TRANSACTION IS SUCCESSFULL *
            * * * * * * * * * * * * * * * * * *
            ''')
            cur.execute("Select Balance from ACCOUNT_DETAILS where Acnumber='%s'"%(Acnumber,))
            data=cur.fetchone()
            for bal in data:            # adding the amount 
                bal+=sum_amount
            cur.execute("UPDATE ACCOUNT_DETAILS SET Balance=%s where Acnumber='%s'"%(bal,Acnumber))
            mycon.commit()                  # updating the table
            know_balance=input("\nDO YOU WANT TO KNOW YOUR BALANCE Y/N:")
            if know_balance.upper()=='Y':           # For knowing balance
                print("\nYOUR CURRENT BALANCE IS : Rs.",bal)
            else:
                pass
            logged=input("\nDO YOU WANT TO CONTINUE Y/N:")          # checking if the user want to continue or not
            if logged.upper() == 'Y':
                continue
            else:
                choice='8'



        elif choice=='2':               # choice for widthrawing the amount
            Amount=int(input("\nPLEASE ENTER THE AMOUNT TO BE WIDTHDRAWN:")) 
            cur.execute("Select Balance from ACCOUNT_DETAILS where Acnumber='%s'"%(Acnumber,))
            data=cur.fetchone()
            for bal in data:
                if bal<Amount:    
                    print('''\n
            * * * * * * * * * * * * * * * * * * * * * * * * *
            * THERE IS INSUFFICIENT BALANCE IN YOUR ACCOUNT *
            * * * * * * * * * * * * * * * * * * * * * * * * * ''')
                    know_balance=input("\nDO YOU WANT TO KNOW YOUR BALANCE Y/N:")
                    if know_balance.upper()=='Y':           # For knowing balance
                        print("\nYOUR CURRENT BALANCE IS : Rs.",bal)
                    else:
                        pass
                    logged=input("\nDO YOU WANT TO CONTINUE Y/N:")
                    if logged.upper() == 'Y':       # checking if the user want to continue or not
                        continue
                    else:
                        choice='8'

                else:    
                    for bal in data:   # Deducting balance
                        bal-=Amount
                    print('''
            * * * * * * * * * * * * * * * * * *
            * YOUR TRANSACTION IS SUCCESSFULL *
            * * * * * * * * * * * * * * * * * *
            ''')
                    cur.execute("UPDATE ACCOUNT_DETAILS SET Balance=%s where Acnumber='%s'"%(bal,Acnumber))
                    mycon.commit()                  # updating the table
                    know_balance=input("\nDO YOU WANT TO KNOW YOUR BALANCE Y/N:")
                    if know_balance.upper()=='Y':           # For knowing balance
                        print("\nYOUR CURRENT BALANCE IS : Rs.",bal)
                    else:
                        pass
                    logged=input("\nDO YOU WANT TO CONTINUE Y/N:")
                    if logged.upper() == 'Y':
                        continue
                    else:
                        choice='8'

        elif choice=='3':               # choice for showing the details
            cur.execute("Select * from ACCOUNT_DETAILS where Acnumber='%s'"%(Acnumber,))
            data=cur.fetchone()
            Acnumber=data[0]
            name=data[1]
            age=data[2]
            bal=data[3]
            Actype=data[4]
            phnumber=data[5]
            print('''\n
        * * * * * * * * * * * * * * * * * * * * *
        * YOUR ACCOUNT DETAILS ARE GIVEN BELOW  *
        * * * * * * * * * * * * * * * * * * * * * ''')
            print('\n')
            print("\tA/C NUMBER     =   ",data[0])
            print("\tNAME           =   ",data[1])
            print("\tAGE            =   ",data[2])
            print("\tBALANCE        =   ",data[3])
            print("\tA/C TYPE       =   ",data[4])
            print("\tPHONE NUMBER   =   ",data[5])
            print("\tPIN            =   ",data[6])
            logged=input("\n\nDO YOU WANT TO CONTINUE Y/N:")
            if logged.upper() == 'Y':       # checking if the user want to continue or not
                continue
            else:
                choice='8'

        elif choice=='4':               # choice for transferring the money
            print(''''
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            * YOU CAN TRANSFER MONEY TO A PERSON WHO IS HAVING AN A/C IN OUR BANK *
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *''')
            Account_No_Receiver=input("\nENTER ACCOUNT NUMBER OF THE RECIEVER:")
            if Account_No_Receiver==Acnumber:
                print("\n!! PLEASE ENTER THE A/C NUMBER OF THE RECEIVER NOT YOURS !!")
                Account_No_Receiver=input("\nENTER ACCOUNT NUMBER OF THE RECIEVER:")
            cur.execute("Select Acnumber from ACCOUNT_DETAILS ")
            data=cur.fetchall()
            while (Account_No_Receiver,) not in data: 
                print()
                print("!! PLS ENTER THE CORRECT A/C NUMBER !!\n")
                Account_No_Receiver=input("ENTER ACCOUNT NUMBER OF THE RECIEVER:")

            Transfer_Amount=int(input("\nENTER AMOUNT TO BE TRANSFERRED:"))
            cur.execute("Select Balance from ACCOUNT_DETAILS where Acnumber='%s'"%(Acnumber,))
            data=cur.fetchone()
            for bal in data:
                if bal<Transfer_Amount:    
                    print('''\n
            * * * * * * * * * * * * * * * * * * * * * * * * *
            * THERE IS INSUFFICIENT BALANCE IN YOUR ACCOUNT *
            * * * * * * * * * * * * * * * * * * * * * * * * * ''')
                    know_balance=input("\nDO YOU WANT TO KNOW YOUR BALANCE Y/N:")
                    if know_balance.upper()=='Y':           # For knowing balance
                        print("\nYOUR CURRENT BALANCE IS : Rs.",bal)
                    else:
                        pass
                    logged=input("\nDO YOU WANT TO CONTINUE Y/N:")        
                    if logged.upper() == 'Y':       # checking if the user want to continue or not
                        continue
                    else:
                        choice='8'

                else:    
                    for bal in data:   # Deducting balance
                        bal-=Transfer_Amount
                    cur.execute("Select Balance from ACCOUNT_DETAILS where Acnumber='%s'"%(Account_No_Receiver,))
                    data=cur.fetchone()
                    for bal_receiver in data:     # adding the amount to the recepient
                        bal_receiver+=Transfer_Amount
                    print('''
            * * * * * * * * * * * * * * * * * *
            * YOUR TRANSACTION IS SUCCESSFULL *
            * * * * * * * * * * * * * * * * * *
            ''')
                    cur.execute("UPDATE ACCOUNT_DETAILS SET Balance=%s where Acnumber='%s'"%(bal,Acnumber))
                    mycon.commit()              # updating the table
                    cur.execute("UPDATE ACCOUNT_DETAILS SET Balance=%s where Acnumber='%s'"%(bal_receiver,Account_No_Receiver))
                    mycon.commit()              # updating the table
                    know_balance=input("\nDO YOU WANT TO KNOW YOUR BALANCE Y/N:")
                    if know_balance.upper()=='Y':           # For knowing balance
                        print("\nYOUR CURRENT BALANCE IS : Rs.",bal)
                    else:
                        pass
                    logged=input("\nDO YOU WANT TO CONTINUE Y/N:")
                    if logged.upper() == 'Y':
                        continue
                    else:
                        choice='8'
                
        elif choice=='5':               # choice for changing the pin
            Pin=int(input("\nENTER YOUR CURRENT PIN:"))
            cur.execute("Select Pin from ACCOUNT_DETAILS where Acnumber='%s'"%(Acnumber,))
            data=cur.fetchone()
            while Pin not in data:
                print("\n!! WRONG PIN !!\n")
                Pin=int(input("ENTER YOUR CURRENT PIN:"))
            New_Pin=int(input("\nENTER YOUR NEW 4 DIGIT PIN:"))
            while len(str(New_Pin))!=4:
                print("\n----- INVALID PIN ----")
                New_Pin=int(input("\nENTER A FOUR DIGIT PIN:"))
            New_Pin_=int(input("\nRE-ENTER YOUR NEW PIN:"))
            while New_Pin!=New_Pin_:
                print('''\n
            * * * * * * * * * * * * * * * * * * * * * *
            * !! YOUR RE-ENTERED PIN DOSEN'T MATCH !! *
            * * * * * * * * * * * * * * * * * * * * * *
            ''')
                New_Pin_=int(input("\nRE-ENTER YOUR NEW PIN:"))

            else:
                cur.execute("UPDATE ACCOUNT_DETAILS SET Pin=%s where Acnumber='%s'"%(New_Pin_,Acnumber))
                mycon.commit()              # updating the table
                print('''\n
            * * * * * * * * * * * * * * * * * * *
            * YOUR PIN IS CHANGED SUCCESSFULLY  *
            * * * * * * * * * * * * * * * * * * *
            ''')
            logged=input("\nDO YOU WANT TO CONTINUE Y/N:")
            if logged.upper() == 'Y':       # checking if the user want to continue or not
                    continue
            else:
                choice='8'
        

        elif choice=='6':                   # choice for changing the number
            phnumber=input("\nENTER YOUR CURRENT PHONE NUMBER:")
            cur.execute("Select Phone_no from ACCOUNT_DETAILS where Acnumber='%s'"%(Acnumber,))
            data=cur.fetchone()
            while len(phnumber)!=10 or phnumber not in data:
                print("\n!! INVALID PHONE NUMBER OR THIS PHONE NUMBER IS NOT RELATED WITH YOUR ACCOUNT !!")
                phnumber=input('\nENTER YOUR 10 DIGIT PHONE NUMBER:') 


            New_Ph_num=input("\nENTER YOUR NEW PHONE NUMBER:")
            cur.execute("Select Phone_no from ACCOUNT_DETAILS")
            data=cur.fetchall()
            while  len(New_Ph_num)!=10 or (New_Ph_num,) in data:
                print("\n!! INVALID PHONE NUMBER OR A/C WITH THIS PHONE NUMBER ALREADY EXISTS IN OUR BANK !!")
                New_Ph_num=input('\nENTER YOUR NEW 10 DIGIT PHONE NUMBER:')

            New_Ph_num_=input("\nRE-ENTER YOUR NEW PHONE NUMBER:")
            while New_Ph_num!=New_Ph_num_:
                print('''\n
            * * * * * * * * * * * * * * * * * * * * * * * * * * *
            * !! YOUR RE-ENTERED PHONE NUMBER DOSEN'T MATCH !!  *
            * * * * * * * * * * * * * * * * * * * * * * * * * * *
            ''')
                New_Ph_num_=input("\nRE-ENTER YOUR NEW PHONE NUMBER:")

            else:
                cur.execute("UPDATE ACCOUNT_DETAILS SET Phone_no='%s' where Acnumber='%s'"%(New_Ph_num_,Acnumber))
                mycon.commit()                      # updating the table
                print('''\n
            * * * * * * * * * * * * * * * * * * * * * * *
            * YOUR PHONE NUMBER IS CHANGED SUCCESSFULLY *
            * * * * * * * * * * * * * * * * * * * * * * *
            ''')
            logged=input("\nDO YOU WANT TO CONTINUE Y/N:")      
            if logged.upper() == 'Y':       # checking if the user want to continue or not
                continue
            else:
                choice='8'
        
        elif choice=='7':               # choice for removing the account from the bank
            ans=input("\nARE YOU SURE YOU WANT TO REMOVE YOURE A/C FROM OUR BANK Y/N:")
            if ans.upper()=='Y':
                cur.execute("Delete from ACCOUNT_DETAILS where Acnumber='%s'"%(Acnumber,))
                mycon.commit()              # updating the table
                print('''\n
            * * * * * * * * * * * * * * * * * * * * * * * * * *
            * YOUR A/C WAS SUCCESSFULLY REMOVED FROM OUR BANK *
            * * * * * * * * * * * * * * * * * * * * * * * * * *
            ''')
                print('''\n
            * * * * * * * * * * * * * * * * * * * * * * *
            * WE APOLOGIZE FOR ANY MISTAKE WE HAVE DONE *
            * * * * * * * * * * * * * * * * * * * * * * *''')
                choice='8'
            else:
                print("\n!! THANK YOU FOR CHANGING YOUR DECISION AND STAYING IN OUR BANK !!")            
                logged=input("\nDO YOU WANT TO CONTINUE Y/N:")
                if logged.upper() == 'Y':       # checking if the user want to continue or not
                    continue
                else:
                    choice='8'
        
        elif choice=='8':           # choice for exiting the portal           
            break
        else:
            print('''\n
            * * * * * * * * * * * * * * * * * * * * *
            * PLEASE CHOOSE FROM THE GIVEN CHOICES  *
            * * * * * * * * * * * * * * * * * * * * *
            ''')

    print('''\n
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            * THANK YOU FOR VISITING GRINGOTTS WARZARDING BANK'S PORTAL *
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
''')
else:               # printing if the choice is no
    print('''\n
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            * THANK YOU FOR VISITING GRINGOTTS WARZARDING BANK'S PORTAL *
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
''')
mycon.close()