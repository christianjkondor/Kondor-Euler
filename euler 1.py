# PROJECT EULER
# Problem 1 | Kondor 2022

# Problem statement:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


import math

# The initial function for Euler 1. The basic idea is to find the sum of all multiples of 3, sum of all multiples of 5, then subtract the ones that are double counted, i.e. the multiples of 15.


# DOCUMENTATION IN PROGRESS
def euler1(n):
    threes = (3/2)*math.floor(n/3)*(math.floor(n/3)+1)
    fives = (5/2)*math.floor(n/5)*(math.floor(n/5)+1)
    fifteens = (15/2)*(math.floor(n/15))*(math.floor(n/15)+1)
    total = threes + fives - fifteens
    return total

#print(euler1(1000)-1000)

# Currently non-functional. Debugging in progress.
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




