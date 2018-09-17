vowels = "a" , "e" , "i" ,  "o" , "u", "y"

def pig_latin(name):
    first_letter = name[:1]
    rest_of_word = name[1:]
    if first_letter in(vowels):
        return first_letter + rest_of_word + "ay"
    else:
        return rest_of_word + first_letter + "ay"
print(pig_latin("table"))
print(pig_latin("abercrombie"))
      
