class Product:

    def __init__(self, name = '', price = 0.0, discount = 0):
        self.__name = name
        self.__price = price
        self.__discount = discount

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, p):
        self.__price = p

    @property
    def discount(self):
        return self.__discount
    
    @discount.setter
    def discount(self, d):
        self.__discount = d

    def compute_new_price(self):
        return f'$ {self.__price * (1 - self.__discount / 100):,.2f}'

    def __str__(self):
        return f'Product name: {self.__name}, Price: $ {self.__price:,.2f}, Discount: {self.__discount}%'

class Tea(Product):
    def __init__(self, name = '', price = 0.0, discount = 0, flavor = ''):
        super().__init__(name, price, discount)
    
        self.__flavor = flavor

    def __str__(self):
        return super().__str__() + f", flavor: {self.__flavor}"


def main():
    thing = Product('widget', 100, 10)
    print(thing)
    print('Discounted price: ', thing.compute_new_price())

    thing.discount = 25
    print(thing)
    print('Discounted price: ', thing.compute_new_price())

    cup = Tea("Bigelow 40 count tea bags", 4.99, 10, "Earl Grey")
    print(cup)


if __name__ == "__main__":
    main()
