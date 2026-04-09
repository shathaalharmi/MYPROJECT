name = "Ali"
for letter in name :
    print(letter)
    
    
num = "1792"
total = 0
for char in num :
    total = total + int(num)
    print(char)
    
#find even number
    
num = "1792"
for char in num :
    if int(char) % 2 == 0 :
       print(char)
       
#if I want the name in the same line
name = "Ali"
for letter in name :
    print(letter, end="")
    
for i in range (1,10) :
    print(i)
    
name = "shatha"
for i in range(len(name)):
    print(name[i])