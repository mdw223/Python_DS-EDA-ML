"""
 Author: Malik Wensman
 Email: mdwensma@ncsu.edu
 Class: CSC 251-001 Fall 2026
 Program: Least number of coins
 Purpose: Compute the least number of coins needed to make change for a given amount of money.
 Bugs: None
 Acknowledgements: None
"""

# Constants for coin values
DOLLAR = 1.00
HALF_DOLLAR = 0.50
QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

# counters for each coin type
dollars = 0
half_dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

total_coins = 0
remaining_amount = 0.0

total = float(input("Enter the total amount of money: $\n"))
print(f"Fewest coins for ${total:.2f}") # 2 decimals only
print("==========================")
print(f"{'Coin Type':<15} {'Number':>10}") # align the column headers
print("--------------------------")

dollars = int(total / DOLLAR) # number of dollars by integer division
total_coins += dollars
print(f"{'Dollars':<15} {dollars:>10}")

remaining_amount = total % DOLLAR # remaining amount after dollars
half_dollars = int(remaining_amount / HALF_DOLLAR) # number of half dollars by integer division
total_coins += half_dollars
print(f"{'Half-Dollars':<15} {half_dollars:>10}")

remaining_amount = remaining_amount % HALF_DOLLAR # remaining amount after half dollars
quarters = int(remaining_amount / QUARTER) # number of quarters by integer division
total_coins += quarters
print(f"{'Quarters':<15} {quarters:>10}")

remaining_amount = remaining_amount % QUARTER # remaining amount after quarters
dimes = int(remaining_amount / DIME) # number of dimes by integer division
total_coins += dimes
print(f"{'Dimes':<15} {dimes:>10}")

remaining_amount = remaining_amount % DIME # remaining amount after dimes
nickels = int(remaining_amount / NICKEL) # number of nickels by integer division
total_coins += nickels
print(f"{'Nickels':<15} {nickels:>10}")

remaining_amount = remaining_amount % NICKEL # remaining amount after nickels
pennies = int(round(remaining_amount / PENNY)) # number of pennies by rounding the remaining amount
total_coins += pennies
print(f"{'Pennies':<15} {pennies:>10}")

print("--------------------------")
print(f"{'Total coins':<15} {total_coins:>10}") # total number of coins
