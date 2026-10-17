"""
 Author: Malik Wensman
 Email: mdwensma@ncsu.edu
 Class: CSC 251-001 Fall 2026
 Program: mortgage calculator
 Purpose: creates an amortization table for a fixed-rate home mortgage and provide a summary of the costs at the end of the table
 Bugs: None
 Acknowledgements: None
"""


# to determine the annual interest rate for the loan depending on the term and down payment desired by the user.
import rate_dict
import table_header
import math
def get_purchase_price():
    while True:
        try:
            purchase_price = float(input("Enter the purchase price of your home: $"))
            print(f"Enter the purchase price of your home: ${purchase_price:.2f}")
            if purchase_price <= 0:
                raise ValueError
            return purchase_price
        except Exception as e:
            print("Must enter a valid number. Please try again.")

def get_term():
    while True:
        try:
            term = int(input("Enter the term of the loan in years: "))
            print(f"Enter the term of the loan in years: {term}")
            if term <= 0:
                raise ValueError
            if term != 10 and term != 15 and term != 20 and term != 30:
                print("Must enter a term of 10, 15, 20, or 30 years.")
                raise ValueError
            return term
        except Exception as e:
            print("Must enter a valid number. Please try again.")

def is_nearest_0_1(value):
    """
    Returns True if the number is rounded to the nearest 0.1.
    E.g., 5.0, 5.1, 5.2 are True. 5.12 is False.
    """
    # Multiply by 10, round to integer, then divide back
    # If the result equals the original, it was already at 0.1 precision
    rounded = round(value * 10) / 10
    return value == rounded

def get_down_payment_percentage():
    while True:
        try:
            down_payment_percentage = float(input("Enter your down payment percentage: "))
            print(f"Enter your down payment percentage: {down_payment_percentage:.1f}")
            if down_payment_percentage < 0 or down_payment_percentage > 100:
                raise ValueError
            
            # Check if the value is precise to the nearest 0.1
            if not is_nearest_0_1(down_payment_percentage):
                print(f"{down_payment_percentage} is not precise enough (not nearest 0.1)")
                continue
            
            return down_payment_percentage
        except Exception as e:
            print("Must enter a valid number. Please try again.")
def get_loan_amount(purchase_price, down_payment_percentage):
    return purchase_price * ((100 - down_payment_percentage) / 100)

def get_LTV_percentage_str(down_payment_percentage, term):
    """Return the LTV bucket string matching the rate_dict keys for the given term."""
    LTV_percentage = 100 - down_payment_percentage
    if term == 10:
        # 10-year products have three tiers
        if LTV_percentage <= 80:
            return "80% or less LTV"
        elif LTV_percentage <= 90:
            return "80.1-90% LTV"
        else:
            return "90.1-100% LTV"
    else:
        # 15-, 20-, 30-year products have two tiers
        if LTV_percentage <= 90:
            return "90% or less LTV"
        else:
            return "90.1-100% LTV"

def get_rate_string(term, down_payment_percentage):
    return f"{term}-Year Fixed, {get_LTV_percentage_str(down_payment_percentage, term)}"

def output_loan_info(rate_string: str):
    '''
    This function is passed a string used as the key for the rates dictionary
    outputs the loan type with the rate information in the format: 
    Loan type: 10-Year Fixed, 90.1-100% LTV at 4.625% APR 
    (You should not return a value from this function)
    '''
    print(f"Loan type: {rate_string} at {rate_dict.rates[rate_string]}% APR")

def get_monthly_interest_payment(loan_amount, annual_rate, term):
    # Loan Payment = Amount x (Interest Rate / 12)
    monthly_rate = annual_rate / 12
    monthly_payment = loan_amount * (monthly_rate / 100)
    return monthly_payment

def get_monthly_payment(principal, annual_rate, years):
    r = annual_rate / 12 / 100
    n = years * 12
    return principal * (r * (1 + r)**n) / ((1 + r)**n - 1)

# Annual PMI rates keyed by (lower_bound_exclusive, upper_bound_inclusive) LTV %
PMI_RATES = {
    (95, 100): 1.040,
    (90, 95):  0.875,
    (85, 90):  0.685,
    (80, 85):  0.475,
    (0,  80):  0.000,
}

def calc_PMI(purchase_price, down_payment_percentage):
    """
    Passed the purchase price and down payment percentage as floats.
    Returns the fixed monthly PMI payment in dollars and cents.
    PMI rate is determined by the initial LTV and applied to the original
    loan amount, spread evenly over 12 months.
    """
    loan_amount = purchase_price * (1 - down_payment_percentage / 100)
    ltv = 100 - down_payment_percentage          # initial LTV %

    annual_pmi_rate = 0.0
    for (low, high), rate in PMI_RATES.items():
        if low < ltv <= high:
            annual_pmi_rate = rate
            break

    return round(loan_amount * annual_pmi_rate / 100 / 12, 2)

def comma_format(value):
    # should have a comma every 3 digits
    # should have 2 decimal places
    return "{:,.2f}".format(value)

def main():
    purchase_price = get_purchase_price()
    term = get_term()
    down_payment_percentage = get_down_payment_percentage()
    rate_string = get_rate_string(term, down_payment_percentage) # same as loan type

    # calculations
    loan_amount = get_loan_amount(purchase_price, down_payment_percentage)
    annual_rate = rate_dict.rates[rate_string]

    # print statements before table
    print()
    print(f"Loan amount: ${comma_format(loan_amount)}")
    output_loan_info(rate_string)
    # round to cents (banker's rounding) so the fixed payment is exact change
    monthly_payment = round(get_monthly_payment(loan_amount, annual_rate, term), 2)

    # PMI is fixed at origination and only dropped once balance < 80% of purchase price
    monthly_pmi = calc_PMI(purchase_price, down_payment_percentage)
    pmi_active = monthly_pmi > 0          # False when down payment >= 20%
    print(f"Monthly Payment = ${comma_format(monthly_payment)}")

    # then the amortization table
    table_header.make_table_header()

    # amortization loop
    outstanding_balance = loan_amount
    total_interest_paid = 0.0
    total_pmi_paid = 0.0

    # payment 0: show initial balance only
    print(f"{0:^8} {'':^18} {'':^20} {comma_format(outstanding_balance):^20}")
    # iterate exactly term*12 months (rounding means balance rarely hits exactly 0)
    for payment_num in range(1, term * 12 + 1):
        # PMI for this payment is based on the balance at the START of the month
        pmi_payment = monthly_pmi if pmi_active else 0.0

        # round interest to the nearest cent (banker's rounding) — this is the key
        # fix that prevents a few-cent drift accumulating between payments
        interest_payment = round(outstanding_balance * annual_rate / 12 / 100, 2)
        principal_payment = monthly_payment - interest_payment
        outstanding_balance = round(outstanding_balance - principal_payment, 2)

        # drop PMI the month AFTER balance falls below 80% of purchase price
        if outstanding_balance < 0.80 * purchase_price:
            pmi_active = False

        print(f"{payment_num:^8} {comma_format(interest_payment):^18} {comma_format(principal_payment):^20} {comma_format(outstanding_balance):^20} {comma_format(pmi_payment):^9}")

        total_interest_paid += interest_payment
        total_pmi_paid += pmi_payment

    print("==============================================================================")
    print()

    # Mortgage summary — right-align dollar amounts to total width 78
    # Use loan_amount (not accumulated principal) so the total is exact
    W = 78
    ti = round(total_interest_paid, 2)
    tp = round(total_pmi_paid, 2)
    total_all = round(ti + loan_amount + tp, 2)
    lbl1 = "Total interest paid: $"
    lbl2 = "Total payment to principal: $"
    lbl3 = "Total PMI paid: $"
    lbl4 = "Total payments: $"
    print("Mortgage Summary")
    print(f"{lbl1}{comma_format(ti):>{W - len(lbl1)}}")
    print(f"{lbl2}{comma_format(loan_amount):>{W - len(lbl2)}}")
    print(f"{lbl3}{comma_format(tp):>{W - len(lbl3)}}")
    print(f"{lbl4}{comma_format(total_all):>{W - len(lbl4)}}")

if __name__ == "__main__":
    main()