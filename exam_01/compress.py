vowels = "aeiou"

def compress_word(w):
    rest = w[1:]
    first = w[0]
    new_word =  ""
    new_word = new_word + first
    for i in rest:
        if i not in  vowels:
            new_word = new_word + i
    return new_word
            
print (compress_word("apple"))
print (compress_word("audacious"))
print (compress_word("special"))
print (compress_word("suspicious"))

def sentence(line):
    return (compress_word(line))


print (sentence("This test is a bit hard"))
print (sentence("For some odd reason, the first letter of my parameters in both of the last functions come up twice in the return, and I can't figure out why,"))
    


    

