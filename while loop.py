counter = 1
while counter <= 10 :
    print(counter,"loop",counter)
    counter = counter + 3

print(counter)


counter = 10
while counter >= 0 :
      print(counter)
      counter = counter - 1
      
# print all even number between 0 to 20

counter = 0
if counter % 2 == 0 : 
   while counter <= 20 :
        print(counter)
        counter = counter + 2

# print all primes number from 2 to 100

num = 2

while num < 200 :
    counter = 2
    isPrime = True
    while counter < num :
        if num % counter == 0:
            isPrime = False
        counter = counter + 1
    if isPrime :
        print("this number is prime", num)
        
    num = num + 1
    
    
#sum the numbers from 1 to 10

counter = 1
Sum = 0
while counter <= 10 :
    Sum= Sum + counter
    counter = counter + 1
    print(Sum)

        
    

    


