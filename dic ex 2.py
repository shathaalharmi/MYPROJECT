dic = {
    
    "sun":[30,29],
    "mon":[29,31],
    "tues":[31,30],
    "wed":[33,32],
    "thur":[35,33],
    "fri":[28,30],
    "sat":[25,23]
    }

for day,temps in dic.items():
    print(day,temps[0])
    
# to calculate average temp of week 2
    
    
totalTemp = 0

for day,temps in dic.items():
    totalTemp =  totalTemp + temps[1]
aveTemp = totalTemp / len(dic)
    
print(aveTemp)

# adding a new week (3)
for day in dic.keys():
    user = int(input("enter a number and -1 to finish:  "))
    dic[day].append(user)
print(dic)



dic["sun"].append(31)
dic["mon"].append(35)
dic["tues"].append(30)
dic["wed"].append(34)
dic["thur"].append(36)
dic["fri"].append(27)
dic["sat"].append(24)
print(dic)



week3Temp=[33,22,34,26,25,31,32]
dic["sun"].append(week3Temp[0])
dic["mon"].append(week3Temp[1])
dic["tues"].append(week3Temp[2])
dic["wed"].append(week3Temp[3])
dic["thur"].append(week3Temp[4])
dic["fri"].append(week3Temp[5])
dic["sat"].append(week3Temp[6])

print(dic)
index=0
for day in dic.keys():
        dic[day].append(week3Temp[index])
        index+=1
print(dic)
