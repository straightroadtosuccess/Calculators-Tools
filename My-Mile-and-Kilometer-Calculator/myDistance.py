import math

mi = float(input("Miles to convert: "))
km = float(input("Kilometers to convert: "))

mitokm = 1.609344
kmtomi = 0.62137

convertedmi = mi * mitokm
convertedkm = km * kmtomi

print(f"Converted Miles amount: {convertedmi:.2f}")
print(f"Converted Kilometers amount: {convertedkm:.1f}")