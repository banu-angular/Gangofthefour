# Visualize a Vending Machine. Its behavior changes depending on its internal state: No Coin, Has Coin, or Out of Stock. If you press the "Dispense" button while in the No Coin state, it shows an error; if you press it in the Has Coin state, it delivers the snack and transitions back to the No Coin state. The machine reacts differently to the same input based on its current condition.
class State:
    def dispense(self):
        pass
class NoCoinState(State):
    def dispense(self):
        print("Error: No coin inserted")
class HasCoinState(State):
    def dispense(self):
        print("Dispensing snack...")
class OutOfStockState(State):
    def dispense(self):
        print("Error: Out of stock")
class VendingMachine:
    def __init__(self):
        self.no_coin_state = NoCoinState()
        self.has_coin_state = HasCoinState()
        self.out_of_stock_state = OutOfStockState()
        self.state = self.no_coin_state

    def insert_coin(self):
        if self.state == self.no_coin_state:
            print("Coin inserted.")
            self.state = self.has_coin_state
        else:
            print("Coin already inserted or machine is out of stock.")

    def dispense(self):
        self.state.dispense()
        if self.state == self.has_coin_state:
            self.state = self.no_coin_state
# Usage Example
vending_machine = VendingMachine()
vending_machine.insert_coin()
vending_machine.dispense()
vending_machine.insert_coin()
vending_machine.dispense()
vending_machine.insert_coin()
vending_machine.state = vending_machine.out_of_stock_state  # Simulate out of stock
vending_machine.dispense()
# Output:
# Coin inserted.
# Dispensing snack...

# Coin inserted.
# Dispensing snack...
# Error: Out of stock   

