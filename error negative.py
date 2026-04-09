negativeCount = 0

while inputStr != '':
    value = int(inputStr)
    if value < 0:
        negativeCount = negativeCount + 1
    inputStr = input("Enter number or empty string to stop: ")
    else:
         print("That wasn't a whole number. Try again!")
print(negativeCount)
