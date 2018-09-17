def capitalize(name):
    space_index = name.find(" ")
    first = name[0:space_index]
    last = name[space_index+1:]
    return first.capitalize() + " " + last.capitalize()
print (capitalize("chana abramov"))

def init(name) :
    space_index = name.find(" ")
    first = name[0:space_index]
    initial = first[0]
    last = name[space_index+1:]
    return initial.capitalize() + ". " + last.capitalize()
print(init("chana abramov"))

def part_pig_latin(name):
    middle_letters = name[1:]
    first = name[0]
    return middle_letters + first + "ay"
print(part_pig_latin("chana"))

def make_out_word(out, word):
  return out[0:2] + word  + out[2:4]
  
print(make_out_word('<<>>', 'mymy'))

def make_tags(tag, word):
  return "<" + tag + ">" + word + "</"+tag+">"

print (make_tags('hi' , 'low'))
