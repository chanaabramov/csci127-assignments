
#Eric Dittus & Chana Abramov
import random
Madlib = "What happened to my <animal> <name> ? One day he <verb> <noun> , and the next day he was speaking <language> <adverb> . Maybe it was the <noun> that he ate. He ate a lot of <adjective> things. But we will never know, because he <verb> to <country> the next day."
def MADLIB(Madlib):
    ProperNoun=['Irvington','Jerry', 'Elizabeth','Hillside']
    noun=['greenbeans', 'cars','markers','cologne']
    verb=['died', 'laughed', 'smoked', 'twerked' , ' choked' , 'cried' , 'gasped', 'heaved' , ]
    adjective = [ 'beautiful' , 'ugly' , 'terrible' , 'plain' ,'ostentatious' , 'critical' ,'heavy' , 'thin', 'thick']
    adverb=['merrily','terribly','cryptically','bootyliciously', 'happily',]
    animal = [' aardvark', 'kangaroo', ' centipede', 'lion', 'zebra', ' fat cat', ' giraffe']
    language = ['hebrew', 'farsi' , 'mandarin' , 'russian' , 'english' ]
    country = ['Argentina', 'Russia', 'Israel', 'China' , 'Japan' , 'Abu Dhabi', 'Uzbekistan' , 'Cuba' , 'Barbados' ,'Bangladesh']
    names = ['Barry','Dillon' , 'Charlie','Samantha' , 'Jonathan','Ahmed', 'Abraham','Esriel' 'Moses', 'Esther', 'G-d','Naomi' , 'Leah', 'Rachel'] 

 
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
                index = random.choice(adverb) #random.choice is easier than doing random.randint....
                list_madlib[i]=index
            if "animal" in list_madlib[i]:
                index = random.randint(0,len(adverb)-1)
                list_madlib[i]=animal[index]
            if "country" in list_madlib[i]:
                index = random.randint(0,len(adverb)-1)
                list_madlib[i]=country[index]
            if "language" in list_madlib[i]:
                index = random.randint(0,len(adverb)-1)
                list_madlib[i]=language[index]
            if "adjective" in list_madlib[i]:
                index = random.randint(0,len(adverb)-1)
                list_madlib[i]=adjective[index]
            if "name" in list_madlib[i]:
                index = random.randint(0,len(adverb)-1)
                list_madlib[i]=names[index]
 
        i+=1
    return space.join(list_madlib)

print(MADLIB(Madlib))
