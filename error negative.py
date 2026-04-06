inputStr = input("Enter number or empty string to stop: ")
negativeCount = 0

while inputStr != '':
    try:
        value = int(inputStr)
        if value < 0:
            negativeCount = negativeCount + 1
    except ValueError:
        print("That wasn't a whole number. Try again!")
    
    inputStr = input("Enter number or empty string to stop: ")

print(negativeCount)
