#Lecture 10 code
from coins import Coin

def main():
    # Create an object from the Coin class.
    my_coin = Coin()

    #print('This side is up:', my_coin.get_sideup())
    print('This side is up:', my_coin.sideup)

    # Toss the coin 10 times and output the result
    print('I am going to toss the coin ten times:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.sideup)

if __name__ == '__main__':
      main()

