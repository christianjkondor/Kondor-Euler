import math

def Euclidean(a, b):
    if int(a) != a or int(b) != b:
        nope = "Question wrongly put"
        return nope
    # Trivial case, if a and b are equal.
    if a == b:
        return a
    # Swaps a and b to make sure a > b so we can start the algorithm
    if b > a:
        a = a*b
        b = a/b
        a = a/b
    # Actual Euclidean algorithm
    r1 = a
    #print(r1)
    r2 = b
    #print(r2)
    k = r1%r2
    #print(k)
    while k != 0:
        r1 = r2
        r2 = k
        k = r1%r2
    return "The GCD of " + str(int(a)) + " and " +str(int(b)) + " is " + str(int(r2))


print(Euclidean(15,20))

    

