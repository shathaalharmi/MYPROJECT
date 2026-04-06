balance = 1000
username = input("Enter username: ")
password = int(input("Enter password: "))
if username == "shatha"and password == 1234 :
    print("access granted , select one option")
    print("1.check balance")
    print("2.deposit money")
    print("3.withdraw money")
    
    selectOption =input("Enter option: 1,2,3: ")
    if selectOption == "1" :
     print("your current amount is 1000")
    elif selectOption == "2" :
        newBalance = float(input("Enter amout to deposit: "))
        print("successfully deposited, you current amount is",balance + newBalance)
    elif selectOption == "3" :
        newBalance = float(input("Enter amout to withdraw: "))
    if newBalance <= balance :
        print("successfully withdraw, you current amount is",balance - newBalance)
    else :
        print("no enough amount")
else :
    print("access denaid") 
        

