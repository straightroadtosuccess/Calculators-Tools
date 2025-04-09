import statistics

amount = int(input("How many numbers? "))

if amount == 2:
    x, y = map(int, input("What are x y? ").split())
    print(statistics.mean([x, y]))
elif amount == 3:
    x, y, z = map(int, input("What are x y z? ").split())
    print(statistics.mean([x, y, z]))
else:
    print("Only 2 or 3 numbers are supported")




