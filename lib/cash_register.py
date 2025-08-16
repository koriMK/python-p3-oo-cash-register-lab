#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0  # Initialize as float
        self.items = []
        self.last_transaction = {
            'amount': 0.0,
            'items': []
        }
    
    def add_item(self, title, price, quantity=1):
        item_cost = price * quantity
        self.total += item_cost
        self.last_transaction = {
            'amount': item_cost,
            'items': [title] * quantity
        }
        self.items.extend([title] * quantity)
    
    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
            return self.total
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        self.total -= self.last_transaction['amount']
        # Remove all items from the last transaction
        for item in self.last_transaction['items']:
            if item in self.items:
                self.items.remove(item)
        # Reset last transaction
        self.last_transaction = {
            'amount': 0.0,
            'items': []
        }