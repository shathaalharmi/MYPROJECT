infile = open("C:/Users/Shatha Alharmi/OneDrive/Desktop/data.txt","r")
line1 = infile.readline()
print(line1)

line2 = infile.readline()
print(line2)

infile.close()
##########################################################
infile = open("C:/Users/Shatha Alharmi/OneDrive/Desktop/data.txt","r")
line = infile.read()
noLines = 1
while line != "":
    print(line)
    noLines += 1
    line = infile.read()
infile.close()
############################################################

infile = open("C:/Users/Shatha Alharmi/OneDrive/Desktop/data.txt","r")
line = infile.readlines()
print(line)
infile.close()
    
##############################################################
infile = open("C:/Users/Shatha Alharmi/OneDrive/Desktop/data.txt","r")
lines = infile.readlines()
print(lines)

for line in range(len(lines)):
    lines[line]=int(lines[line].strip())
    
print(sum(lines)/len(lines))
print(max(lines))
print(min(lines))

infile.close()
##############################################################
infile = open("C:/Users/Shatha Alharmi/OneDrive/Desktop/data.txt","r")
print(infile.read())
infile.close()
##############################################################
infile = open("C:/Users/Shatha Alharmi/OneDrive/Desktop/data.txt","r")
lines = infile.read().split("\n")
print(lines)
infile.close()

##############################################################
infile = open("C:/Users/Shatha Alharmi/OneDrive/Desktop/data.txt","w")
infile.write("hello nafadh\nfrom shatha")
infile.close()

###############################################################





