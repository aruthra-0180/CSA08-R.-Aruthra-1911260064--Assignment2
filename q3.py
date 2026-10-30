# Q3 - Vehicle Registration Number Validator

def normalise(text):
    text = text.strip()
    text = text.replace(" ", "")
    text = text.replace("-", "")
    text = text.upper()
    return text


print("VEHICLE NUMBER VALIDATOR")

number = input("Enter vehicle number: ")

reg = normalise(number)

print("Normalised Number:", reg)
def is_valid(reg):

    if len(reg) == 9:
        return (reg[0:2].isalpha() and
                reg[2:4].isdigit() and
                reg[4:5].isalpha() and
                reg[5:9].isdigit())

    elif len(reg) == 10:
        return (reg[0:2].isalpha() and
                reg[2:4].isdigit() and
                reg[4:6].isalpha() and
                reg[6:10].isdigit())

    else:
        return False


if is_valid(reg):
    print("Valid Registration Number")
else:
    print("Invalid Registration Number")