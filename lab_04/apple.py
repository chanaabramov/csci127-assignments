import random

def build_random_list(size,min_value,max_value):
    l = [] 
    i = 0
    while i < size:
        l.append(random.randrange(min_value,max_value))
        i = i + 1
    return l
list  = build_random_list(10,-10,10)
print(list)

fad = build_random_list(3,-5,5)
print(fad)
fod = build_random_list(3,-5,5)
print(fod)
def countApplesandOranges(s,t,a,b):
    count =  0
    count2 = 0
    for i in range(0,len(fad)):
        if a + fad[i] >= s and a + fad[i] <=t:
            count =  count + 1
    for i in range(0,len(fod)):
        if b + fod[i] >= s and b + fod[i] <=t:
            count2 =  count2 + 1
    print( "The house is from point" ,s, "to point" , t)
    print("The apple tree is at point" , a)
    print("The orange tree is at point" , b)
    print(len(fod),"oranges fell")
    print(len(fad), "apples fell")
    print (count , "apples fell on the house") 
    print (count2 , "oranges fell on the house")
print(countApplesandOranges(3,6,-1,7))

    