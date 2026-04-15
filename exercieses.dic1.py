dic = {
        "sunday":30,
        "monday":29,
        "tuesday":31,
        "wednesdays":33,
        "thursday":35,
        "friday":28,
        "saturday":25
    
    }

totalTemp = 0
for key in dic:
    totalTemp =  totalTemp + dic[key]
aveTemp = totalTemp / len(dic)

print(sum(dic.values()))
print(max(dic.values()))
print(min(dic.values()))

maxm=0
for value in dic.values():
    if value > maxm:
        maxm = value

for item in dic.items():
    print(item[0],item[1])
    if item[1] == maxm:
         print("this max temp was on day: " ,item[1])

#OR------------------------------------------
for day, temp in dic.items():
    if temp == maxm:
        print(day)