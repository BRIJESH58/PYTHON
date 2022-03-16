try:
    AMOUNT = 300
    if AMOUNT < 2999:
        raise ValueError("PLEASE ADD MONEY IN YOUR ACCOUNT")
    else:
        print("YOU ARE ELIGIBLE TO PURCHASE DSA SELF PACED COURSE")
except ValueError as E:
    print(E)