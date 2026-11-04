import random

class Coin:
  """
  A class representing a coin.
  Attributes:
    sideup (str): The value of the side facing up, 'Heads' or 'Tails'
  """
       
  def __init__(self):
    """
    Initializes a new Coin object.
    Args: None
    """
    self.__sideup = 'Heads'

  def toss(self):
    """
    Changes the side facing up based upon random number 0 or 1.
    Args: None
    """
    if random.randint(0, 1) == 0:
      self.__sideup = 'Heads'
    else:
      self.__sideup = 'Tails'

  @property
  def sideup(self):
    """
    Accessor for the sideup attribute.
    Returns: 
      str: The side of the coin facing up
    """
    return self.__sideup



class Coins:
  """
  A class representing a collection of coins as a list.
  Attributes:
    clist (list): A list containing the coin objects
  """
  def __init__(self):
    """
    Initializes the list for Coin objects.
    Args: None
    """
    self.__clist = []
  
  @property
  def clist(self):
    """
    Accessor for the list of Coins.
    Returns: 
      list: The list of Coin objects
    """
    return self.__clist

  def toss_all(self):
    """
    Changes the side facing up for each coin in clist.
    Args: None
    """
    for coin in self.__clist:
      coin.toss()

  def add_coin(self, coinObj):
    """
    Mutator method to add a new Coin object to clist.
    Args: 
      coinObj (Coin): the new Coin object to be added to clist
    """
    self.__clist.append(coinObj)
