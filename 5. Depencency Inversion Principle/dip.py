# Il nous permet d'ajouter de l'abstraction à notre application, ce qui signifie simplement notre niveau élevé.
# Les modules ne devraient pas avoir d'impact sur nos modules de bas niveau à moins que nous le lui demandions spécifiquement.

class PaymentGateway:
    def proccess_payment(self, amount):
        print("Making payment on Stripe")
        print("Making payment on Venmo")
        pass
    
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class Order:
    def __init__(self, order_id, items, payment_gateway):
        self.order_id = order_id
        self.items = items
        self.payment_gateway = payment_gateway
        
    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total
    
    def place_order(self):
        total = self.calculate_total()
        # Perform order placement logic
        self.payment_gateway.proccess_payment(total)

# High-level module
class OrderManager:
    def __init__(self, order):
        self.order = order    
    
    def place_order(self):
        self.order.place_order()
        
payment_gateway = PaymentGateway()
order_items = [
    Item("Product 1", 10),
    Item("Product 2", 20),
    Item("Product 3", 15)
]
order = Order(123, order_items, payment_gateway)
order_manager = OrderManager(order)
order_manager.place_order()

