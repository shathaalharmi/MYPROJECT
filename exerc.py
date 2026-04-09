def boxString(contents):
    n = len(contents)
    print("-" *(n+2))
    print("!" + contents + "!")
    print("-" *(n+2))
    
boxString("shthat")

#Write a function table(n) that prints multiplication table of a number.def multiplication(num):
def multiplication(num):
    for i in range(1,13):
     print(i,"*",num,"=", num*i)
print(multiplication(3))

# Write a function factorial(n) that returns factorial of a number.def factorial(n):
def factorial(n):
    total = 1
    for i in range (1,n+1):
        total = total * i
    print(total)
factorial(3)

#Write a function Fibonacci Number
def fab(n):
    a = 0
    b = 1
    print(a)
    for i in range (n):
             temp = a
             a = b
             b = b + temp
             
             
             if a > 7:
                 break
             else :
                 print(a)
fab(3)

#Write a function sum_squares(n) that returns 1^1 + ... + n^n .
def sum_squre(n):
    summ = 0
    for i in range(n+1):
        result = i**i
        summ += result
        
    return summ
print(sum_squre(4))