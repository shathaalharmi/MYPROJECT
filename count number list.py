values = [1,1,1,3,3,3]
checked = []
for i in values:
    rep = 0
    if i not in checked:
        for j in values :
            if i == j:
               rep = rep + 1
        checked.append(i)
        if rep > 1 :
            print(i, "is repeated", rep, "times")