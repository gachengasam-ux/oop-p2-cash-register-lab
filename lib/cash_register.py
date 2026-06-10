#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int):
            print("Not valid discount")
            return

        if value < 0 or value > 100:
            print("Not valid discount")
            return

        self._discount = value

    def add_item(self, item, price, quantity=1):
        """Add item with default quantity=1"""
        self.total += price * quantity
        
        # Add the item to items list for each quantity
        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """Apply discount if there is one, otherwise print message"""
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        
        # Calculate discount amount
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        
        
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        """Remove the last transaction and update total and items"""
        if len(self.previous_transactions) == 0:
            return

        last_transaction = self.previous_transactions.pop()
        
        # Remove items from the list by quantity
        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])
        
        # Subtract from total
        self.total -= last_transaction["price"] * last_transaction["quantity"]
  

     

      
     
     
