# Q2 - OTP Verification

correct_otp = "1234"

print("WHILE LOOP")

attempts = 0

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
    print("Account Locked for 30 Minutes")


print("\nFOR LOOP")

attempts = 0

for i in range(3):
    otp = input("Enter OTP: ")

    while otp == "":
        print("Blank entry. Try again.")
        otp = input("Enter OTP: ")

    attempts += 1

    if otp == correct_otp:
        print("OTP Verified Successfully")
        break

    print("Wrong OTP")

else:
    print("Account Locked for 30 Minutes")