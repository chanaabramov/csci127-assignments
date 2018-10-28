import random

def build_random_list(size,max_value):
    l = [] 
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        i = i + 1
    return l
list  = build_random_list(100,100)
print(list)
def max(list):
    greatest = list[0]
    for i in range(1, len(list)):
        if list[i] >= greatest:
            greatest = list[i]
    spot = list.index(greatest)

    return greatest , spot
def freq(list,val):
    frequency = []
    for num in list:
        if num == val:
            frequency.append(num)
    return len(frequency)

def mode(list):
    greatest = freq(list,list[0])
    for val in list:
        if freq(list, val) >= greatest:
            greatest = freq(list, val)
         
    return greatest , list [val]




print(mode(list))
print(freq(list, 54))
print (max(list))
        
