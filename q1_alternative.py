
# Alternative Method: Match Case

def check_subsidy(units, ration, senior):

    match (units <= 100,
           101 <= units <= 200 and ration,
           units > 200 and senior):

        case (True, _, _):
            return "Full Subsidy"

        case (_, True, _):
            return "Partial Subsidy"

        case (_, _, True):
            return "Special Subsidy"

        case _:
            return "No Subsidy"


print("MATCH-CASE RESULTS")

print(check_subsidy(80, True, False))
print(check_subsidy(150, True, False))
print(check_subsidy(250, False, True))
print(check_subsidy(300, False, False))
