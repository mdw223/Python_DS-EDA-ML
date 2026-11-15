'''
Author: Malik Wensman
Email: mdwensma@ncsu.edu
Class: CSC 251-001 Fall 2026
Program: HW10
Purpose: This module contains the Car and CarLot classes.
Bugs: None
Acknowledgements: None
Date: 11/12/2026
'''

import sys

DEFAULT_PRICE = 28000
DEFAULT_YEAR = 2026
DEFAULT_MIN_YEAR = 1900

class Car:
    """
    One vehicle in the dealership inventory.

    Attributes:
        __make (str): manufacturer name
        __model (str): model name
        __year (int): model year; values before 1900 are replaced with 2026
        __price (int): price in dollars, rounded to the nearest integer
    """
    def __init__(self, make: str, model: str, year: int, price):
        """
        Create a car, replacing an invalid year or price with the defaults.

        A price below 0 is set to 28000. A year before 1900 is set to 2026.
        The price is rounded to the nearest integer. A year or price that
        cannot be converted to a number raises Exception.

        Parameters:
            make (str): manufacturer name
            model (str): model name
            year (int): model year
            price: price in dollars; converted with float, then rounded
        """
        try:
            price = int(round(float(price)))
            if (price < 0):
                print("Price must be greater than 0, setting to $28,000")
                price = DEFAULT_PRICE

            year = int(year)
            if (year < DEFAULT_MIN_YEAR):
                print(f"Year must be greater than {DEFAULT_MIN_YEAR}, setting to {DEFAULT_YEAR}")
                year = DEFAULT_YEAR

            self.__make = make
            self.__model = model
            self.__year = year
            self.__price = price
        except:
            raise Exception("Invalid car number.")
        
    @property
    def make(self) -> str:
        """
        Return the car's manufacturer.

        Returns:
            make (str): manufacturer name
        """
        return self.__make

    @property
    def model(self) -> str:
        """
        Return the car's model.

        Returns:
            model (str): model name
        """
        return self.__model

    @property
    def year(self) -> int:
        """
        Return the car's model year.

        Returns:
            year (int): model year
        """
        return self.__year

    @property
    def price(self) -> float:
        """
        Return the car's price.

        Returns:
            price (float): price in dollars
        """
        return self.__price

    @price.setter
    def price(self, price: float):
        """
        Set the car's price.

        Parameters:
            price (float): new price in dollars
        """
        self.__price = price
    
    def __str__(self) -> str:
        """
        Return the car as year, make, and model.

        Returns:
            description (str): formatted as "year make model"
        """
        return f"{self.__year} {self.__make} {self.__model}"

class CarLot:
    """
    A collection of Car objects, one list element per vehicle.

    Attributes:
        __car_list (list[Car]): cars currently in inventory
    """
    def __init__(self):
        """
        Create an empty car lot.
        """
        self.__car_list = []
    
    @property
    def car_list(self) -> list[Car]:
        """
        Return the cars currently in inventory.

        Returns:
            car_list (list[Car]): the inventory list
        """
        return self.__car_list

    def readFile(self, file_name: str):
        """
        Read car data from a text file and store each row as a Car.

        Each line is "make model year price", separated by single spaces.
        An I/O error prints the default error message and ends the program.

        Parameters:
            file_name (str): path to the input file
        """
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    make, model, year, price = line.split(' ')
                    self.__car_list.append(Car(make, model, int(year), float(price)))
        except IOError as e:
            print(e)
            sys.exit(1)
        

    def showCars(self):
        """
        Print a numbered list of every car and its price.
        """
        print("Car Lot Inventory")
        print("------------------------------")
        for index,car in enumerate(self.__car_list, start=1):
            print(f"{index} {car} ${car.price:,}")
    
    def addCar(self, car: Car):
        """
        Add a car to the inventory and confirm the addition.

        Parameters:
            car (Car): the car to add
        """
        self.__car_list.append(car)
        print(f"{car} added.")
    
    def removeCar(self, car_number):
        """
        Remove the car at the given inventory number and confirm the removal.

        Inventory numbers start at 1. A number outside that range, or a value
        that is not an integer, raises Exception.

        Parameters:
            car_number: inventory number of the car to remove
        """
        try:
            car_number = int(car_number)
            if car_number < 1 or car_number > len(self.__car_list):
                raise Exception("Invalid car number.")
            car = self.__car_list.pop(car_number - 1)
            print(f"{car} removed.")
        except:
            raise Exception("Invalid car number.")

    
    def changePrice(self, car_number, new_price):
        """
        Change the price of the car at the given inventory number.

        A price below 0 is replaced with 28000, then the price is rounded
        to the nearest integer. An invalid car number or a price that cannot
        be converted to a number raises Exception.

        Parameters:
            car_number: inventory number of the car to update, starting at 1
            new_price: new price in dollars
        """
        try:
            car_number = int(car_number)
            new_price = float(new_price)
            if (new_price < 0):
                print("Price must be greater than 0, setting to $28,000")
                new_price = DEFAULT_PRICE
            new_price: int = int(round(float(new_price)))
            self.__car_list[car_number - 1].price = new_price
            car = self.__car_list[car_number - 1]
            print(f"{car} price changed to ${new_price:,}")
        except:
            raise Exception("Invalid car number.")
    
    def writeFile(self, file_name: str):
        """
        Write the current inventory to a text file, one car per line.

        Each line is "make model year price". A confirmation is printed
        after the file is written.

        Parameters:
            file_name (str): path to the output file
        """
        with open(file_name, 'w') as file:
            for car in self.__car_list:
                file.write(f"{car.make} {car.model} {car.year} {car.price}\n")
        print(f"\nInventory written to {file_name}.")
