# OTP Verification using Recursion

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


print("\nRECURSION")
verify_otp(0)
# Demonstration of Pass Statement

for i in range(3):
    if i == 1:
        pass
    else:
        print("Attempt:", i + 1)