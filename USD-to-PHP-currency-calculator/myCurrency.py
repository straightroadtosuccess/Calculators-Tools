import math

amountu = float(input("USD amount to convert: "))
amountp = float(input("PHP amount to convert: "))

utop = 58.41
ptou = 1.0 / 58.41

convertedu = amountp * ptou
convertedp = amountu * utop

print(f"Converted USD amount: {convertedu:.2f}")
print(f"Converted PHP amount: {convertedp:.1f}")
