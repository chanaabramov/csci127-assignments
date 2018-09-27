import math 
def roots(x):
    steps = 0 
    old_guess = 2
    root =  math.sqrt(x)
    while old_guess != root:
        new_guess =  ((old_guess + (x/old_guess))/2)
        if new_guess != root :
            old_guess = new_guess
            new_guess =  ((old_guess + (x/old_guess))/2)
            print(old_guess)
            steps = steps +1 
        else:
            return "this took " + str(float(steps))+ " guesses"
print (roots(20))
    
    
    