# Extra Attempts with Security Question

correct_otp = "1234"
correct_answer = "chennai"

answer = input("What is your hometown? ")

if answer.lower() == correct_answer:
    max_attempts = 5
    print("Correct answer! You get 2 extra attempts.")
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