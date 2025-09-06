from abc import ABC, abstractmethod


def check_item_quantity(machine, item_id: int):
    if (machine.items[item_id]['quantity'] > 0):
        machine.items[item_id]['quantity'] -= 1
        machine.set_state(DispensingVendingState(machine))
    else:
        machine.set_state(ItemSoldVendingState(machine))


class VendingState(ABC):
    def __init__(self, machine):
        self.machine = machine

    @abstractmethod
    def button_pressed(self):
        pass

    @abstractmethod
    def insert_coin(self):
        pass

    @abstractmethod
    def item_pressed(self, item_id: int):
        pass


class HasCoinVendingState(VendingState):

    def button_pressed(self):
        return "Please select item"

    def insert_coin(self):
        return "Coin already there"

    def item_pressed(self, item_id: int):
        check_item_quantity(self.machine, item_id)
        return f"Item now selected is {self.machine.items[item_id]['name']}"


class ItemSoldVendingState(VendingState):

    def button_pressed(self):
        self.machine.set_state(HasCoinVendingState(self.machine))
        return "Item is Sold Out, please select another item"

    def insert_coin(self):
        return "Coin already there"

    def item_pressed(self, item_id: int):
        check_item_quantity(self.machine, item_id)
        return f"Item now selected is {self.machine.items[item_id]['name']}"


class NoCoinVendingState(VendingState):

    def button_pressed(self):
        return "Please enter coin"

    def insert_coin(self):
        self.machine.set_state(HasCoinVendingState(self.machine))
        return "Coin inserted, please select item"

    def item_pressed(self, item_id: int):
        return f"Please enter coin to get item {self.machine.items[item_id]['name']}"


class DispensingVendingState(VendingState):

    def button_pressed(self):
        self.machine.set_state(NoCoinVendingState(self.machine))
        return "ITEM DISPENSED"

    def insert_coin(self):
        return "Coin already there"

    def item_pressed(self, item_id: int):
        check_item_quantity(self.machine, item_id)
        return f"Item now selected is {self.machine.items[item_id]['name']}"
