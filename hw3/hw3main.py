"""
 Author: Malik Wensman
 Email: mdwensma@ncsu.edu
 Class: CSC 251-001 Fall 2026
 Program: hw3mian.py
 Purpose: Produce a table that converts heights in feet and inches to centimeters
 Bugs: None
 Acknowledgements: None
"""

try:
    from hw3.header import header
    import hw3.hw3functions as functions
except ModuleNotFoundError:
    # Allow running the script directly from the hw3/ directory (e.g., for student testing).
    from header import header
    import hw3functions as functions

def main() -> None:
    """Run the program to produce a conversion table from feet/inches to centimeters.

    Parameters:
    None

    Returns:
    None
    """

    start_feet, start_inches = functions.get_values('starting', 0, 0)
    end_feet, end_inches = functions.get_values('ending', start_feet, start_inches)

    current_feet = start_feet
    current_inches = start_inches

    print()
    print()
    header()
    
    while(current_feet < end_feet or (current_feet == end_feet and current_inches <= end_inches)):
        centimeters = functions.convert_values(current_feet, current_inches)
        functions.print_table(current_feet, current_inches, centimeters)

        current_inches += 1
        if current_inches == functions.INCHES_PER_FOOT:
            current_inches = 0
            current_feet += 1

'''
Run the program directly with the input (shows stdout and any stderr):
python3 hw3/hw3main.py < hw3/inputs/input01.txt

See outputs:
python3 hw3/hw3main.py < hw3/inputs/input01.txt > hw3/tmp/out.txt 2>hw3/tmp/err.txt
ls -l hw3/tmp/out.txt hw3/tmp/err.txt
sed -n '1,120p' hw3/tmp/err.txt
sed -n '1,120p' hw3/tmp/out.txt

'''
if __name__ == "__main__":
    main()