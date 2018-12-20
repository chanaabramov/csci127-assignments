import random


        
        
def canMakeWord(letters,word):
    yes = 0
    for i in word:
        if i in letters:
            yes +=1
    if yes ==  len(word):
        return True
    else:
        return False
print(canMakeWord("dnsrtuscti" , "rustic"))
print(canMakeWord("lkdmskjelkwfeqwjs" , "chana"))
    