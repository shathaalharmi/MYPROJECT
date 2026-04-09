sidelength = 10
def cubeVolume(sidelength):
    if sidelength >= 0 :
        return sidelength ** 3
    else :
        return 0

print(cubeVolume(sidelength))

#pyramidoVolume 
def pVolume(baseArea,height):
    volume = (1/3)*(baseArea * height)
    return volume
print(pVolume(3,3))


    