def lady(string):
    n  = len(string) 
    spaces =  (list(string))
    print(spaces)
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in range(0, n-1):
        if spaces[i] == spaces[ i+1] or spaces[i] == spaces[ i-1]:
            happy = True
        else:
            space = spaces.index("_")
            temp = spaces[space]
            spaces[space] = spaces[i]
            spaces[i] = temp
            print(spaces)
            for i in range(0, len(spaces)-1):
                if spaces[i] == spaces[ i+1] or spaces[i] == spaces[ i-1]:
                    happy = True
                else:
                    happy = False
        
    under = []
    for i in range(0,n-1):
        if spaces[i] == "_":
            under.append(spaces.index(i))

            
print(lady("X_Y__Z"))
print(lady("RBY_BYR"))
        

        