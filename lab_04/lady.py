
testcases = ["RB_BY_YY", "XY_XY"]

for test in testcases:
    b = test
    

newb= list(b)
countlist = [] 
empty_list = []

def sort(b):
    val = "_"
    for item in (newb):
        if item == "_":
            empty_list.append(item)
    while val in newb:
        newb.remove(val)
    newb2 = sorted(newb)
    return newb2

newb2 = sort(b)
print(newb2)

def freq2(l,item):
    count = 0
    for i in range(len(l)):
        if l[i] == item:
            count = count + 1
    return count


def conditions(b):
    if len(empty_list) >= 1:
        for i in range (len(newb2)):
            count = freq2(newb2, newb2[i])
            if count >= 2:
                happy= True
            else:
                happy = False
                break
        return happy
for test in testcases:
    print(test)
    print(conditions(b))









        