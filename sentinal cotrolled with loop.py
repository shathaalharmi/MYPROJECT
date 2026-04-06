salary = 0.0
total = 0.0
count = 0
while salary >= 0 :
    salary = float(input("Enter a salary or -1 to finish: "))
    if salary >= 0.0 :
        total = total + salary
        count = count + 1
        ave = total / count
        print(ave)
        
        
# let user enter student grades using loop 98 , 90, 70 and 50 and compute the average

grades = 0.0        
total = 0.0      
count = 0
while grades >= 0 :
    grades = int(input("Enter student grades or -1 to finish: "))
    if grades >= 0 :
        total = total + grades
        count = count + 1
ave = total / count
print (ave)

#ask the user to enter grades and print the highest

grades = 0      
maxx = 0
while grades >= 0:
    grades = float(input("Enter student grades or -1 to finish: "))
    if maxx < grades:
        maxx = grades
print(maxx)


