import math

def euler1(n):
    threes = (3/2)*math.floor(n/3)*(math.floor(n/3)+1)
    fives = (5/2)*math.floor(n/5)*(math.floor(n/5)+1)
    fifteens = (15/2)*(math.floor(n/15))*(math.floor(n/15)+1)
    total = threes + fives - fifteens
    return total

#print(euler1(1000)-1000)

def GeneralEuler1(n, bases):
    total = 0

    
    for i in range(len(bases)):
        total += (bases[i-1]/2)*(math.floor(n/bases[i-1]))*(math.floor(bases[i-1])+1)
    for i in range(len(bases)):
        for j in range(len(bases)-1):
            composite = bases[i-1]*bases[j-1]
            total -= (composite/2)*(math.floor(n/composite))*(math.floor(n/composite)+1)
    for i in bases:
        if n % i == 0:
            total -= n
            break
    return total


print(GeneralEuler1(1000, [3,5]))




