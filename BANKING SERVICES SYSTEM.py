# Super Class : User
# Has a function to show user details
# Enter the customer details into the system
# Perform deposit and withdrawal using account number and password

import datetime
import sys
import json
import getpass # masks password from being echoed
import crypto # cryptography module - security enhancement for password encryption

#THIS IS THE FUNCTION THAT I USE TO DO MAIN MENU THAT SHOWS SUPERUSER,ADMIN, AND CUSTOMER.
# TODO: modify input validation - completed
def MainMenu():
    print ('>>>>>WELCOME TO XXXX BANK<<<<<\n')
    print (' [1] Superuser')
    print (' [2] Admin')
    print (' [3] Customer')
    print (' [4] Exit')
    try:
        choice = int(input("\nEnter your choice: "))

        # Logic correction and input validation by parsing the input 
        while True:
            if choice == 1:
                print ('\n>>>>SUPERUSER LOGIN<<<<\n')
                UserID = input("Enter SUID: ")
                Password = getpass.getpass("Enter SU password: ")

                if ValidateUserCredentials(UserID, Password, 'superuser') is not None:
                    SuperUserAcc()
                else:
                    print('Invalid Username or Password! Please try again.')
                
            elif choice == 2:
                print ('\n>>>>ADMIN LOGIN<<<<\n')
                AdminID = input("Enter AdminID: ")
                Password = getpass.getpass("Enter Admin Password: ")
                
                if ValidateUserCredentials(AdminID, Password, 'admin') is not None:
                    AdminAcc()
                else:
                    print('Invalid Username or Password! Please try again.')

            elif choice == 3:
                print ('\n>>>>CLIENT LOGIN<<<<\n')
                ClientID = input("Enter ClientID: ")
                Password = getpass.getpass("Enter Client Password: ")
                
                if ValidateUserCredentials(ClientID, Password, 'client') is not None:
                    ClientAcc()
                else:
                    print('Invalid Username or Password! Please try again.')

            elif choice == 4:
                sys.exit() 
            
            else:
                print(f"Invalid! Integer value should only between 1-3.\n")
                MainMenu()

    except KeyboardInterrupt:
        print("[System's Forced to Exit]")
        sys.exit()

    except ValueError:
        print('Invalid! Only use non-negative integer values.\n')
        MainMenu()

# VALIDATE CREDENTIALS
# TODO: use method overloading using *args - completed
def ValidateUserCredentials(*args):
    try:
        with open('user.json', 'r') as f:
            data = json.load(f)
        for i in range(len(data['user'])):
            try:
                # Searching Record
                if len(args) == 2:
                    for j in range(len(data['user'][i][args[1]])):
                        if args[0] in data['user'][i][args[1]][j]['id']:
                            record = data['user'][i][args[1]][j]
                            f.close()
                            return record
                
                # Deleting Record
                if len(args) == 3 and args[2] == True:
                    for j in range(len(data['user'][i][args[1]])):
                        if args[0] in data['user'][i][args[1]][j]['id']:
                            del data['user'][i][args[1]][j]
                            
                            with open('user.json', 'w') as file:
                                json.dump(data, file, indent=2)
                            file.close()
                            f.close()
                                
                # Validating Record
                elif len(args) == 3:
                    encrypted_pass = crypto.Encryption(args[1]) # hash the password - to compare
                    for j in range(len(data['user'][i][args[2]])):
                        if args[0] in data['user'][i][args[2]][j]['id'] and encrypted_pass.hash() in data['user'][i][args[2]][j]['password']:
                            return True
            except KeyError:
                continue
        return None
    
    except FileNotFoundError as fe:
        print("Failed to open file.", fe)
        sys.exit()

#THIS FUNCTION IS FOR REGISTER ADMIN ACCOUNT ON THE SYSTEM            
def SuperUserAcc():
    print('\n>>>>SUPERUSER MENU<<<<\n')
    print("[1] REGISTER ADMIN ACCOUNT")
    print("[2] FIND ADMIN RECORD")
    print("[3] DELETE ADMIN RECORD")
    print("[4] EDIT ADMIN RECORD")
    print("[5] LOGOUT")
    print("[6] QUIT")

    try:
        choice = int(input("\nEnter Choice: "))

        # TODO: register AdminID, two-time password confirmation -> user.json - completed
        while True:   
            if choice == 1:
                RegAdminID = input("AdminID: ")
                RegAdminPassword = getpass.getpass("Password: ")
                ConfirmPassword = getpass.getpass("Confirm Password: ")
                AdminName = input("Admin Name: ")

                if RegAdminPassword != ConfirmPassword:
                    print("Password didn't match! Please try again.")
                    SuperUserAcc()

                else:
                    if len(RegAdminPassword) < 5:
                        print("Password is too short, consider adding more characters: ")
                        SuperUserAcc()

                    else:
                        encrypt = crypto.Encryption(RegAdminPassword) # hash the password
                        with open("user.json", "r") as a:
                            ra = json.load(a)

                        newAdmin = {
                            "id": RegAdminID,
                            "password": encrypt.hash(),
                            "name": AdminName
                        }

                        ra['user'][1]['admin'].append(newAdmin)

                        with open("user.json", "w") as user:
                            json.dump(ra, user, indent=2)
                        
                        print('\nAdmin Account Created Successfully!')
                        SuperUserAcc()
            
            # TODO: record searching - completed
            elif choice == 2:
                AdminID = input("AdminID: ")
                AdminName = ValidateUserCredentials(AdminID, 'admin')
                if AdminName is not None:
                    print(f"Name: {AdminName['name']}")
                    SuperUserAcc()
                else:
                    print("No record found.")
                    SuperUserAcc()
            
            # TODO: delete record
            elif choice == 3:
                AdminID = input("AdminID: ")
                if ValidateUserCredentials(AdminID, 'admin') is not None:
                    del_confirmation = input("Record found! Proceed to delete?[Y/N]: ")
                    if del_confirmation.upper() == 'Y':
                        ValidateUserCredentials(AdminID, 'admin', True)
                        print("Deleted successfully")
                    elif del_confirmation.upper() == 'N':
                        print("Deletion cancelled")
                    else:
                        print("Invalid character! Please try again.")
                    SuperUserAcc()
            
            # TODO: record manipulation
            elif choice == 4:
                AdminID = input("AdminID: ")
                Record = ValidateUserCredentials(AdminID, 'admin')
                if Record is not None:
                    print(f"\nRecord Found!\nID: {Record['id']}\nName: {Record['name']}")
                    SuperUserAcc()
                else:
                    print("No record found.")
                    SuperUserAcc()

            elif choice == 5:
                MainMenu()

            elif choice == 6: 
                sys.exit()

    except KeyboardInterrupt:
        print("[System's Forced to Exit]")
        sys.exit()

    except ValueError:
        print('Invalid! Only use non-negative integer values.\n')
        SuperUserAcc()

#THIS LINE IS A FUNCTION FOR REGISTER CLIENT INFORMATION INTO THE SYSTEM
def AdminAcc():
    print('\n>>>>ADMIN MENU<<<<\n')
    print("[1] REGISTER CLIENT ACCOUNT")
    print("[2] CREATE PERSONAL SAVING OR WEALTH ACCS")
    print("[3] USER RECORD VALIDATION")
    print("[4] LOGOUT")
    print("[5] QUIT")
    
    try:
        choice = int(input("Enter Choice: "))
        
        while True:
            # TODO: register ClientID, two-time password confirmation -> user.json - completed   
            if choice == 1:
                RegClientID = input("ClientID: ")
                RegClientPassword = getpass.getpass("Password: ")
                ConfirmPassword = getpass.getpass("Confirm Password: ")
                ClientName = input("Client Name: ")

                if RegClientPassword != ConfirmPassword:
                    print("Password didn't match! Please try again.")
                    AdminAcc()

                else:
                    if len(RegClientPassword) < 5:
                        print("Password is too short, consider adding more characters: ")
                        AdminAcc()

                    else:
                        encrypt = crypto.Encryption(RegClientPassword) # hash the password
                        with open("user.json", "r") as a:
                            ra = json.load(a)

                        newClient = {
                            "id": RegClientID,
                            "password": encrypt.hash(),
                            "name": ClientName,
                            "accounts": [
                              {
                                "type": None,
                                "number": None
                              },
                              {
                                "type": None,
                                "number": None
                              }
                            ]
                        }

                        ra['user'][2]['client'].append(newClient)

                        with open("user.json", "w") as user:
                            json.dump(ra, user, indent=2)
                        
                        print('\nClient Account Created Successfully!')
                        AdminAcc()

            elif choice == 2:
                SavingOrCurrent()
                return AdminAcc()
            
            elif choice == 3:
                savchangepass('logdetails')
                return MainMenu()

            elif choice == 4:
                curchangepass('logdetails')
                return MainMenu()
            
            elif choice == 5:
                fh = open('ClientDatabase.txt','r')
                print(fh.read())
                return AdminAcc()
            
            elif choice == 6:
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
            
            elif choice == 7:
                MainMenu()
            
            elif choice == 8:
                sys.exit()

    except KeyboardInterrupt:
        print("[System's Forced to Exit]")
        sys.exit()

    except ValueError:
        print('Invalid! Only use non-negative integer values.\n')
        AdminAcc()
        
def ClientAcc():
    print('\n>>>>CLIENT MENU<<<<\n')
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

#THIS FUNCTION IS TO DO TRANSACTION ON SAVING ACCOUNT EITHER DEPOSIT OR WITHDRAWAL        
def Savingdepositorwithdraw():
    print('>>>>SAVING TRANSACTION MENU<<<<')
    print("\n\n")
    print("Select option to continue")
    print("[1] Do you wish to deposit")
    print("[2] Do you wish to withdraw")
    choice = int(input("Enter Choice: "))
    if choice in ('1','2'):   
        if choice == 1:
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
                
        
        elif choice == 2:
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
    choice = int(input("Enter Choice: "))
    if choice in ('1','2'):   
        if choice == 1:
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
                
        
        elif choice == 2:
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
    print("\n")
    print("Select option to continue")
    print("[1] Press enter if you want to generate statement of saving account")
    print("[2] Return to main menu")
    print("[3] EXIT")
    choice = int(input("Enter Choice: "))
    if choice in ('1','2','3'):
        if choice == 1:
            print('statement of saving account')
            fh = open('savingbalance.txt', 'r')
            print(fh.read())
            fh.close()
            print('Statement of saving account generated successfully')
            now = datetime.datetime.now()
            print(now.strftime("%y-%m-%d %H:%M:%S"))

        elif choice == 2:
            print("Return to the main menu")
            MainMenu()

        elif choice == 3:
            sys.exit()

#THIS FUNCTION IS TO GENERATE STATEMENT OF CURRENT ACCOUNT TRANSACTION
def CurrentStatementOfAccount():
    print('>>>>CURRENT ACCOUNT STATEMENT<<<<')
    print("\n")
    print("Select option to continue")
    print("[1] Press enter if you want to generate statement of current account")
    print("[2] Return to main menu")
    print("[3] EXIT")
    choice = int(input("Enter Choice: "))
    if choice in ('1','2','3'):
        if choice == 1:
            print('statement of current account')
            fh = open('currentbalance.txt', 'r')
            print(fh.read())
            fh.close()
            print('Statement of current account generated successfully')
            now = datetime.datetime.now()
            print(now.strftime("%y-%m-%d %H:%M:%S"))

        elif choice == 2:
            print("Return to the main menu")
            MainMenu()

        elif choice == 3:
            sys.exit()
            
#THIS FUNCTION IS TO CHOOSE EITHER THE CLIENT WANT TO CREATE SAVING OR CURRENT ACCOUNT
def SavingOrCurrent():
    print('>>>>BANK ACCOUNT REGISTRATION MENU<<<<')
    print("\n")
    print('[1] Do you wish to create Saving acc? ')
    print('[2] Do you wish to create Current acc? ')
    print('[3] Return to MainMenu')
    print('[4] EXIT')
    choice = int(input("Enter Choice: "))
    if choice in ('1','2','3','4'):
        if choice == 1:
            print('AutogeneratedUniqueAccNumberSaving')
            fh = open('SAVUNIQUEID.txt', 'r')
            print(fh.read())
            fh.close()
            print('Saving Account Created Successfully')
            Savingdepositorwithdraw()
            return SavingOrCurrent()

        elif choice == 2:
            print('AutogeneratedUniqueAccNumberCurrent')
            fh = open('CURUNIQUEID.txt', 'r')
            print(fh.read())
            fh.close()
            print('Current Account Created Successfully')
            Currentdepositorwithdraw ()
            return SavingOrCurrent()

        elif choice == 3:
            MainMenu()

        elif choice == 4:
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