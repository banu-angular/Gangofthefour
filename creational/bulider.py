    # 🔌 Scenario: The Universal Travel Adapter
    # Imagine you are developing a Payment Processing System for an e-commerce site.
    # The Problem:
    # Your system is designed to work with a modern payment provider called SmartPay. However, a new client wants to use an old, legacy provider called OldSchoolBank.
    # SmartPay uses a method called makePayment(amount).
    # OldSchoolBank uses a completely different method called transferFunds(valueInCents, currency).
    # # You don't want to rewrite your entire app's logic just to support this one old bank. Instead, you create an Adapter.
# Adapter Pattern Implementation in Python
class PaymentAdapter:
    def __init__(self, old_bank):
        self.old_bank = old_bank

    def make_payment(self, amount):
        value_in_cents = int(amount * 100)
        currency = "USD"
        return self.old_bank.transfer_funds(value_in_cents, currency)

class OldSchoolBank:
    def transfer_funds(self, value_in_cents, currency):
        return f"Transferring {value_in_cents} {currency} through OldSchoolBank"

class SmartPay:
    def make_payment(self, amount):
        return f"Processing payment of ${amount} through SmartPay"
        
# Example usage:
if __name__ == "__main__":  
    smart_pay = SmartPay()
    old_bank = OldSchoolBank()
    adapter = PaymentAdapter(old_bank)
    print(smart_pay.make_payment(100))  # Processing payment of $100 through SmartPay
    print(adapter.make_payment(100))     # Transferring 10000 USD through OldSchoolBank
    print(smart_pay.make_payment(200))  # Processing payment of $200 through SmartPay
    print(adapter.make_payment(200))     # Transferring 20000 USD through OldSchoolBank