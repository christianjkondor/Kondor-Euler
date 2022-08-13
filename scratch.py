import math

n = 1000
bases = [3, 5]
total = 0
for i in bases:
        total += (
            (i / 2)
            * (math.floor(n / i))
            * (math.floor(n / i) + 1)
        )

