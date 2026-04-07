inputStr = input("Enter number or empty string to stop: ")
num1 = 0
num2 = 0

while inputStr !="":
    num = int(inputStr)
    if num > 0 :
        num1 = num1 + 1
    if num == num2:
        print("The number",num,"is repeated")
        num2 = num
        inputStr = input("Enter number or empty string to stop: ")
        
print("the number is not repeated")