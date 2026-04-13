medals = [
    [0,3,0],
    [0,0,1],
    [0,0,1]
             ]

for i in range(len(medals)):
    for j in range(len(medals[i])):
         print(medals[i][j]," ",end="")
    print()
    
    
matrix = [
    [2,4,5,1],
    [3,2,9,6],
    [1,0,2,10]
    ]
totals =[]
for row in range(len(matrix)):
    total = 0
    for j in range(len(matrix[row])):
        total = total + matrix[row][j]
    totals.append(total)
maxx = max(totals)
print(totals.index(20))
        
        
    
        