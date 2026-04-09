def func1(*args):
    for arg in args :
        print(10,3.14)
#########################################
def calculation(a, b):
    off = a + b , a - b
    return off
res = calculation(40, 10)
print(res)
##########################################
def show_employee(name , salary = 3000):
    print("name:", name,  "salary", salary)
show_employee("shatha")
show_employee("lama",2500)
###########################################
def outer(a,b):
    def inner():
         return a+b 
    return inner() + 5
print(outer(10,10))
###########################################
def factorial(n):
    if n==0 or n==1 :
        return 1
    return n * factorial(n-1)
print(factorial(5))
###########################################
def total(n):
   if n == 0 :
       return 0
   return n + total(n-1)  
print(total(10))
###########################################
#use recursive
def digit(n):
    if n == 0:
        return n
    return 1+digit(n//10)
print(digit(175))


