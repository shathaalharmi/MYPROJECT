inputStr = input("Enter number or empty string to stop: ")
negativeCount = 0
while inputStr !='':
    
    value = int(inputStr)
    
    if value < 0: 
        negativeCount = negativeCount + 1
            print("That wasn't a whole number. Try again!")
        inputStr = input("Enter number or empty string to stop: ")
print(negativeCount)


        
        
    
        