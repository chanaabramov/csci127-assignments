
import operator

def build_word_counts(words):
    d={}
    for word in words.split():
        d.setdefault(word,0)
        d[word]=d[word]+1
    return d

def clean_data(s):
    result=""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result = result + letter.lower()
        else:
            result = result + " "
    return result

filename="/Users/chanaabramov/fall-2018-127/classcode/dictionaries/moby-small.txt"
f = open(filename, encoding='utf-8')
s = f.read()
words_uncleaned = build_word_counts(s)
cleaned_string = clean_data(s)
print("-------------------")
words = build_word_counts(cleaned_string)
words_sorted = sorted(words.items(), key=operator.itemgetter(1))
ten_common = words_sorted[:10]
print("-------------------")
words_sorted_rv = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
print(words_sorted_rv)
print("-------------------")
ten_least = words_sorted_rv[:10]
print('The 10 most common words are:')
print(ten_least)
print('The 10 least common words are:')
print(ten_common)

dict = {
    'call': [],
    'me' : [],
    'ishmael' : [],
    'some' : [],
    'years' : [],
    'ago' : []
    }

foo = cleaned_string.split()
i = 0
while i < len(foo):    
    if foo[i] in dict:
        dict[foo[i]].append(foo[i+1])
    i += 1
    