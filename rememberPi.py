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
#print(num)

num = str(0)
#################
lokiDict = {0:["l"], 1:["t","d"],2:["n"],3:["m"],4:["r"],5:["s","z"], 6:["b","p"],7:["f","v"],8:["k","c","q"],9:["g","j","sh","ch"]}
print ("#"*20)
print ("The loki basic dictionary:")
for number,loki in lokiDict.items():
    print ("Number " + str(number) + " can be replaced by:" )
    for l in loki:
        print (l)
    print()

#####################
# dictionary with number-name pairs
loki99 = {"0":["Lee"], "1":["Tea"],"2":["Neo"],"3":["Ma"],"4":["Rio"],"5":["Sea"],"6":["Bee"],"7":["Fee"],"8":["Key"],"9":["Goo"]}
print ("#"*20)

#####################
# show dictionary
def show_dictionary(dict):
    '''show dictionary nicely.'''
    print ("\nThe lokis from 0 to 9:")
    for number,loki in dict.items():
        print (loki[0]+" stands for " + str(number))
    print()

show_dictionary(loki99)

#########################
# update dictionary with additional loki
def update_dictionary(dict,num,lok):
    '''insert new loki on first place.'''
    dict[num].insert(0,lok)

###################
# transform number into loki code
num = "012345"
print ("#"*20)
print ("Your number is:")
for n in num:
    print (n,end=" ")
print()

print ("\nYour number in Loki code:")
for n in num:
    print(loki99[n][0],end=" ")

print()

##################
# option to replace with other loki name
print()
print ("#"*20)
print("Replace lokis:")
replace = input ("Which number to replace:")
#replace = "0"

currentLoki = loki99[replace][0]
print("Current Loki is %s" %currentLoki)
newLoki = input("Which new Loki for %s?:" %replace)
#newLoki = "Leo"

print("You want to replace %s with %s for %s:"%(currentLoki,newLoki,replace))
print()
##################

# test, if the newLoki can replace the number
from transformLoki import transform_loki

if transform_loki(newLoki) == replace:
    print ("New Loki can replace old one!")
    print ("Loki of %s is %s and can replace %s for %s."%(newLoki,transform_loki(newLoki),currentLoki,replace))
    update_dictionary(loki99,replace,newLoki)
    show_dictionary(loki99)

else:
    print ("Sorry, try again!")
    print ("Loki of %s is %s and cannot replace %s for %s."%(newLoki,transform_loki(newLoki),currentLoki,replace))


########
# update loki99 dictionary
