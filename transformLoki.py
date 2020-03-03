#################
# function that transforms a number into a loki word

def transform_loki(loki):
    """ transforms a word into a number."""
    #print ("Original Loki: %s"% loki)
    
    ##############
    # make lowercase
    lokiNumber=loki.lower()
    #print (lokiNumber)

    ##############
    # delete double consonants 
    deleteDouble = ["b","c","d","f","g","k","l","m","n","p","r","s","t","v","z"]
    for double in deleteDouble:
        lokiNumber = lokiNumber.replace(double+double,double)

    #print (lokiNumber)    

    ##############
    # replace consonant combos
    consoCombos = {"sch":"g","sh":"g","ch":"g"}
    for combo,conso in consoCombos.items():
        lokiNumber = lokiNumber.replace(combo,conso)
    #print (lokiNumber)    
    ##############
    # delete vowels and useless consonants
    deleteVowels = ["a","e","h","i","o","u","w","x","y"]
    for vowel in deleteVowels:
        lokiNumber = lokiNumber.replace(vowel,"")
    #print (lokiNumber)    
    ##############
    # replace remaining consonants with numbers
    consoNumbers = {"b":"6","c":"8","d":"1","f":"7","g":"9","j":"9","k":"8","l":"0","m":"3","n":"2","p":"6","q":"8","r":"4","s":"5","t":"1","v":"7","z":"5"}
    for conso,number in consoNumbers.items():
        lokiNumber = lokiNumber.replace(conso,number)
    #print (lokiNumber)  
    
    #print (("%s becomes %s") %(loki,lokiNumber))
    #print()

    return lokiNumber  

################
# test data for function
"""
lokiList = ["soccer","latte","tissue","chair","shop","school"]
for l in lokiList:
    transform_loki(l)

lokiList1 = ["Lee", "Tea", "Neo","Ma","Rio","Sea","Bee","Fee","Key","Goo"]
for l in lokiList1:
    transform_loki(l)

"""
""" 
for l in lokiList:
    lokiNumber = transform_loki(l)
    print (("%s becomes %s") %(l,lokiNumber))
    print()
"""



#################
# function to transform a Loki into a number
# needed, if a new Loki follows the rules

#lokiDict = {0:["l"], 1:["t","d"],2:["n"],3:["m"],4:["r"]}
#print (lokiDict)

