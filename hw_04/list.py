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
value = random.randrange(0,7)
print (l)
print (value)


def locate(l, value):
    ind =  0
    if value not in(l):
        return -1
    for i in l:
        if i == value :
            return i , ind
        else:
            i= i+1
            ind = ind+1

def count(l,value):
    num= 0
    for i in l:
        if i == value:
            num = num+1
        i = i+1
    return num       

def reverse(l):
    index = len(l) - 1
    lnew = []
    while index >= 0:
        lnew.append(l[index])
        index -= 1
    return lnew

def isIncreasing(l):
    x=0
    y=1
    inc = True
    while len(l) > y:
        if l[y] >= l[x]:
            x += 1
            y += 1
        else :
            x += 1
            y += 1
            inc = False
    return inc

def palindrome(l):
    begin = 0
    end = len(l) -1
    palind = True
    if l[begin] == l[end]:
        begin += 1
        end += 1
    else:
        palind = False
    return palind

print (locate(l, value))
print (count(l,value))
print(reverse(l))
print (isIncreasing(l))
print (palindrome(l))