# get input from user
weight = float(input("What is the weight: "))
unit = (input("Is it in lb or kg? ")).lower()

# convert the unit to correct type
if unit == "lb":
    lbtokg = (weight / 2.2)
    print(f"{lbtokg:.2f}")
elif unit == "kg":
    kgtolb = (weight * 2.2)
    print(f"{kgtolb:.2f}")


