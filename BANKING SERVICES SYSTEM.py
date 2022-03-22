# BADRUL HAIKAL IMAN
# TP061466
# Super Class : User
# Has a function to show user details
# Enter the customer details into the system
# Perform deposit and withdrawal using account number and password

import datetime
import sys

#THIS IS THE FUNCTION THAT I USE TO DO MAIN MENU THAT SHOWS SUPERUSER,ADMIN, AND CUSTOMER.
def MainMenu():
    print ('                              >>>>MAIN MENU<<<<                             ')
    print ('                       >>>>>WELCOME TO BADRUL BANK<<<<<                     ')
    print ()
    print ()
    print ()
    print (' [1] Super User')
    print (' [2] Admin')
    print (' [3] Customer')
    choice = input("Enter choice: ")


    if choice in ('1','2','3'):

        if choice == '1':
            UserID = input("Enter SUID: ")
            Password = input("Enter SU password: ")
            while UserID!='SUPERUSER1' or Password!='1234567' :
                print ('Access denied')
                UserID = input("Enter SUID: ")
                Password = input("Enter SU password: ")
            AdminAcc()
            
                                

        elif choice == '2':
            print ('                            >>>>ADMIN MENU<<<<                            ')
            print ()
            print ()
            print ()
            AdminID = input("Enter AdminID:")
            Password = input("Enter Admin Password: ")
            while AdminID!='ADMIN1' or Password!='1234567' :
                print ('Access denied')
                AdminID = input("Enter AdminID:")
                Password = input ("Enter Admin password: ")
            registerclient()
            SavingOrCurrent()  
            
                
        
        elif choice == '3':
            print ('                            >>>>CLIENT MENU<<<<                            ')
            print ()
            print ()
            print ()
            print (' [1]SAVING ACC')
            print (' [2]CURRENT ACC')
            choice = input("Enter choice: ")
            if choice in ('1','2'):
                if choice == '1':
                    AccNumber = input("Enter AccNumber:")
                    Password = input("Enter Client Password: ")
                    while AccNumber!='0000,0000,0000,0001' or Password!='1234567' :
                        print ('Access denied')
                        AccNumber = input("Enter AccNumber: ")
                        Password = input ("Enter Client password: ")
                    Savingdepositorwithdraw() 
                    SavingStatementOfAccount() 
                
                elif choice == '2':
                    AccNumber = input("Enter AccNumber:")
                    Password = input("Enter Client Password: ")
                    while AccNumber!='0000,0000,0000,0001' or Password!='1234567' :
                        print ('Access denied')
                        AccNumber = input("Enter AccNumber: ")
                        Password = input ("Enter Client password: ")
                    Currentdepositorwithdraw()
                    CurrentStatementOfAccount()

#THIS FUNCTION IS FOR REGISTER ADMIN ACCOUNT ON THE SYSTEM            
def AdminAcc():
    print('                            >>>>ADMIN REGISTERATION MENU<<<<                            ')
    print()
    print()
    print()
    print("[1] REGISTER ADMIN ACCOUNT")
    print("[2] CHECK ADMIN SETTING")
    print("[3] ADMIN DATA VALIDATION")
    print("[4] RETURN TO MAIN MENU")
    print("[5] EXIT.")
    choice = input("Enter Choice: ")
    if choice in ('1','2','3','4','5'):   
        if choice == '1':
            AA = open("AdminDatabase.txt","r")
            AdminID = input("Create AdminID:")
            AdminID1 = input("Enter AdminID again:")
            Name = input("Enter Name:")
            Password = input("Create Password:")

            if AdminID != AdminID1:
                print("AdminID don't match, restart")
                AdminAcc()

            else:
                if len(Name)<=2:
                    print("name too short, restart:")
                    AdminAcc()

                else:
                    AA = open("AdminDatabase.txt","a")
                    AA.write(AdminID+"\n "+Name+"\n "+Password+"\n")
                    print("Success!")
                    print('Admin Account Created Successfully')
                    AdminAcc()
                    
        
        elif choice == '2':
            fh = open('AdminDatabase.txt','r')
            print(fh.read())
            return AdminAcc()
        
        elif choice == '3':
            fh = open('AdminDatabase.txt','r')
            word = input("Enter the word to search:")
            b = " "
            count=1
            
            while(b):
                b=fh.readline()
                C=b.split()
                if word in C:
                    print("Line Number:",count,":",b)
                count+=1
                return AdminAcc()
        
        elif choice == '4':
            MainMenu()

        elif choice == '5': 
            sys.exit()           

#THIS LINE IS A FUNCTION FOR REGISTER CLIENT INFORMATION INTO THE SYSTEM
def registerclient():
    print('                            >>>>CLIENT REGISTERATION MENU<<<<                            ')
    print()
    print()
    print()
    print("[1] REGISTER CLIENT ACCOUNT")
    print("[2] CREATE SAV OR CUR ACCOUNT")
    print("[3] CHANGE PASSWORD FOR SAV ACC")
    print("[4] CHANGE PASSWORD FOR CUR ACC")
    print("[5] CHECK USER SETTING")
    print("[6] USER DATA VALIDATION")
    print("[7] RETURN TO MAINMENU")
    print("[8] EXIT")
    choice = input("Enter Choice: ")
    if choice in ('1','2','3','4','5','6','7','8'):   
        if choice == '1':
            CA = open("ClientDatabase.txt","r")
            clientID = input("Create clientID:")
            clientID1 = input("Enter clientID again:")
            Name = input("Enter Name:")
            Age = input("Enter Age:")
            IdentificationCard = input("Enter IdentificationCard:")
            ContactNumber = input("Enter ContactNumber:")
            Address = input("Enter Address:")
            DateOfBirth = input("Enter DateOfBirth:")

            
            if clientID != clientID1:
                print("ClientID don't match, restart")
                registerclient()
            
            else:
                if len(Name)<=2:
                    print("name too short, restart:")
                    registerclient()

                else:
                    CA = open("ClientDatabase.txt","a")
                    CA.write(clientID+"\n "+Name+"\n "+Age+"\n "+IdentificationCard+"\n "+ContactNumber+"\n "+Address+"\n "+DateOfBirth+"\n")
                    print("Success!")
                    registerclient()

        elif choice == '2':
            SavingOrCurrent()
            return registerclient()
        
        elif choice == '3':
            savchangepass('logdetails')
            return MainMenu()

        elif choice == '4':
            curchangepass('logdetails')
            return MainMenu()
        
        elif choice == '5':
            fh = open('ClientDatabase.txt','r')
            print(fh.read())
            return registerclient()
        
        elif choice == '6':
            fh = open('ClientDatabase.txt','r')
            word = input("Enter the word to search:")
            b = " "
            count=1
            
            while(b):
                b=fh.readline()
                C=b.split()
                if word in C:
                    print("Line Number:",count,":",b)
                count+=1
                return MainMenu()
        
        elif choice == '7':
            MainMenu()
        
        elif choice == '8':
            sys.exit()

#THIS FUNCTION IS TO DO TRANSACTION ON SAVING ACCOUNT EITHER DEPOSIT OR WITHDRAWAL        
def Savingdepositorwithdraw():
    print('                            >>>>SAVING TRANSACTION MENU<<<<                            ')
    print()
    print()
    print()
    print("Select option to continue")
    print("[1] Do you wish to deposit")
    print("[2] Do you wish to withdraw")
    choice = input("Enter Choice: ")
    if choice in ('1','2'):   
        if choice == '1':
                #reading file
                balance_file = open("savingbalance.txt", "r")
                #reading account balance
                account_balance = float(balance_file.readline())
                balance_file.close()
                #printing account balance
                print("Your current balance is $%.2f" % (account_balance))
                #input for deposit amount
                deposit_amount = float(input("How much money do you wish to deposit? "))
                #printing deposit amount
                print("You deposited $%.2f" % (deposit_amount))
                #calculate final account balance 
                account_balance = account_balance + deposit_amount
                #storing balance after deposit in a file
                deposit_file = open("savingdeposit.txt", "w")
                deposit_file.write(str(account_balance))
                deposit_file.close()
                #printing deposit
                print("Your new balance is $%.2f" % (account_balance))
                #call function Savingdepositorwithdraw
                return Savingdepositorwithdraw()
                
        
        elif choice == '2':
            #reading file
            balance_file = open("savingdeposit.txt", "r")
            #reading account balance
            account_balance = float(balance_file.readline())
            print("You are not permitted to withdraw")    
            balance_file.close()
            #printing account balance
            print("Your current balance is $%.2f" % (account_balance))
            #input for deposit amount
            withdraw_amount = float(input("How much money do you wish to withdraw? "))
            #printing deposit amount
            print("You withdraw $%.2f" % (withdraw_amount))
            #calculate final account balance 
            account_balance = account_balance - withdraw_amount
            #storing balance after deposit in a file
            withdraw_file = open("savingbalance.txt", "w")
            withdraw_file.write(str(account_balance))
            withdraw_file.close()
            #printing withdraw
            print("Your new balance is $%.2f" % (account_balance))
            #call function Savingdepositorwithdraw
            SavingStatementOfAccount()

#THIS FUNCTION IS TO DO TRANSACTION ON CURRENT ACCOUNT EITHER DEPOSIT OR WITHDRAWAL  
def Currentdepositorwithdraw():
    print('                            >>>>CURRENT TRANSACTION MENU<<<<                            ')
    print()
    print()
    print()
    print("Select option to continue")
    print("[1] Do you wish to deposit")
    print("[2] Do you wish to withdraw")
    choice = input("Enter Choice: ")
    if choice in ('1','2'):   
        if choice == '1':
                #reading file
                balance_file = open("currentbalance.txt", "r")
                #reading account balance
                account_balance = float(balance_file.readline())
                balance_file.close()
                #printing account balance
                print("Your current balance is $%.2f" % (account_balance))
                #input for deposit amount
                deposit_amount = float(input("How much money do you wish to deposit? "))
                #printing deposit amount
                print("You deposited $%.2f" % (deposit_amount))
                #calculate final account balance
                account_balance = account_balance + deposit_amount
                #storing balance after deposit in a file
                deposit_file = open("currentdeposit.txt", "w")
                deposit_file.write(str(account_balance))
                deposit_file.close()
                #printing deposit
                print("Your new balance is $%.2f" % (account_balance))
                #call function Savingdepositorwithdraw
                return Currentdepositorwithdraw()
                
        
        elif choice == '2':
            #reading file
            balance_file = open("currentdeposit.txt", "r")
            #reading account balance
            account_balance = float(balance_file.readline())
            balance_file.close()
            #printing account balance
            print("Your current balance is $%.2f" % (account_balance))
            #input for deposit amount
            withdraw_amount = float(input("How much money do you wish to withdraw? "))
            #printing deposit amount
            print("You withdraw $%.2f" % (withdraw_amount))
            #calculate final account balance
            account_balance = account_balance - withdraw_amount
            #storing balance after deposit in a file
            withdraw_file = open("currentbalance.txt", "w")
            withdraw_file.write(str(account_balance))
            withdraw_file.close()
            #printing deposit
            print("Your new balance is $%.2f" % (account_balance))
            #call function Savingdepositorwithdraw
            CurrentStatementOfAccount()

#THIS FUNCTION IS TO GENERATE STATEMENT OF SAVING ACCOUNT TRANSACTION
def SavingStatementOfAccount():
    print('                            >>>>SAVING ACCOUNT STATEMENT<<<<                            ')
    print()
    print()
    print()
    print("Select option to continue")
    print("[1] Press enter if you want to generate statement of saving account")
    print("[2] Return to main menu")
    print("[3] EXIT")
    choice = input("Enter Choice: ")
    if choice in ('1','2','3'):
        if choice == '1':
            print('statement of saving account')
            fh = open('savingbalance.txt', 'r')
            print(fh.read())
            fh.close()
            print('Statement of saving account generated successfully')
            now = datetime.datetime.now()
            print(now.strftime("%y-%m-%d %H:%M:%S"))

        elif choice == '2':
            print("Return to the main menu")
            MainMenu()

        elif choice == '3':
            sys.exit()

#THIS FUNCTION IS TO GENERATE STATEMENT OF CURRENT ACCOUNT TRANSACTION
def CurrentStatementOfAccount():
    print('                            >>>>CURRENT ACCOUNT STATEMENT<<<<                            ')
    print()
    print()
    print()
    print("Select option to continue")
    print("[1] Press enter if you want to generate statement of current account")
    print("[2] Return to main menu")
    print("[3] EXIT")
    choice = input("Enter Choice: ")
    if choice in ('1','2','3'):
        if choice == '1':
            print('statement of current account')
            fh = open('currentbalance.txt', 'r')
            print(fh.read())
            fh.close()
            print('Statement of current account generated successfully')
            now = datetime.datetime.now()
            print(now.strftime("%y-%m-%d %H:%M:%S"))

        elif choice == '2':
            print("Return to the main menu")
            MainMenu()

        elif choice == '3':
            sys.exit()
            
#THIS FUNCTION IS TO CHOOSE EITHER THE CLIENT WANT TO CREATE SAVING OR CURRENT ACCOUNT
def SavingOrCurrent():
    print('                            >>>>ACCOUNT REGISTERATION MENU<<<<                            ')
    print()
    print()
    print()
    print('[1] Do you wish to create Saving acc? ')
    print('[2] Do you wish to create Current acc? ')
    print('[3] Return to MainMenu')
    print('[4] EXIT')
    choice = input("Enter Choice: ")
    if choice in ('1','2','3','4'):
        if choice == '1':
            print('AutogeneratedUniqueAccNumberSaving')
            fh = open('SAVUNIQUEID.txt', 'r')
            print(fh.read())
            fh.close()
            print('Saving Account Created Successfully')
            Savingdepositorwithdraw()
            return SavingOrCurrent()

        elif choice == '2':
            print('AutogeneratedUniqueAccNumberCurrent')
            fh = open('CURUNIQUEID.txt', 'r')
            print(fh.read())
            fh.close()
            print('Current Account Created Successfully')
            Currentdepositorwithdraw ()
            return SavingOrCurrent()

        elif choice == '3':
            MainMenu()

        elif choice == '4':
            sys.exit()

#THIS FUNCTION IS TO CHANGE THE CLIENT SAVING ACCOUNT PASSWORD
def savchangepass(logdetails):
      allrecord = []
      with open("SAVUNIQUEID.txt","r") as fh:
            for rec in fh:
                  reclist = rec.strip().split(":")
                  allrecord.append(reclist)
      newpassword = input("Please Enter new Password for saving account : ")
      ind = -1
      nor = len(allrecord)
      for cnt in range(0,nor):
            if logdetails[0] == allrecord[cnt][0]:
                  ind = cnt
                  break
      
      allrecord[ind][1] = newpassword
      with open("SAVUNIQUEID.txt","w") as fh:
            nor = len(allrecord)
            for cnt in range(0,nor):
                  rec = ":".join(allrecord[cnt])+"\n"
                  fh.write(rec)
            print("New password created successfully")

#THIS FUNCTION IS TO CHANGE THE CLIENT CURRENT ACCOUNT PASSWORD
def curchangepass(logdetails):
      allrecord = []
      with open("CURUNIQUEID.txt","r") as fh:
            for rec in fh:
                  reclist = rec.strip().split(":")
                  allrecord.append(reclist)
      newpassword = input("Please Enter new Password for current account : ")
      ind = -1
      nor = len(allrecord)
      for cnt in range(0,nor):
            if logdetails[0] == allrecord[cnt][0]:
                  ind = cnt
                  break
      
      allrecord[ind][1] = newpassword
      with open("CURUNIQUEID.txt","w") as fh:
            nor = len(allrecord)
            for cnt in range(0,nor):
                  rec = ":".join(allrecord[cnt])+"\n"
                  fh.write(rec)
            print("New password created successfully")



#THIS IS A DEFAULT SUPERUSER MENU BEFORE ACCESSING OTHER MENU       
print ('                            >>>> SUPERUSER MENU <<<<                          ')
print ('                        >>>> WELCOME TO BADRUL BANK <<<<                      ')
print ()
print ()
print ()
print (' [1] -------------------CHOOSE [1] TO LOG IN AND CONTINUE---------------------')
print (' [2] --------------------------CHOOSE [2] TO EXIT-----------------------------')



choice = input("Enter choice:")


if choice in ('1','2'):

    if choice == '1':
        UserID = input("Enter SUID: ")
        Password = input("Enter SU password: ")
        while UserID!='SUPERUSER1' or Password!='1234567' :
            print ('Access denied')
            UserID = input("Enter SUID: ")
            Password = input("Enter SU password: ")
        MainMenu()

    if choice == '2':
        sys.exit()
        
        
        
                            

    
            
            
            
           



            
                    
                    
                    
                    
                    
                    
                    



                    
                    
        





        
        

        

    
    
    
    
    
    