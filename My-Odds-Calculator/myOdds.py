# Odds Calculation
import math

# Given equation 1 in 30,000 odds:
# ln((29,999/30,000)n) = ln(0.05)
# Solve for n

odd = int(input('The odds are 1 in what: '))
fodd = odd - 1

n = math.log(0.05) / math.log(fodd/odd)
print("n ≈", n)
