import random

def build_random_list(size,max_value):
    l = [] 
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        i = i + 1
    return l
l  = build_random_list(100,100)
def fast_mode(l,max_value):
    tallies = []
    for i in range(max_value):
        tallies.append(0)
    for item in l:
        tallies[item] = tallies[item] + 1
    return tallies
print(fast_mode(l,100))