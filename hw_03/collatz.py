# number
#if number is even you willdivide by 2
#if odd you will do 3n+1 until n=1
#in the loop print out the sequence. return and print out the number of steps
#Chloe Gottlieb and Chana Abramov
def collatz(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = (n / 2)
            steps = steps + 1
        else:
            n = (3 * n + 1)
            steps = steps + 1
    stepsFinal = "it took " + str(steps) + " steps"
    stepsFinalFinal = print(stepsFinal)
    return n
    return stepsFinalFinal
print(collatz(565656))
