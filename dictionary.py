favoriteColor = {"romeo": "green","shatha":"pink"}
print(favoriteColor)

friendsNum= {'Ali':9999,'Muna':8888}
aliNum=friendsNum['Ali']
print(aliNum)

friendsNum= {'Ali':[9999,6666,7777],'Muna':8888}
if "Ali" in friendsNum:
    aliNum=friendsNum['Ali'][1]
    print(aliNum)
print(friendsNum.get("Muna",411))
print(friendsNum.get("reem",411))