import math

# Printing the two types of calculations
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

print()

# Allowing the user to choose which calculation they want to do
calc_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Making sure the input is not case sensitive
calc_type = (calc_type.casefold())

# Conditional statements
if calc_type == ("investment"):
    # Money which is being deposited
    deposit = float(input("Enter the amount of money which you are depositing: "))
    # Interest rate (Dividing it by 100 to get percentage)
    interest_rate = float(input("Enter the interest rate (DO NOT ADD A PERCENTAGE SIGN): "))
    interest_rate = (interest_rate/100)
    # The number of years they plan on investing
    years = float(input("Enter the number of years which you plan on investing for : "))
    print()
    # Asking if they want simple or compound interest
    print("Would you like simple interest or compound interest?")
    interest = input("Enter either 'simple' or compound': ")
    print()
    # Making sure the input is not case sensitive
    interest = (interest.casefold())
    # Conditional statements
    if interest == ("simple"):
        # Simple interest formula
        amount_after_interest = (deposit*(1 + interest_rate*years))
        # Printing the amount after interest
        print("The total amount once the interest has been applied is:",amount_after_interest)
        # Compound interest statement
    elif interest == ("compound"):
        # Compound interest formula
        amount_after_interest = (deposit*math.pow((1+interest_rate),years))
        # Printing the amount after interest
        print("The total amount once the interest has been applied is:",amount_after_interest)
    else:
        # Invalid interest type error
        print("Invalid interest type")

elif calc_type == ("bond"):
    # The present value of the house
    present_value = float(input("Enter the present value of the house: "))
    # Interest rate (Dividing it by 100 to get percentage)
    interest_rate = float(input("Enter the interest rate (DO NOT ADD A PERCENTAGE SIGN): "))
    interest_rate = (interest_rate/100)
    # Dividing the annual interest rate to get the monthly interest rate
    interest_rate = (interest_rate/12)
    repay_time = float(input("Enter the number of months you plan to take to repay the bond: "))
    print()
    #Bond repayment formula
    repayment = ((interest_rate*present_value)/(1+interest_rate)**(-repay_time))
    print("The amount that you will need to pay on a the home loan each month is:", repayment)
else:
    # Invalid calculation type error
    print("Invalid calculation type")