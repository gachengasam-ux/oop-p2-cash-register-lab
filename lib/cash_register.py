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

    def add_item(self, item, price, quantity):
        self.total += price * quantity
        self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if len(self.previous_transactions) == 0:
            print("There is no discount to apply.")
            return

        last_transaction = self.previous_transactions.pop()

        if last_transaction["item"] in self.items:
            self.items.remove(last_transaction["item"])

        self.total -= last_transaction["price"] * last_transaction["quantity"]
        self.total -= self.total * (self.discount / 100)

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            return

        last_transaction = self.previous_transactions.pop()

        if last_transaction["item"] in self.items:
            self.items.remove(last_transaction["item"])

        self.total -= last_transaction["price"] * last_transaction["quantity"]      
      
  

     

      
     
     
