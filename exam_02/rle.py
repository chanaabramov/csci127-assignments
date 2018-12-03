##d = {}
##def encode(s):
##    for i in range(1,len(s)):
##        d[s[0]] = 1
##        if s[i] == s[i-1]:
##            d[s[i]] = d[s[i]]+1
##        else:
##            d[s[i]] = 1
##    return(d)
##print(encode('abbaaccddee'))

##def decode(list):

def encode(s):
    for i in s:
        l = []
        l.append(i)
        print(l)
        count= 0
        for count in range(1,len(s)):
            if s[count] == s[count-1]:
                count = count +1
                l.append(count)
                print(l)
                
            
print(encode('abbaaccddee'))