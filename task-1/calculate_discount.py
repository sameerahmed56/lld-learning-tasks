from abc import ABC, abstractmethod


class Cart:
    def __init__(self, amount):
        self.amount = amount


class Discount(ABC):

    @abstractmethod
    def discount(self, amount: int):
        pass


class PercentageDiscount(Discount):
    def __init__(self, percentage: int):
        self.validate_percentage(percentage)
        self.percentage = percentage

    def validate_percentage(self, percentage: int):
        if (percentage < 0 or percentage > 100):
            raise ValueError('invalid percentage')

    def discount(self, amount):
        return amount - (amount * self.percentage / 100)


class FixedDiscount(Discount):
    def __init__(self, fixed_amount: int):
        self.validate_fixed_amount(fixed_amount)
        self.fixed_amount = fixed_amount

    def validate_fixed_amount(self, fixed_amount: int):
        if (fixed_amount < 0):
            raise ValueError('invalid fixed amount')

    def discount(self, amount: int):
        return max(0, amount - self.fixed_amount)


class CalculateDiscount:
    def __init__(self):
        pass

    def calculate(self, amount: int, discount_type: Discount):
        return discount_type.discount(amount)


shopping_cart = Cart(100)
ten_percentage_discount = PercentageDiscount(10)
fifty_fixed_discount = FixedDiscount(50)
print(CalculateDiscount().calculate(shopping_cart.amount, ten_percentage_discount))
print(CalculateDiscount().calculate(shopping_cart.amount, fifty_fixed_discount))
