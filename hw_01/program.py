def capitalize(name):
    space_index = name.find(" ")
    first = name[0:space_index]
    last = name[space_index+1:]
    return capitalize(first[0]) + capitalize(last[0])

print (capitalize("chana abramov"))


def make_out_word(out, word):
  return out[0:2] + word  + out[2:4]
  
print(make_out_word('<<>>', 'mymy'))

def make_tags(tag, word):
  return "<" + tag + ">" + word + "</"+tag+">"

print (make_tags('hi' , 'low'))
