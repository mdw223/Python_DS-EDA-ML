"""
 Author: Malik Wensman
 Email: mdwensma@ncsu.edu
 Class: CSC 251-001 Fall 2026
 Program: mortgage calculator
 Purpose: creates an amortization table for a fixed-rate home mortgage and provide a summary of the costs at the end of the table
 Bugs: None
 Acknowledgements: None
"""

import math
import rate_dict
import table_header

# ── Constants ──────────────────────────────────────────────────────────────────
VALID_TERMS         = (10, 15, 20, 30)  # allowed loan term lengths in years
MONTHS_PER_YEAR     = 12                # payment periods per year
PERCENTAGE_SCALE    = 100               # divisor to convert a percentage to a decimal
DOWN_PAYMENT_PREC   = 0.1              # required precision for down payment entry (nearest 0.1%)
PMI_DROP_THRESHOLD  = 0.80             # principal/purchase-price ratio below which PMI is dropped
SUMMARY_WIDTH       = 78               # total character width used to right-align summary amounts

# 10-year loan LTV tier cut-offs (10-yr has 3 tiers; all others have 2)
LTV_10YR_LOW_CUTOFF = 80               # ≤ 80% LTV  → "80% or less LTV"
LTV_10YR_MID_CUTOFF = 90               # 80–90% LTV → "80.1-90% LTV"
LTV_OTHER_CUTOFF    = 90               # 15/20/30-yr: ≤ 90% → "90% or less LTV"

# Annual PMI rates keyed by (lower_bound_exclusive, upper_bound_inclusive) LTV %
PMI_RATES = {
    (95, 100): 1.040,
    (90, 95):  0.875,
    (85, 90):  0.685,
    (80, 85):  0.475,
    (0,  80):  0.000,
}


# ── Input helpers ──────────────────────────────────────────────────────────────

def get_purchase_price():
    """Prompts the user to enter the purchase price of their home and validates the input.
    Parameters:
        None
    Returns:
        purchase_price (float): the validated purchase price of the home in dollars
    """
    while True:
        try:
            purchase_price = float(input("Enter the purchase price of your home: $"))
        except ValueError:
            # Non-numeric input (e.g. "one million") – cannot even echo it
            print("Invalid price. Try again.")
            continue

        # Echo the parsed value so the user can confirm what was read
        print(f"Enter the purchase price of your home: ${purchase_price:.2f}")

        if purchase_price <= 0:
            print(f"Price must be greater than $0.00. Try again.")
            continue

        return purchase_price


def get_term():
    """Prompts the user to enter the loan term in years and validates that it is in VALID_TERMS.
    Parameters:
        None
    Returns:
        term (int): the validated loan term in years (10, 15, 20, or 30)
    """
    while True:
        try:
            term = int(input("Enter the term of the loan in years: "))
        except ValueError:
            # Non-integer input (e.g. "ten") – cannot echo it
            print(f"Term must be a whole number. Try again.")
            continue

        # Echo the parsed value before range check
        print(f"Enter the term of the loan in years: {term}")

        if term not in VALID_TERMS:
            # Use continue instead of raise so only ONE error message is printed
            print(f"Term must be one of {list(VALID_TERMS)}. Try again.")
            continue

        return term


def is_nearest_0_1(value):
    """Checks whether a float value is expressed to the nearest 0.1 (one decimal place).
    Parameters:
        value (float): the number to check for 0.1 precision
    Returns:
        result (bool): True if value is at 0.1 precision, False otherwise
    """
    # Avoid direct float equality; use math.isclose to handle IEEE 754 rounding
    rounded = round(value / DOWN_PAYMENT_PREC) * DOWN_PAYMENT_PREC
    return math.isclose(value, rounded, abs_tol=1e-9)


def get_down_payment_percentage():
    """Prompts the user to enter their down payment percentage and validates that it is
    between 0 and 100 and expressed to the nearest 0.1.
    Parameters:
        None
    Returns:
        down_payment_percentage (float): the validated down payment percentage (0.0 – 100.0)
    """
    while True:
        try:
            pct = float(input("Enter your down payment percentage: "))
        except ValueError:
            # Non-numeric input – cannot echo it
            print("Down payment must be a number. Try again.")
            continue

        # Echo the parsed value before range / precision checks
        print(f"Enter your down payment percentage: {pct:.1f}")

        if pct < 0 or pct > PERCENTAGE_SCALE:
            print(f"Down payment must be between 0 and {PERCENTAGE_SCALE}%. Try again.")
            continue

        if not is_nearest_0_1(pct):
            print(f"Down payment must be expressed to the nearest {DOWN_PAYMENT_PREC}%. Try again.")
            continue

        return pct


# ── Calculation helpers ────────────────────────────────────────────────────────

def get_loan_amount(purchase_price, down_payment_percentage):
    """Calculates the loan amount as the purchase price minus the down payment.
    Parameters:
        purchase_price (float): the full purchase price of the home in dollars
        down_payment_percentage (float): the down payment expressed as a percentage (0 – 100)
    Returns:
        loan_amount (float): the principal loan amount in dollars
    """
    return purchase_price * ((PERCENTAGE_SCALE - down_payment_percentage) / PERCENTAGE_SCALE)


def get_LTV_percentage_str(down_payment_percentage, term):
    """Returns the LTV tier string that matches the corresponding key in rate_dict for the given term.
    Parameters:
        down_payment_percentage (float): the down payment expressed as a percentage (0 – 100)
        term (int): the loan term in years (10, 15, 20, or 30)
    Returns:
        ltv_str (str): the LTV tier label used as part of the rate_dict key
    """
    ltv_percentage = PERCENTAGE_SCALE - down_payment_percentage
    if term == 10:
        # 10-year products have three tiers
        if ltv_percentage <= LTV_10YR_LOW_CUTOFF:
            return "80% or less LTV"
        elif ltv_percentage <= LTV_10YR_MID_CUTOFF:
            return "80.1-90% LTV"
        else:
            return "90.1-100% LTV"
    else:
        # 15-, 20-, 30-year products have two tiers
        if ltv_percentage <= LTV_OTHER_CUTOFF:
            return "90% or less LTV"
        else:
            return "90.1-100% LTV"


def get_rate_string(term, down_payment_percentage):
    """Builds the full rate_dict key string from the loan term and down payment percentage.
    Parameters:
        term (int): the loan term in years (10, 15, 20, or 30)
        down_payment_percentage (float): the down payment expressed as a percentage (0 – 100)
    Returns:
        rate_string (str): the key string used to look up the APR in rate_dict
                           (e.g. "10-Year Fixed, 90.1-100% LTV")
    """
    return f"{term}-Year Fixed, {get_LTV_percentage_str(down_payment_percentage, term)}"


def output_loan_info(rate_string):
    """Prints the loan type and its annual percentage rate (APR) to the console.
    Parameters:
        rate_string (str): the key used to look up the loan in rate_dict
                           (e.g. "10-Year Fixed, 90.1-100% LTV")
    Returns:
        None
    """
    try:
        print(f"Loan type: {rate_string} at {rate_dict.rates[rate_string]}% APR")
    except KeyError:
        print(f"Error: loan type '{rate_string}' was not found in the rate dictionary.")


def get_monthly_interest_payment(loan_amount, annual_rate, term):
    """Calculates the simple monthly interest payment on the outstanding loan balance.
    Parameters:
        loan_amount (float): the current outstanding principal balance in dollars
        annual_rate (float): the annual interest rate as a percentage (e.g. 4.625)
        term (int): the loan term in years (unused here; kept for signature consistency)
    Returns:
        monthly_payment (float): the interest-only portion of one monthly payment in dollars
    """
    monthly_rate = annual_rate / MONTHS_PER_YEAR
    return loan_amount * (monthly_rate / PERCENTAGE_SCALE)


def get_monthly_payment(principal, annual_rate, years):
    """Calculates the fixed monthly mortgage payment using the standard amortization formula.
    Parameters:
        principal (float): the initial loan amount in dollars
        annual_rate (float): the annual interest rate as a percentage (e.g. 4.625)
        years (int): the loan term in years
    Returns:
        monthly_payment (float): the fixed monthly payment amount in dollars
    """
    r = annual_rate / MONTHS_PER_YEAR / PERCENTAGE_SCALE
    n = years * MONTHS_PER_YEAR
    return principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)


def calc_PMI(purchase_price, down_payment_percentage):
    """Calculates the fixed monthly PMI payment based on the initial LTV and loan amount.
    The PMI rate is determined at origination and does not change until PMI is dropped.
    Parameters:
        purchase_price (float): the full purchase price of the home in dollars
        down_payment_percentage (float): the down payment expressed as a percentage (0 – 100)
    Returns:
        monthly_pmi (float): the fixed monthly PMI payment in dollars and cents
    """
    loan_amount = purchase_price * (1 - down_payment_percentage / PERCENTAGE_SCALE)
    ltv = PERCENTAGE_SCALE - down_payment_percentage   # initial LTV %

    annual_pmi_rate = 0.0
    for (low, high), rate in PMI_RATES.items():
        if low < ltv <= high:
            annual_pmi_rate = rate
            break

    return round(loan_amount * annual_pmi_rate / PERCENTAGE_SCALE / MONTHS_PER_YEAR, 2)


def comma_format(value):
    """Formats a numeric value as a string with comma separators and exactly two decimal places.
    Parameters:
        value (float): the monetary value to format
    Returns:
        formatted (str): the value formatted as a string (e.g. "1,234.56")
    """
    return "{:,.2f}".format(value)


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    """Drives the mortgage calculator: collects user input, prints loan information,
    outputs the full amortization table, and displays the mortgage cost summary.
    Parameters:
        None
    Returns:
        None
    """
    try:
        # ── Collect and validate user inputs ──────────────────────────────────
        purchase_price        = get_purchase_price()
        term                  = get_term()
        down_payment_pct      = get_down_payment_percentage()
        rate_string           = get_rate_string(term, down_payment_pct)

        # ── Derived values ────────────────────────────────────────────────────
        loan_amount    = get_loan_amount(purchase_price, down_payment_pct)
        annual_rate    = rate_dict.rates[rate_string]          # KeyError caught below
        monthly_payment = round(get_monthly_payment(loan_amount, annual_rate, term), 2)

        monthly_pmi = calc_PMI(purchase_price, down_payment_pct)
        pmi_active  = monthly_pmi > 0   # False when down payment >= 20 %

        # ── Pre-table output ──────────────────────────────────────────────────
        print()
        print(f"Loan amount: ${comma_format(loan_amount)}")
        output_loan_info(rate_string)
        print(f"Monthly Payment = ${comma_format(monthly_payment)}")

        # ── Amortization table ────────────────────────────────────────────────
        table_header.make_table_header()

        outstanding_balance = loan_amount
        total_interest_paid = 0.0
        total_pmi_paid      = 0.0

        # Payment 0: initial balance only (no interest/principal breakdown yet)
        print(f"{0:^8} {'':^18} {'':^20} {comma_format(outstanding_balance):^20}")

        for payment_num in range(1, term * MONTHS_PER_YEAR + 1):
            # PMI is based on the balance at the START of this month
            pmi_payment = monthly_pmi if pmi_active else 0.0

            # Round each month's interest to the nearest cent (banker's rounding)
            interest_payment   = round(
                outstanding_balance * annual_rate / MONTHS_PER_YEAR / PERCENTAGE_SCALE, 2
            )
            principal_payment  = monthly_payment - interest_payment
            outstanding_balance = round(outstanding_balance - principal_payment, 2)

            # Drop PMI the month AFTER balance falls below 80% of purchase price
            if outstanding_balance < PMI_DROP_THRESHOLD * purchase_price:
                pmi_active = False

            print(
                f"{payment_num:^8} "
                f"{comma_format(interest_payment):^18} "
                f"{comma_format(principal_payment):^20} "
                f"{comma_format(outstanding_balance):^20} "
                f"{comma_format(pmi_payment):^9}"
            )

            total_interest_paid += interest_payment
            total_pmi_paid      += pmi_payment

        print("==============================================================================")
        print()

        # ── Mortgage summary ──────────────────────────────────────────────────
        ti        = round(total_interest_paid, 2)
        tp        = round(total_pmi_paid, 2)
        total_all = round(ti + loan_amount + tp, 2)

        lbl1 = "Total interest paid: $"
        lbl2 = "Total payment to principal: $"
        lbl3 = "Total PMI paid: $"
        lbl4 = "Total payments: $"

        print("Mortgage Summary")
        print(f"{lbl1}{comma_format(ti):>{SUMMARY_WIDTH - len(lbl1)}}")
        print(f"{lbl2}{comma_format(loan_amount):>{SUMMARY_WIDTH - len(lbl2)}}")
        print(f"{lbl3}{comma_format(tp):>{SUMMARY_WIDTH - len(lbl3)}}")
        print(f"{lbl4}{comma_format(total_all):>{SUMMARY_WIDTH - len(lbl4)}}")

    except KeyError as e:
        print(f"Error: rate not found for loan type {e}. Please check your inputs.")
    except ZeroDivisionError:
        print("Error: cannot compute payment — annual rate produced a division by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
