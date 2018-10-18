
#Eric Dittus & Chana Abramov
import random
ProperNoun=['Irvington','Jerry', 'Elizabeth','Hillside']
noun=['greenbeans', 'cars','markers','cologne']
verb=['died', 'laughed', 'smoked', 'twerked']
adverb=['merrily','terribly','cryptically','bootyliciously'] 
Madlib= "There once was a man named <ProperNoun> and he loved to eat <noun> a lot. He grew old and <verb> until he layed down <adverb> and <verb> "

def MADLIB(Madlib):
    list_madlib = Madlib.split(' ')
    i=0
    space=" "
    while i< len(list_madlib)-1:
        if "<" in list_madlib[i]:
            if "ProperNoun" in list_madlib[i]:
                index = random.randint(0, len(ProperNoun)-1)
                list_madlib[i]=ProperNoun[index]
            if "noun" in list_madlib[i]:
                index = random.randint(0, len(noun)-1)
                list_madlib[i]=noun[index]
            if ("verb" in list_madlib[i]) and ("ad" not in list_madlib[i]):
                index = random.randint(0, len(verb)-1)
                list_madlib[i]=verb[index]
            if "adverb" in list_madlib[i]:
                index = random.randint(0,len(adverb)-1)
                list_madlib[i]=adverb[index]
 
        i+=1
    return space.join(list_madlib)

print(MADLIB(Madlib))
