import random

def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the list
      max_value : the max random value to put in the list
    """
    l = [] # start with an empty list

    # make a loop that counts up to size
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l


l =  build_random_list(10,20)
print (l)
def filterodd(l):
    newl = []
    for i in range(len(l)):
        if l[i] % 2 != 0:
            newl.append(l[i])
    return newl
print(filterodd(l))

def mapsquare(l):   #mapping is taking one set of functions and relating it to another set of functions
    squared = []
    for i in l:
        squared.append(i ** 2)
    return squared
print(mapsquare(l))
            
        
            