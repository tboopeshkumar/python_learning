# Get the loan details
money_owed = float(input("how much money do you owe ? \n"))
apr = float(input("what is the annual percentage rate?\n"))
payment = float(input("what will your montly payment be?\n"))
months = int(input("how many months do you want to see results for?\n"))

# Divide apr by 100 to make it percent, then divide by 12 to make montly
monthly_rate = apr/100/12

for i in range(months):
    # Add in interest
    interest_paid = money_owed * monthly_rate
    monthly_rate = monthly_rate + interest_paid

    if money_owed - payment < 0:
        print("The last payment is", money_owed);
        print("You paid off the loan in", i+1, "months")
        break
    
    # Make payment 

    money_owed = money_owed - payment

    # Print the results after this month

    print("Paid", payment, "of which", interest_paid, "was interest.", end=' ')
    print("Now I owe", money_owed)



