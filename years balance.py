RATE = 5
INITAIL_BALANCE = 10000.0

numYears = int(input("Enter a number for years"))
balance = INITAIL_BALANCE
for year in range (1 , numYears+ 1) :
    interest = balance * RATE/ 100
    balance = balance + interest
    print("%4d %10.2f" % (year , balance))
    