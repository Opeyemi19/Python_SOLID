# Chaque classe ou objet ou méthode dans l'ensemble de l'application ne doit avoir qu'une seule responsabilité, ce qui permet de réduire les bugs tout en augmentant les performances de l'application.
# Chaque élément de votre code doit être complètement organisé, de sorte qu'il n'y a qu'une responsabilité pour chaque morceau de code spécifique de votre application.

class Item:
    def __init__(self, name, price):
        """This is initial function

        Args:
            name (string): A name of each item.
            price (number): A number of each item.
        """
        self.name = name
        self.price = price
           
class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
        
    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total
    
class OrderManager:
    def place_order(self, order):
        total = order.calculate_total()
        print(f'total is: {total}')
        
order_items = [
    Item("Product 1", 10),
    Item("Product 2", 20),
    Item("Product 3", 15)
]
order = Order(123, order_items)
order_manager = OrderManager()
order_manager.place_order(order)