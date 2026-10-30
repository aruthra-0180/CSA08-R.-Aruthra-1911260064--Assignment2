
# Program 1: if-elif-else

households = [
    ("H1", 80, True, False),
    ("H2", 100, False, False),
    ("H3", 101, True, False),
    ("H4", 150, False, False),
    ("H5", 200, True, False),
    ("H6", 201, True, False),
    ("H7", 250, False, True),
    ("H8", 300, True, False)
]

print("IF-ELIF-ELSE RESULTS")

for name, units, ration, senior in households:

    if units <= 100:
        result = "Full Subsidy"
    elif 101 <= units <= 200 and ration:
        result = "Partial Subsidy"
    elif units > 200 and senior:
        result = "Special Subsidy"
    else:
        result = "No Subsidy"

    print(name, "-", result)


# Program 2: Separate IF

print("\nSEPARATE IF RESULTS")

for name, units, ration, senior in households:

    if units <= 100:
        print(name, "- Full Subsidy")

    if 101 <= units <= 200 and ration:
        print(name, "- Partial Subsidy")

    if units > 200 and senior:
        print(name, "- Special Subsidy")

    if not (units <= 100 or
            (101 <= units <= 200 and ration) or
            (units > 200 and senior)):
        print(name, "- No Subsidy")


# Program 3: Overlapping IF conditions

print("\nOVERLAPPING IF TEST")

units = 100

if units <= 100:
    print("Full Subsidy")

if units >= 100:
    print("Special Offer")
