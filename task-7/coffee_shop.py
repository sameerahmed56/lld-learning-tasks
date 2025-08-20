from abc import ABC, abstractmethod


class Beverage(ABC):

    @abstractmethod
    def calculate_price(self):
        pass


class Espresso(Beverage):

    def calculate_price(self):
        return 100


class CondimentBeverage(Beverage):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        super().__init__()

    def calculate_price(self):
        return self.beverage.calculate_price()


class MilkCondiment(CondimentBeverage):

    def calculate_price(self):
        return super().calculate_price() + 20


class MochaCondiment(CondimentBeverage):

    def calculate_price(self):
        return super().calculate_price() + 30


espresso = Espresso()
milk_espresso = MilkCondiment(Espresso())
mocha_espresso = MochaCondiment(Espresso())
mocha_and_milk_espresso = MochaCondiment(milk_espresso)

print(f'Espresso price {espresso.calculate_price()}')
print(f'Milk Espresso price {milk_espresso.calculate_price()}')
print(f'Mocha Espresso price {mocha_espresso.calculate_price()}')
print(f'Mocha and Milk Espresso price {mocha_and_milk_espresso.calculate_price()}')
