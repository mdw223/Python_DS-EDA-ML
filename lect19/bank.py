# This program demonstrates the BankAccount class with the __str__ method.
from bankaccountdefault import BankAccount

def main():
    # Get the starting balance.
#    start_bal = float(input('Enter your starting balance: '))

    # Create a BankAccount object.
    savings = BankAccount()
    print(savings)

    # Deposit the user's paycheck.
#    pay = float(input('How much were you paid this week? '))
#    print('I will deposit that into your account.')
    savings.deposit()
    print(savings)

    # Display the balance.
    print(savings)

    # Get the amount to withdraw.
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    savings.withdraw(cash)

    # Display the balance.
    print(savings)

if __name__ == '__main__':
      main()
