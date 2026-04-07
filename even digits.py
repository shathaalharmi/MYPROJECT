# let the user enter a number and print even digits in number using loop and indexs

count = 0  
number = input("Enter a number: ")
while count < len(number) :
      if int(number[count])%2 ==0 :
        print(int(number[count])) 
      count = count + 1