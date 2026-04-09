###########using global scope
balance = 1000
def withdraw(amount):
    global balance
    if balance >= amount :
        balance = balance - amount
withdraw(350)
print("balance=",balance)

##########using lambda

a = 'GeeksforGeeks'
upper = lambda x : x.upper()
print(upper(a))

area= lambda x,y : x*y
print(area(3,4))
###########

check = lambda x : "positive" if x > 0 else "negative" if x < 0 else "zero"
print(check(5))
print(check(-3))
print(check(0))