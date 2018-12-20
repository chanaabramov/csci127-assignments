d ={}

def addline(dict,line):
    lower_line = ""
    for letter in line:
        lower_line = lower_line + letter.lower()
    clean_line = lower_line.split()
    for word in clean_line:
        if word[0] in d:
            d[word[0]] = d[word[0]] + " " + word
        else:
            d[word[0]] = word
    return d

def spellcheck(d,word):
##    print(d)
    lower_word = ""
    lower_word =  word.lower()
    #print(lower_word)
    print(d[lower_word[0]])
    words = (d[lower_word[0]]).split()
    for vals in words:
        if vals == word:
            return True
    return False
  
    
           
print(addline({},"couches chana cat in houses with doors and windows"))

print("______________________")
print(addline(d,"I a extremely tired but i have shit to do"))
print("______________________")
print(addline(d,"I need to visit my grandmother and do my laundry"))
print("______________________")
print(spellcheck(d, 'cat'))
print(spellcheck(d, 'hulabaloo'))
print(spellcheck(d, 'tired'))