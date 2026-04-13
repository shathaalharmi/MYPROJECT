def multiply(lis,factor):
    lis = list(lis)
    for i in range(len(lis)):
        lis[i] = lis[i] * factor
    return lis
listt = [1,2,3]
factor = 2
print(multiply(listt,factor))
print(listt)

#################################

temperatures = [18,21,33,32,44,39,40,39,36,30,22,18]
print(len(temperatures))
fourtheQuarter = temperatures[9:]
print(fourtheQuarter)

#################################

limit = 100
pos = 0
found = False
while pos <len (value) and not found:
    if values [pos] >limit:
        found = True
    else:
        pos = pos+1
if found :
    print("fount at position",pos)
else:
    print("not found")
    
#################################