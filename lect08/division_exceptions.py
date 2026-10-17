# This program divides two numerical values.

def main():
    try:
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter another number: '))

        #Could be moved to the else
        result = num1/num2

        #Could be moved to else
        #print(result)
        
    except ZeroDivisionError as err:
        print(err)
        print('Error: Cannot divide by zero!')
    
    except ValueError as err:
        print(err)
        print('You must enter a numerical value!')
    
    else:
        #only prints if no exception thrown
        print(result)

        

if __name__ == '__main__':
    main()

