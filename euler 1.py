# PROJECT EULER
# Problem 1 | Kondor 2022

# Problem statement:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


import math

# The initial function for Euler 1. The basic idea is to find the sum of all multiples of 3, sum of all multiples of 5, then subtract the ones that are double counted, i.e. the multiples of 15.


# I began my solution by starting with the classic Gauss summation formula: The sum S from 1 to n is equal to n(n+1)/2. I applied similar logic to the apocryphal Gaussian derivation (1+100, 2+99, ...) to get my general formula for the sum of all multiples of k below n.

# Theorem: 

def euler1(n):
<<<<<<< Updated upstream
    threes = (3 / 2) * math.floor(n / 3) * (math.floor(n / 3) + 1)
    fives = (5 / 2) * math.floor(n / 5) * (math.floor(n / 5) + 1)
    fifteens = (15 / 2) * (math.floor(n / 15)) * (math.floor(n / 15) + 1)
=======
    #Apply formula to 3 to get sum of multiples of three
    threes = (3/2)*math.floor(n/3)*(math.floor(n/3)+1)
    # Apply formula to 5 to get sum of multiples of five
    fives = (5/2)*math.floor(n/5)*(math.floor(n/5)+1)
    # Apply formula to the product of the two to get the sum of all of the double counted numbers
    fifteens = (15/2)*(math.floor(n/15))*(math.floor(n/15)+1)
    # Add multiples of three to multiples of five and adjust for double counting
>>>>>>> Stashed changes
    total = threes + fives - fifteens
    return total


# print(euler1(1000)-1000)

# Currently non-functional. Debugging in progress
# Generalized version, for any natural number n and an array of bases
def GeneralEuler1(n, bases):
    # Set a running total
    total = 0
    # Find sum of multiples of each element of bases
    for i in bases:
        total += (i/2)*(math.floor(n/i))*(math.floor(i)+1)
    # Adjust for double counting
    for i in bases:


<<<<<<< Updated upstream
    for i in range(len(bases)):
        total += (
            (bases[i - 1] / 2)
            * (math.floor(n / bases[i - 1]))
            * (math.floor(bases[i - 1]) + 1)
        )
    for i in range(len(bases)):
        for j in range(len(bases) - 1):
            composite = bases[i - 1] * bases[j - 1]
            total -= (
                (composite / 2)
                * (math.floor(n / composite))
                * (math.floor(n / composite) + 1)
            )
    for i in bases:
        if n % i == 0:
            total -= n
            break
    return total
=======
    
#    for i in range(len(bases)):
 #       total += (bases[i-1]/2)*(math.floor(n/bases[i-1]))*(math.floor(bases[i-1])+1)
  #  for i in range(len(bases)):
   #     for j in range(len(bases)-1):
    #        composite = bases[i-1]*bases[j-1]
     #       total -= (composite/2)*(math.floor(n/composite))*(math.floor(n/composite)+1)
#    for i in bases:
 #       if n % i == 0:
  #          total -= n
   #         break
    #return total
>>>>>>> Stashed changes


print(GeneralEuler1(1000, [3, 5]))
