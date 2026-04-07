for x in range (1 ,5) :
     print (x, x ** 1)
     print (x, x ** 2)
     print (x, x ** 3)
     print (x, x ** 4)
     
     
     
for x in range (1 ,5) :
    for power in range (1, 5):
        print(x**power, " ",end="")
    print()
    
    
    
for i in range(5) :
    print("*",end= "")
print()


for line in range (100):
    for i in range(5) :
        print("*",end="")
    print()
    
    
# output
#1234
#1234
for line in range (2):
    for i in range(1,5) :
        print(i,end="")
    print()
    
    
for i in range (3):
    for j in range(5) :
        if i % 2 == j % 2 :
           print("*",end="")
        else:
           print(" ", end="")
    print()

    
