import math

inch = float(input("Inches to convert: "))
cm = float(input("Centimeters to convert: "))

intocm = inch * 2.54
cmtoin = cm * 0.3937

print(f"Converted Inches amount in Centimeters: {intocm:.2f}")
print(f"Converted Centimeters amount in Inches: {cmtoin:.1f}")
