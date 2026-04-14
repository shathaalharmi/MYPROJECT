records = [
    ("Ali", "Math", 85),
    ("Sara", "Math", 90),
    ("Ali", "Science", 78),
    ("Sara", "Science", 88),
    ("Ali", "English", 92),
    ("Sara", "English", 85)
]

output = {}
for name,subject,grade in records:
    if name not in output:
        output[name]={}
    output[name][subject]=grade
print(output)
########################################
records = [
    ("Ali", "Math", 85),
    ("Sara", "Math", 90),
    ("Ali", "Science", 78),
    ("Sara", "Science", 88),
    ("Ali", "English", 92),
    ("Sara", "English", 85)
]

bigDic = {}
for record in range(len(records)):
    name = records[record][0]
    sub = records[record][1]
    grade = records[record][2]
    
    if name not in bigDic:
        bigDic[name] = {}
    bigDic[name][sub]=grade
print(bigDic)

records=  [{'Math': 85, 'Science': 78, 'English': 92}, {'Math': 90, 'Science': 88, 'English': 85}]

averages = {}

for subject in records[0]:
    total = 0
    
    for record in records:
        total += record[subject]
    
    avg = total / len(records)
    averages[subject] = avg

print(averages)

          


        
    
        
   