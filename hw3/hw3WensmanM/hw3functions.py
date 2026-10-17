"""
 Author: Malik Wensman
 Email: mdwensma@ncsu.edu
 Class: CSC 251-001 Fall 2026
 Program: hw3functions.py
 Purpose: contains functions for converting heights in feet and inches to centimeters and printing a conversion table
 Bugs: None
 Acknowledgements: None
"""

INCHES_PER_FOOT = 12
INCHES_TO_CM = 2.54

'''
Type can be 'starting' or 'ending' to indicate which height is being entered
'''
def get_values(type: str, start_feet: int, start_inches: int) -> tuple[int, int]: 
    """Prompt the user to enter a height in feet and inches and validate the input.

    Parameters:
    type (str): either 'starting' or 'ending' to indicate which height is being entered
    start_feet (int): the starting feet value used to validate the ending height
    start_inches (int): the starting inches value used to validate the ending height

    Returns:
    (feet, inches) (tuple[int, int]): the validated feet and inches values entered by the user
    """

    feet = int(input(f"Enter the {type} height in feet and inches. First enter the number of feet as an integer between 0 and 20: "))
    inches = int(input("Now enter the number of inches as an integer between 0 and 11: "))

    while feet < 0 or feet > 20 or inches < 0 or inches > 11:
        print("Invalid input. Please enter a value between 0 and 20 for feet and a value between 0 and 11 for inches.")
        feet = input(f"Enter the {type} height in feet and inches. First enter the number of feet as an integer between 0 and 20: ")
        feet = int(feet)
        inches = input("Now enter the number of inches as an integer between 0 and 11: ")
        inches = int(inches)

    if type == 'ending':
        if feet < start_feet or (feet == start_feet and inches < start_inches):
            print("Invalid input. The ending height must be greater than or equal to the starting height.")
            return get_values(type, start_feet, start_inches)

    return feet, inches

def convert_values(feet: int, inches: int) -> float: 
    """Convert a height given in feet and inches to centimeters.

    Parameters:
    feet (int): number of feet (non-negative)
    inches (int): number of inches (0-11)

    Returns:
    centimeters (float): equivalent height in centimeters
    """

    total_inches = feet * INCHES_PER_FOOT + inches
    centimeters = total_inches * INCHES_TO_CM
    return centimeters


def print_table(feet: int, inches: int, centimeters: float) -> None:
    """Print a single formatted table row showing feet, inches, and centimeters.

    Parameters:
    feet (int): feet value to print
    inches (int): inches value to print
    centimeters (float): centimeter value to print (will be formatted to 2 decimal places)

    Returns:
    None
    """

    print(f"{feet:>10} | {inches:>10} || {centimeters:>10.2f}")