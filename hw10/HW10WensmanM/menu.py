"""HW 10 menu.py, provides user options for car lot inventory
    Class: CSC251
    Date: Spring 2026
"""

def showMenu():
  '''Prints a menu of user options
    Parameters: none
    Returns: choice(str): string input from user
  '''
  print("\nChoose an option:")
  print("(s)how inventory")
  print("(a)dd a car")
  print("(r)emove a car")
  print("(c)hange a car price")
  print("(e)xit program")
  choice = input()
  print()
  return choice
