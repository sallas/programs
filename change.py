import math
cents = int(round(float(raw_input("")) * 100))
for i, j in [("Quarters:", 25),("Dimes:", 10),("Nickels:",5),("Pennies:",1)]:
    if cents >= j:
        print i, cents/j
        cents %= j
