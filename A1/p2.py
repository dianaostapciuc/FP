# Solve the problem from the second set here
# (8)

def GenerateTheFibonacciSequenceUpUntilN(n, a, b): 
    if n < 1:
        return 1
    c = a + b
    while c <= n:
        a = b
        b = c
        c = a + b
    return c

def FindTheSmallestNumberFromFibo():
    n = int(input("The number: "))
    m = GenerateTheFibonacciSequenceUpUntilN(n, 1, 1)
    print("The smallest number larger than the given n from the Fibonacci sequence is: " + str(m))
    return

FindTheSmallestNumberFromFibo()
