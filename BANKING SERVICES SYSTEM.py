# Super Class : User
# Has a function to show user details
# Enter the customer details into the system
# Perform deposit and withdrawal using account number and password

import datetime
import sys
import yaml

#THIS IS THE FUNCTION THAT I USE TO DO MAIN MENU THAT SHOWS SUPERUSER,ADMIN, AND CUSTOMER.
# TODO: modify input validation
def MainMenu():
    print ('>>>>>WELCOME TO XXXX BANK<<<<<\n')
    print (' [1] Super User')
    print (' [2] Admin')
    print (' [3] Customer')
    print (' [4] Exit')
    choice = int(input("\nEnter your choice: "))

    with open('user.json', 'r') as u:
        data = json.load(u)

    # Logic correction and input validation by parsing the input 
    while True:
        if choice == 1:
            print ('\n>>>>SUPERUSER LOGIN<<<<\n')
            UserID = input("Enter SUID: ")
            Password = input("Enter SU password: ")

            if ValidateUserCredentials(data['user'], UserID, Password, 'superuser'):
                SuperUserAcc()
            else:
                print('Invalid Username or Password! Please try again.')
            
        elif choice == 2:
            print ('>>>>ADMIN LOGIN<<<<\n')
            AdminID = input("Enter AdminID:")
            Password = input("Enter Admin Password: ")
            
            if ValidateUserCredentials(data['user'], AdminID, Password, 'admin'):
                AdminAcc()
            else:
                print('Invalid Username or Password! Please try again.')

        elif choice == 3:
            print ('>>>>CLIENT LOGIN<<<<\n')
            print (' [1]SAVING ACCOUNT')
            print (' [2]WEALTH ACCOUNT')
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                AccNumber = input("Enter AccNumber:")
                Password = input("Enter Client Password: ")

                while AccNumber!='0000,0000,0000,0001' or Password!='1234567' :
                    print ('Access denied')
                    AccNumber = input("Enter AccNumber: ")
                    Password = input ("Enter Client password: ")
                Savingdepositorwithdraw() 
                SavingStatementOfAccount() 
            
            elif choice == 2:
                AccNumber = input("Enter AccNumber:")
                Password = input("Enter Client Password: ")
                
                while AccNumber!='0000,0000,0000,0001' or Password!='1234567' :
                    print ('Access denied')
                    AccNumber = input("Enter AccNumber: ")
                    Password = input ("Enter Client password: ")
                Currentdepositorwithdraw()
                CurrentStatementOfAccount()

        elif choice == 4:
            break

        else:
            print ('Invalid! Please try again.\n')

# TODO: use YAML to store data
def ValidateUserCredentials(user_data, input_id, input_password, role):
    for user in user_data:
        if role in user and input_id in user[role] and input_password in user.get('password', []):
            return True
    return False

#THIS FUNCTION IS FOR REGISTER ADMIN ACCOUNT ON THE SYSTEM            
def SuperUserAcc():
    print('>>>>SUPERUSER MENU<<<<')
    print("\n")
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
def AdminAcc():
    print('>>>>CLIENT REGISTRATION MENU<<<<')
    print("\n\n")
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
                AdminAcc()
            
            else:
                if len(Name)<=2:
                    print("name too short, restart:")
                    AdminAcc()

                else:
                    CA = open("ClientDatabase.txt","a")
                    CA.write(clientID+"\n "+Name+"\n "+Age+"\n "+IdentificationCard+"\n "+ContactNumber+"\n "+Address+"\n "+DateOfBirth+"\n")
                    print("Success!")
                    AdminAcc()

        elif choice == '2':
            SavingOrCurrent()
            return AdminAcc()
        
        elif choice == '3':
            savchangepass('logdetails')
            return MainMenu()

        elif choice == '4':
            curchangepass('logdetails')
            return MainMenu()
        
        elif choice == '5':
            fh = open('ClientDatabase.txt','r')
            print(fh.read())
            return AdminAcc()
        
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
    print('>>>>SAVING TRANSACTION MENU<<<<')
    print("\n\n")
    print("Select option to continue")
    print("[1] Do you wish to deposit")
    print("[2] Do you wish to withdraw")
    choice = input("Enter Choice: ")
    if choice in ('1','2'):   
        if choice == '1':
                balance_file = open("savingbalance.txt", "r")
                account_balance = float(balance_file.readline())
                balance_file.close()
                print("Your current balance is $%.2f" % (account_balance))
                deposit_amount = float(input("How much money do you wish to deposit? "))
                print("You deposited $%.2f" % (deposit_amount)) 
                account_balance = account_balance + deposit_amount
                deposit_file = open("savingdeposit.txt", "w")
                deposit_file.write(str(account_balance))
                deposit_file.close()
                print("Your new balance is $%.2f" % (account_balance))
                return Savingdepositorwithdraw()
                
        
        elif choice == '2':
            balance_file = open("savingdeposit.txt", "r")
            account_balance = float(balance_file.readline())
            print("You are not permitted to withdraw")    
            balance_file.close()
            print("Your current balance is $%.2f" % (account_balance))
            withdraw_amount = float(input("How much money do you wish to withdraw? "))
            print("You withdraw $%.2f" % (withdraw_amount))
            account_balance = account_balance - withdraw_amount
            withdraw_file = open("savingbalance.txt", "w")
            withdraw_file.write(str(account_balance))
            withdraw_file.close()
            print("Your new balance is $%.2f" % (account_balance))
            SavingStatementOfAccount()

#THIS FUNCTION IS TO DO TRANSACTION ON CURRENT ACCOUNT EITHER DEPOSIT OR WITHDRAWAL  
def Currentdepositorwithdraw():
    print('>>>>CURRENT TRANSACTION MENU<<<<')
    print("\n\n")
    print("Select option to continue")
    print("[1] Do you wish to deposit")
    print("[2] Do you wish to withdraw")
    choice = input("Enter Choice: ")
    if choice in ('1','2'):   
        if choice == '1':
                balance_file = open("currentbalance.txt", "r")
                account_balance = float(balance_file.readline())
                balance_file.close()
                print("Your current balance is $%.2f" % (account_balance))
                deposit_amount = float(input("How much money do you wish to deposit? "))
                print("You deposited $%.2f" % (deposit_amount))
                account_balance = account_balance + deposit_amount
                deposit_file = open("currentdeposit.txt", "w")
                deposit_file.write(str(account_balance))
                deposit_file.close()
                print("Your new balance is $%.2f" % (account_balance))
                return Currentdepositorwithdraw()
                
        
        elif choice == '2':
            balance_file = open("currentdeposit.txt", "r")
            account_balance = float(balance_file.readline())
            balance_file.close()
            print("Your current balance is $%.2f" % (account_balance))
            withdraw_amount = float(input("How much money do you wish to withdraw? "))
            print("You withdraw $%.2f" % (withdraw_amount))            
            account_balance = account_balance - withdraw_amount           
            withdraw_file = open("currentbalance.txt", "w")
            withdraw_file.write(str(account_balance))
            withdraw_file.close()           
            print("Your new balance is $%.2f" % (account_balance))     
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
    print('>>>>CURRENT ACCOUNT STATEMENT<<<<')
    print("\n\n")
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
    print('>>>>BANK ACCOUNT REGISTRATION MENU<<<<')
    print("\n")
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

if __name__ == "__main__":
    MainMenu()