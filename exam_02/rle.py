d = {}
def encode(s):
    for i in range(1,len(s)):
        d[s[0]] = 1
        if s[i] == s[i-1]:
            d[s[i]] = d[s[i]]+1
        else:
            d[s[i]] = 1
    return(d)
print(encode('abbaaccddee'))

##def decode(list):
    