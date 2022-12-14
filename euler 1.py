# PROJECT EULER
# Problem 1 | Kondor 2022

# Problem statement:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


import math

# The initial function for Euler 1. The basic idea is to find the sum of all multiples of 3, sum of all multiples of 5, then subtract the ones that are double counted, i.e. the multiples of 15.


# DOCUMENTATION IN PROGRESS
def euler1(n):
    threes = (3 / 2) * math.floor(n / 3) * (math.floor(n / 3) + 1)
    fives = (5 / 2) * math.floor(n / 5) * (math.floor(n / 5) + 1)
    fifteens = (15 / 2) * (math.floor(n / 15)) * (math.floor(n / 15) + 1)
    total = threes + fives - fifteens
    return total


# print(euler1(1000)-1000)

# Currently non-functional. Debugging in progress.
def GeneralEuler1(n, bases):
    total = 0

    # For each of the things we're finding multiples of, apply the formula to get the sum of all the multiples.
    for i in bases:
        total += (
            (i / 2)
            * (math.floor(n / i))
            * (math.floor(n / i) + 1)
        )
    # Account for double counting
    for i in range(len(bases)-1):
        for j in range(i, len(bases)):
            if i != j:
                composite = bases[i] * bases[j]
                #print(composite)
                total -= (
                    (composite / 2)
                    * (math.floor(n / composite))
                    * (math.floor(n / composite) + 1)
                )
    # This for loop (tentatively) appears to be working as intended
    # Failsafe to make sure it doesn't include n itself (specific condition for project euler)
    for i in bases:
        if n % i == 0:
            total -= n
            break
    return total


print(GeneralEuler1(1000, [3, 5]))