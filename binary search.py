listt = [1,4,7,8,3]
listt.sort()
x = int(input("Enter a number: "))
start =0
end = len(listt)-1
while start<end:
    mid=(start+end)//2
    if listt[mid]==x:
        print(mid)
        break
    elif x>listt[mid]:
        start = mid + 1
    elif x<listt[mid]:
        end = mid - 1
else:
    print("Not found!")