def makeacronym(s):
    d = {}
    for word in s.split():
        d[word] = word[0].lower()
    acro = (d.values())
    return (acro)
        
        
print(makeacronym("Laugh Out Loud"))
print(makeacronym("Read the Fine Manual"))