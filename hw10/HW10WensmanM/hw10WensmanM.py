'''
Author: Malik Wensman
Email: mdwensma@ncsu.edu
Class: CSC 251-001 Fall 2026
Program: HW10
Purpose: This program manages the inventory for a car dealership.
Bugs: None
Acknowledgements: None
Date: 11/12/2026
'''
import sys
import menu
from car import Car, CarLot

def exit_program(car_lot: CarLot, exit_code: int):
    car_lot.writeFile(input("Enter the name of the file to save to: "))
    sys.exit(exit_code)

def get_car_info():
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    year = input("Enter the year the car was manufactured: ")
    price = input("Enter the price of the car: ")
    return make, model, year, price

def main():
    '''
    Reads in the car data frim a text file specified by the user.
    The user will be provided with a menu of 5 options.
    They may select show to see a list of all cars on the lot, 
    they may add a new car, remove a car from inventory, 
    change the price of a car,
    or exit the program. 
    Upon exiting, all changes to the inventory should automatically 
    be saved in a text file specified by the user
    '''

    car_lot = CarLot()
    try:
        print("*** Welcome to the Car Lot ***")
        file_name = input("Enter name of car data input file: ")
        car_lot.readFile(file_name)
        choice = menu.showMenu()
        while choice != 'e':
            if choice == 's':
                car_lot.showCars()
            elif choice == 'a':
                make, model, year, price = get_car_info()
                car_lot.addCar(Car(make, model, year, price))
            elif choice == 'r':
                car_lot.removeCar(input(f"Enter car number (1 to {len(car_lot.car_list)}): "))
            elif choice == 'c':
                car_lot.changePrice(input(f"Enter car number (1 to {len(car_lot.car_list)}): "), input("Enter new price: "))
            
            choice = menu.showMenu()

        exit_program(car_lot, 0)
    except Exception as e:
        print(e)
        exit_program(car_lot, 1)

if __name__ == "__main__":
    main()