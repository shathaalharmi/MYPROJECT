RATE = 5
balance = 10000
TARGET = 20000
year = 0
while balance <= TARGET :
    year = year + 1
    intrest = balance * RATE/100
    balance = balance + intrest
    print(year, balance)