x=1
def fizz_buzz(x):
    while x<=100 :
        if x % 3 == 0 and x % 5 == 0 :
            print("fizz" + "buzz")
        elif x % 3 == 0:
            print ("fizz")
        elif x % 5 == 0:
            print("buzz")
        else:
            print(x)
        x = x+1
        
print(fizz_buzz(x))
            
        