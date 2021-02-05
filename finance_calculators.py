'''This Python program offers users a choice between 2 financial calculators.
One is an Investment Calculator, which calculates their total investment with
either simple or compund interest, and the other is a Bond Repayment Calculator.
'''

import math

invest_calc = False
bond_calc = False


# Ask user to input their choice of calculator - investment or bond.
print('''\nChoose either 'investment' or 'bond' from the menu below to proceed:\n\ninvestment\t- to calculate the amount of interest you'll earn on investment
bond\t\t- to calculate the amount you'll have to pay on a home loan''')
select_calc = input("\nType in your selection (investment/bond): ")


# The user input should not be case sensitive.
if select_calc == "investment" or select_calc == "Investment" or select_calc == "INVESTMENT":
    invest_calc = True
elif select_calc =="bond" or select_calc == "Bond" or select_calc == "BOND":
    bond_calc = True
else:
    print("You have made a spelling error, please try again.")


# If input is 'investment' ask user to input their investment details.
if invest_calc == True:
    print("\n------Investment Calculator------\n")
    deposit_amt = float(input("Enter your initial deposit amount: R"))
    annual_int_rate = (float(input("Interest rate: "))) / 100
    num_years = int(input("Investment length (years): "))
    interest_type = input("Simple or compound interest (simple/compound): ") 
    # If input is 'simple' calculate the total investment amount and print results.
    if interest_type == "simple":
        # Simple interest formula used is A = P(1 + rt).
        invest_total = deposit_amt * (1 + (annual_int_rate) * num_years)
        print("\nIn {} years you will have: R{:.2f}".format(num_years, invest_total))
    else:
        # If input is 'compound', calculate the total investment amount and print results.
        if interest_type =="compound":
            # Compound interest formula used is A = P(1 + r) ^ t.
            invest_total = deposit_amt * math.pow((1 + (annual_int_rate)),num_years)
            print("\nIn {} years you will have: R{:.2f}".format(num_years, invest_total))
else:
    # If input is 'bond' ask user to input their home loan details.
    if bond_calc == True:
        print("\n------Bond Repayment Calculator------\n")
        prop_value = float(input("Enter your current property value: "))
        annual_int_rate = (float(input("Interest rate: "))) / 100
        monthly_int_rate = annual_int_rate / 12
        num_months = int(input("Repayment term (months): "))
        # Calculate the total using this simple loan formula x = (i.P)/(1 - (1+i)^(-n)) and print results.
        bond_repay = (monthly_int_rate * prop_value) / (1 -(math.pow((1 + monthly_int_rate), - num_months)))
        print("\nYour monthly repayment will be: R{:.2f}".format(bond_repay))
