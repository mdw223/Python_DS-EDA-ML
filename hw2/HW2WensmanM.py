"""
 Author: Malik Wensman
 Email: mdwensma@ncsu.edu
 Class: CSC 251-001 Fall 2026
 Program: Yardage Calculator
 Purpose: Compute the yardage needed for a given amount of money.
 Bugs: None
 Acknowledgements: None
"""

import math
from fractions import Fraction

# CONSTANTS
WIDTH = 21.5 # inches
YARD_INCHES = 36
ROUNDING = 8 # round to the 1/8 of a yard. You always roundup

# user selects length of fabric in yards 
# to get the length of fabric you need to cut, you add the 0.5 in seam allowance on each of the two ends (top and bottom)
# must calculate the finished_length (what is left after sewing)
def prompt_for_length() -> float:
    """Prompts the user for the finished pillowcase length.

    Parameters:
    None

    Returns:
    finished_length_in_inches (float): The user's chosen pillowcase length in inches, validated to be between 0 and 108 inclusive.
    """
    finished_length_in_inches = float(input('Enter the length of the pillowcase in inches (0-108"): '))
    while finished_length_in_inches < 0 or finished_length_in_inches > 108:
        finished_length_in_inches = float(input('Invalid input for length. Re-enter the length in inches(0-108"): '))
    return finished_length_in_inches

def prompt_for_price() -> float:
    """Prompts the user for the fabric price per yard.

    Parameters:
    None

    Returns:
    price_per_yard (float): The price of the fabric in dollars per yard, validated to be non-negative.
    """
    price_per_yard = float(input('Enter the price per yard: $'))
    while price_per_yard < 0:
        price_per_yard = float(input('Invalid input for price. Re-enter the price per yard: $'))
    return price_per_yard

def add_seam_allowance(length_in_inches: float) -> float:
    """Adds the seam allowance to the finished pillowcase length.

    Parameters:
    length_in_inches (float): The finished pillowcase length in inches before seam allowance is added.

    Returns:
    total_length_in_inches (float): The length in inches after adding 1 inch total of seam allowance.
    """
    return length_in_inches + 1 # add 0.5 inch seam allowance to each end (top and bottom)

def convert_to_yards(length_in_inches: float) -> float:
    """Converts a length from inches to yards.

    Parameters:
    length_in_inches (float): The length to convert, measured in inches.

    Returns:
    length_in_yards (float): The same length expressed in yards.
    """
    return length_in_inches / YARD_INCHES

def round_up_to_nearest_eighth_yard(length_in_yards: float) -> float:
    """Rounds a yard length up to the nearest 1/8 yard.

    Parameters:
    length_in_yards (float): The fabric length measured in yards.

    Returns:
    rounded_length_in_yards (float): The value rounded up to the nearest 1/8 yard.
    """
    return math.ceil(length_in_yards * ROUNDING) / ROUNDING

def print_cost(cost: float) -> None:
    """Prints the total cloth cost with two decimal places.

    Parameters:
    cost (float): The total fabric cost in dollars.

    Returns:
    None
    """
    print(f"Fabric cost: ${cost:.2f}")

def format_yards(length_in_yards: float) -> str:
    """Formats a yard amount as a readable string with whole yards and reduced fractions.

    Parameters:
    length_in_yards (float): The number of yards to format.

    Returns:
    formatted_length (str): A human-readable fabric-length string such as '1-1/8 yards' or '1/2 yard'.
    """
    whole_yards, leftover_eighths = get_whole_and_leftover_yards(length_in_yards)

    # if the leftover was rounded up to a whole yard, add it to the whole yards and set leftover to 0
    if leftover_eighths == ROUNDING:
        whole_yards += 1
        leftover_eighths = 0

    if whole_yards == 0 and leftover_eighths == 0:
        return "0 yards"

    if leftover_eighths == 0:
        if whole_yards == 1:
            return "1 yard"
        return f"{whole_yards} yards"

    fraction_obj = Fraction(leftover_eighths, ROUNDING)

    if whole_yards == 0:
        return f"{fraction_obj.numerator}/{fraction_obj.denominator} yard"

    return f"{whole_yards}-{fraction_obj.numerator}/{fraction_obj.denominator} yards"

def print_fabric(length_in_yards: float) -> None:
    """Prints the formatted minimum fabric statement.

    Parameters:
    length_in_yards (float): The total required yardage to display.

    Returns:
    None
    """
    print(f"Minimum fabric needed: {format_yards(length_in_yards)}")

def get_whole_and_leftover_yards(length_in_yards: float) -> tuple[int, int]:
    """Separates a yard length into its whole-yard and leftover eighth-yard portions.

    Parameters:
    length_in_yards (float): The total length in yards to split apart.

    Returns:
    whole_yards (int): The integer number of whole yards.
    leftover_eighths (int): The remaining fraction converted to eighths of a yard.
    """
    whole_yards = int(length_in_yards) 

    leftover_yards = length_in_yards - whole_yards 
    leftover_eighths = round(leftover_yards * ROUNDING) # get the leftover yards and convert to eighths
    return whole_yards, leftover_eighths

def test_get_whole_and_leftover_yards() -> None:
    """Tests the helper that splits yard lengths into whole and leftover eighths.

    Parameters:
    None

    Returns:
    None
    """
    print("Testing get_whole_and_leftover_yards(0.0)")
    expected = (0, 0)
    actual = get_whole_and_leftover_yards(0.0)
    if expected == actual:
        print("Test passed")
    else:
        print("Test failed")
        print("Expected: ", expected)
        print("Actual: ", actual)

    print("Testing get_whole_and_leftover_yards(1.5)")
    expected = (1, 4)
    actual = get_whole_and_leftover_yards(1.5)
    if expected == actual:
        print("Test passed")
    else:
        print("Test failed")
        print("Expected: ", expected)
        print("Actual: ", actual)

    print("Testing get_whole_and_leftover_yards(2.125)")
    expected = (2, 1)
    actual = get_whole_and_leftover_yards(2.125)
    if expected == actual:
        print("Test passed")
    else:
        print("Test failed")
        print("Expected: ", expected)
        print("Actual: ", actual)


def test_round_up_to_nearest_eighth_yard() -> None:
    """Tests the yard-rounding helper that rounds up to the nearest 1/8 yard.

    Parameters:
    None

    Returns:
    None
    """
    print("Testing round_up_to_nearest_eighth_yard(0.75)")
    expected = 1.0
    actual = round_up_to_nearest_eighth_yard(0.75)
    if expected == actual:
        print("Test passed")
    else:
        print("Test failed")
        print("Expected: ", expected)
        print("Actual: ", actual)

    print("Testing round_up_to_nearest_eighth_yard(1.1)")
    expected = 1.125
    actual = round_up_to_nearest_eighth_yard(1.1)
    if expected == actual:
        print("Test passed")
    else:
        print("Test failed")
        print("Expected: ", expected)
        print("Actual: ", actual)

    print("Testing round_up_to_nearest_eighth_yard(2.0)")
    expected = 2.0
    actual = round_up_to_nearest_eighth_yard(2.0)
    if expected == actual:
        print("Test passed")
    else:
        print("Test failed")
        print("Expected: ", expected)
        print("Actual: ", actual)


def test() -> None:
    """Runs the project test functions.

    Parameters:
    None

    Returns:
    None
    """
    test_get_whole_and_leftover_yards()
    test_round_up_to_nearest_eighth_yard()


def main() -> None:
    """Runs the main pillowcase yardage calculator program.

    Parameters:
    None

    Returns:
    None
    """
    # test()

    # get finished length
    finished_length_in_inches = prompt_for_length()
    if finished_length_in_inches == 0:
        finished_length_in_yards = 0.0
    else:
        finished_length_in_inches = add_seam_allowance(finished_length_in_inches)
        finished_length_in_yards = convert_to_yards(finished_length_in_inches)
        finished_length_in_yards = round_up_to_nearest_eighth_yard(finished_length_in_yards)

    # calculate the price
    price_per_yard = prompt_for_price()
    cost = finished_length_in_yards * price_per_yard

    # print the results
    print("")
    print_fabric(finished_length_in_yards)
    print_cost(cost)

if __name__ == "__main__":
    main()