def fizz_buzz(number):
    x=1
    while x<=number :
        if x % 3 == 0 and x % 5 == 0 :
            print("fizz" + "buzz")
        elif x % 3 == 0:
            print ("fizz")
        elif x % 5 == 0:
            print("buzz")
        else:
            print(x)
        x = x+1
        
print(fizz_buzz(100))
            
        