############################
# rememberPi
# to remember a given 1# loki system
# to remember a given 2# loki system
# to define one's own loki system
# to use this system to remember any number
# to use this system to remember Pi

print()
import random

#########
# input number, cut spaces and transform into list
# num = input("Number please:")
num = "12 34"
num = num.replace(" ","")
num = [int(x) for x in str(num)] 


#########
# generate random number for test reasons
num =[]
while len(num) < 6:
    r=random.randint(0,9)
    if r not in num: 
        num.append(r)
print(num)

#####################
# dictionary with number-name pairs
lokiDict = {0:"Lee", 1:"Tea",2:"Neo",3:"Ma",4:"Rio",5:"Sea",6:"Bee",7:"Fee",8:"Key",9:"Goo"}
#print(lokiDict)
for number,loki in lokiDict.items():
    print (loki + " stands for " + str(number))

###################
# transform number into loki code
print ("\nYour number in Loki code:")
lokiNum = [lokiDict[x] for x in num]
for x in lokiNum:
    print (x, end = " ")
print()

##################
# option to replace with other loki name

#replace = int(input ("Which number to replace:"))
replace = 1

currentLoki = lokiDict[replace]
print("Current Loki is %s" %currentLoki)
#newLoki = input("Which new Loki for %s?:" %replace)
newLoki = "tit"

print("You want to replace %s with %s for %s"%(currentLoki,newLoki,replace))

##################

# test, if the newLoki can replace the number
from transformLoki import transform_loki
print (transform_loki(newLoki))

if transform_loki(newLoki) == replace:
    print: ("yes")
else:
    print:("no")
