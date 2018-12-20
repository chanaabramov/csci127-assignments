def countPlurals(line):
    s = line.split()
    pluralCount = 0
    for word in s:
        if word[-1] == 's':
            pluralCount += 1 
    return pluralCount

def notPossesive(line):
    pluralCount = 0
    s = line.split()
    for word in s:
        if word[-1] == 's' and word[-2] != "'":
            pluralCount += 1
    return pluralCount


print(notPossesive("couches in houses with doors and windows"))
print(notPossesive("tests test's houses house's"))
print(countPlurals("couches in houses with doors and windows"))
print(countPlurals("theses wills alls bes considereds plurals becauses theys alls ends withs thes letters s"))
