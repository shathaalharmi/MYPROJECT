listt = ["Ali","Muna","Ahmed","Reem","Nuha"]
listt [1] = "shatha"
print(listt)

# insert
listt = ["Ali","Muna","Ahmed","Reem","Nuha"]
listt.insert(1,"shatha")
print(listt)

# finding
listt = ["Ali","Muna","Ahmed","Reem","Nuha"]
if "Nuha" in listt:
    print("in listt")
else:
    print("no")
    
# finding index
listt = ["Ali","Muna","Ahmed","Reem","Nuha"]
n = listt.index("Nuha")
print(n)

#pop 
listt = ["Ali","Muna","Ahmed","Reem","Nuha"]
n = listt.pop(1)
print(n)

# remove
listt = ["Ali","Muna","Ahmed","Reem","Nuha"]
listt.remove("Muna")
print(listt)

#concatenation
list1=["shatha","salim"]
list2=["nuha","ahmed"]
friends = list1+list2
print(friends)

#replication
list1=["shatha","salim"]
rep = list1 * 3
print(rep)






