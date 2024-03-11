# Solve the problem from the first set here
# (1)

def PrimeNumber(x):
    if x < 2:
        return False
    count = 0
    for i in range (2, int(x/2)+1):
        if (x%i) == 0:
            count += 1
    if count == 0:
        return True
    return False

def FindTheFirstPrimeNumberLargerThanTheInputNumber():

    n = int(input ("The number: "))
    n += 1

    while (PrimeNumber(n)) == False:
        n += 1

    print ("The first prime number larger than n is: " + str(n))
    return

FindTheFirstPrimeNumberLargerThanTheInputNumber()