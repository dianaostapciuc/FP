# Solve the problem from the third set here
# (15)

def IsThisAPerfectNumber (x):
    s=0
    for i in range (1, int(x/2)+1):
        if x%i == 0:
            s = s + i
    if s == x:
        return True
    return False

def FindTheLargestPerfectNumberSmallerThanN():
    n = int(input("The Number: "))
    n = n-1

    while n > 1:
        if IsThisAPerfectNumber(n) == True:
            print ("The largest perfect number smaller than a given natural number n is: "+str(n))
            break
        n=n-1

    if n == 1:
        print ("There is no number that fits the criteria.")

FindTheLargestPerfectNumberSmallerThanN()