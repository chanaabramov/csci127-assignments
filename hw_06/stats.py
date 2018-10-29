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
    frequency = 0
    for num in list:
        if num == val:
            frequency = frequency +1
    return (frequency)

def mode(list):
    greatest_val = list[0]
    greatest = freq(list,list[0])
    for val in list:
        if freq(list, val) >= greatest:
            greatest = freq(list, val)
            greatest_val = val
         
    return greatest , greatest_val



print(mode(list))
print(freq(list, 54))
print (max(list))
        
