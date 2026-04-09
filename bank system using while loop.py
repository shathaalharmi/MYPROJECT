balance = 1000 

username = input("Enter username: ")
password = int(input("Enter password: "))

if username == "shatha" and password == 1234:
    print("access granted, select one option")
    
    
    while True:
        print("\n1. check balance")
        print("2. deposit money")
        print("3. withdraw money")
        
        selectOption = input("Enter option: 1, 2, or 3: ")

        if selectOption == "1":
            print("your current amount is", balance)
            
        elif selectOption == "2":
            newBalance = float(input("Enter amount to deposit: "))
            balance = balance + newBalance
            print("successfully deposited, your current amount is", balance)
            
        elif selectOption == "3":
            newBalance = float(input("Enter amount to withdraw: "))
            if newBalance <= balance:
                balance = balance - newBalance
                print("successfully withdraw, your current amount is", balance)
            else:
                print("no enough amount")
                
        
        else:
            print("Invalid option, try again.")

else:
    print("access denied")
