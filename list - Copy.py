value = ["Ali","Mohammed",21,34,65,75]
print(value)
print(value[3])
print(value[1][len(value[1])-2])
print(value[1][len(value[1])//2])
################################################
value = [1,2]
value.append(20)
value.append(30)
value[1] = 5
print(value)
################################################
grades = []
for i in range(5):
    grade = float(input("Enter a grade: "))
    grades.append(grade)
print(grades)

#for grade in range(len(grades)):
    #print(grade[grades])
   
   
for grade in grades:
   print(grades) 
#################################################
#searching for a number entered by user 
value = [5,9,6,7,3,10]
index = -1
number = float(input("Enter a value that you want to find: "))
for i in range(len(value)):
    if value[i] == number:
        index = i
        break
print(index)
#################################################
# sum of the value
values = [1,2,3,4,5]
total = 0
for i in values:
     total = total + i
print(total)

# find max 
values = [1,2,3,4,5]
maxm = values[0]
for i in values:
    if maxm < i :
        maxx = i
print(maxx)

# print the odd values
values = [1,2,3,4,5,6]
odd=values[0]
for i in values :
    if i%2 == 1:
      print(i)
      
# go througt the list values and replace all negative values to 0
values = [-2,-1,0,1,2]
for i in range(len(values)):
    if values[i] < 0:
        values[i]= 0
print(values) 
###########################
values = [3,2,4,6,1,0]
target = 5
num = values[0]
num2 = values[2]

for i in values :
    if num + i == target :
        print(num , i)
    if num2 + i == target:
        print(num2,i )
        
# or
values = [3,2,4,6,1,0]
target = 5
for i in range(len(values)):
    for j in range(i+1,len(values)):
        if values[i] + values[j]== target:
            print(values[i],values[j])



        
  


