# write a function that enters whether the entered number is prime or not
def isPrime(num):
    if num <= 1:
        return
    i = 2
    while i < num :
        if num%i==0:
            return False
        i+=1
    return True
print(isPrime(3))





      
        