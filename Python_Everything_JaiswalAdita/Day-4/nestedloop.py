income = int(input("Enter your income: "))
credit_score = int(input("Enter your credit score: "))

if income >= 60000:
    if credit_score >= 700:
        print("You are eligible for a loan with a low interest rate.")
    else:
        print("You are eligible for a loan with a higher interest rate.")
else:
    print("You are not eligible for a loan.")