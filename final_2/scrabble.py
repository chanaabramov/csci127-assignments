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
    
def withWild(letters,word):
    count = 0
    for i in letters:
        if i == "?":
            count = count+ 1
    yes = 0
    for i in word:
        if i in letters:
            yes +=1
        if i not in letters and count> 0 :
            yes += 1
            count = count- 1
    if yes ==  len(word):
        return True
    else:
        return False
    
            
        
    
print(canMakeWord("dnsrtuscti" , "rustic"))
print(canMakeWord("lkdmskjelkwfeqwjs" , "chana"))
print(withWild("lkdcak?el?feqwhs" , "chana"))
print(withWild("lkd??????????qwhs" , "chanachana"))
print(withWild("lkdcak?elfeqwhs" , "change"))
    