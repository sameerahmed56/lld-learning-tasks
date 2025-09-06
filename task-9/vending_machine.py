from vending_state import VendingState, NoCoinVendingState


class VendingMachine:

    def __init__(self, state: VendingState, vending_machine_items: dict):
        self.current_state = state
        self.items = vending_machine_items

    def set_state(self, state: VendingState):
        self.current_state = state

    def button_pressed(self):
        return self.current_state.button_pressed()

    def insert_coin(self):
        return self.current_state.insert_coin()

    def press_item(self, item_id: int):
        return self.current_state.item_pressed(item_id)


items = {1: {'name': 'coke', 'quantity': 10},
         2: {'name': 'pepsi', 'quantity': 10},
         3: {'name': 'fanta', 'quantity': 10}}

vending_machine = VendingMachine(None, items)
no_coin_state = NoCoinVendingState(vending_machine)
vending_machine.set_state(no_coin_state)
print(vending_machine.button_pressed())
print(vending_machine.insert_coin())
print(vending_machine.press_item(1))
print(vending_machine.button_pressed())
print(vending_machine.press_item(1))
