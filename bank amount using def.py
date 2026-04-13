balance = 1000
def login(username, password):
    return username == "shatha" and password == 1234


def deposit():
    global balance
    balance = balance + amount


def withdraw():
    global balance
    if amount <= balance:
      balance = balance - amount
    else:
        print("Not enough amount.")
        return balance


username = input("Enter username: ")
password = int(input("Enter password: "))
while True :
    if username == "shatha"and password == 1234 :
      print("access granted , select one option")
      print("1.check balance")
      print("2.deposit money")
      print("3.withdraw money")
      choice = input("Enter option (1, 2, 3 or q): ")
      
      while True:
          choice = input("Choose option 1, 2, 3, or q to quit: ")
          if choice == "1":
                 print("Your current amount is:", balance)

          elif choice == "2":
                 amount = float(input("Enter amount to deposit: "))
                 balance = deposit()
                 print("successfully deposited, you current amount is", balance)

          elif choice == "3":
                 amount = float(input("Enter amount to withdraw: "))
                 balance = withdraw()
                 print("successfully withdraw, you current amount is:", balance)

          else:
                 print("no enough amount")

else:
    print("Access denied")
    
    
