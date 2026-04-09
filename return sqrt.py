#write a function that is going to return sqrt if its perfect or not :
from math import sqrt
def sqrNumer(num):
    root = sqrt(num)
    if root.is_integer()== True:
        return root
    else:
        return (" Not perfect sqrt")
print(sqrNumer(6))
    


