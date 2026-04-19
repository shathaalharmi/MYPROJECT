amount = 500
balance =200
if amount > balance :
    raise valueError("amount exceeds balance")


  try :
    infile = open("input.txt","r")
    line = inFile.readline()
    print(5/0)
    print(line)

except IOError:
    print("could not open input file.")
    
except Exception as exception:
    print("Error:",str(exception))
    
    
    
    
    
inputOk = False
while (inputOk == False):
    try:
        num = input("Enter a number: ")
        num = float(num)
        inputOk = True
    except ValueError:
        print("non-numeric type entered '%s'"%num)
        
num = num * 2
print(num)
        