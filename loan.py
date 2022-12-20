#get loan details
money_owned = float(input("Enter the amount of money you owe, in dollars: "))
apr = float(input("Enter the annual percentage rate:"))
payment = float(input("Enter the monthly payment you can make:"))
months = int(input("Enter the number of months you want to see results for:"))

#divide by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = apr/100/12
for i in range(months):
    interest_paid = money_owned * monthly_rate
    money_owned = money_owned + interest_paid

    if money_owned - payment < 0:
        print("The last payment is", money_owned)
        print("You paid off the loan in", i + 1, "months")
        break
    else:
        money_owned = money_owned - payment
        print("Paid", payment, "of which", interest_paid, "was interest", end=" ")
        print("Now I owe", money_owned)

