balance = 1000 
username_correct = "shatha"
password_correct = 1234

username = input("Enter username: ")
password = int(input("Enter password: "))

if username == "shatha" and password == 1234:
    print("Access granted!")
    
   
    active = True
    while active:
        print("\nSelect one option:")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")

        selectOption = input("Enter option (1, 2, 3, or 4): ")

        if selectOption == "1":
            print("Your current amount is", balance)

        elif selectOption == "2":
            newAmount = float(input("Enter amount to deposit: "))
            balance = balance + newAmount  
            print("Successfully deposited. Your current amount is", balance)

        elif selectOption == "3":
            newAmount = float(input("Enter amount to withdraw: "))
            if newAmount <= balance:
                balance = balance - newAmount  
                print("Successfully withdrawn. Your current amount is", balance)
            else:
                print("Not enough amount!")

        elif selectOption == "4":
            print("Goodbye!")
            active = False 
        
        else:
            print("Invalid option, try again.")
else:
    print("Access denied.")

       
