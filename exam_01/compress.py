vowels = "aeiou"
i = 1

def compress_word(w):
    new_word =  ""
    new_word = new_word + w[0]
    for i in range((len(w))):
        if w[i] not in  vowels:
            new_word = new_word + w[i]
            i = i + 1
    return new_word
            
print (compress_word("apple"))
print (compress_word("audacious"))
print (compress_word("special"))
print (compress_word("suspicious"))
 
#i cant get the first letter to work properly

def sentence(line):
    return (compress_word(line))


print (sentence("This test is a bit hard"))
print (sentence("For some odd reason, the first letter of my parameters in both of the last functions come up twice in the return, and I can't figure out why,"))
    


    

