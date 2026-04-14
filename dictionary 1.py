contacts = {"fred":[11,77],"mary":88,"bob":99}
for key in contacts:
    if type(contacts[key]) is list :
        count=1
        for i in contacts[key]:
            print(key,i,"",count)
            count = count + 1
    else:  
        print(key,contacts[key])
#############################################
keys = [1,1,3,3,2,2,7,7,7,5,6]
result= {}
for i in keys:
    if i not in result:
        result[i] = keys.count(i)
print(result)
###########################################
contacts = {"fred":[11,77],"mary":88,"bob":99}
for item in contacts.items():
    print(item[0],item[1])
    if type(item[1]) is list:
        for i in item[1]:
            print(i)
#############################################
contacts = {"fred":[11,77],"mary":88,"bob":99}
for value in contacts.values():
    print(value)
for key in contacts.keys():
    print(key)

