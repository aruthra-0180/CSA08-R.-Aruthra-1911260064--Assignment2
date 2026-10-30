# Q2 - OTP Verification

correct_otp = "1234"
attempts = 0

print("WHILE LOOP")

while attempts < 3:
    otp = input("Enter OTP: ")

    if otp == "":
        print("Blank entry. Try again.")
        continue

    attempts += 1

    if otp == correct_otp:
        print("OTP Verified Successfully")
        break

    print("Wrong OTP")

else:
    print("Account Locked for 30 Minutes")# FOR LOOP

print("\nFOR LOOP")

for i in range(3):

    otp = input("Enter OTP: ")

    while otp == "":
        print("Blank entry. Try again.")
        otp = input("Enter OTP: ")

    if otp == "1234":
        print("OTP Verified Successfully")
        break

    print("Wrong OTP")

else:
    print("Account Locked for 30 Minutes")
   # SECURITY QUESTION - EXTRA ATTEMPTS

print("\nSECURITY QUESTION")

correct_otp = "1234"
answer = input("What is your hometown? ")

if answer.lower() == "chennai":
    max_attempts = 5
    print("Correct answer! 2 extra attempts granted.")
else:
    max_attempts = 3

attempts = 0

while attempts < max_attempts:

    otp = input("Enter OTP: ")

    if otp == "":
        print("Blank entry. Try again.")
        continue

    attempts += 1

    if otp == correct_otp:
        print("OTP Verified Successfully")
        break

    print("Wrong OTP")

else:
    print("Account Locked for 30 Minutes") 
    # RECURSIVE OTP VERIFICATION

print("\nRECURSION")

def verify_otp(attempts):

    correct_otp = "1234"

    if attempts == 3:
        print("Account Locked for 30 Minutes")
        return

    otp = input("Enter OTP: ")

    if otp == "":
        print("Blank entry. Try again.")
        verify_otp(attempts)

    elif otp == correct_otp:
        print("OTP Verified Successfully")

    else:
        print("Wrong OTP")
        verify_otp(attempts + 1)


verify_otp(0)
# PASS STATEMENT

print("\nPASS STATEMENT")

for i in range(3):

    if i == 1:
        pass
    else:
        print("Attempt:", i + 1)