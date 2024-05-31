# Il devrait nous permettre d'utiliser les interfaces comme une relation, mais nous ne devrions utiliser que les interfaces que nous devons être capables de créer ou d'effectuer une action spécifique dans notre application.
# Il augmente la flexibilité, les performances et permettre à notre application de réellement pouvoir évoluer en suivant ce principe.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def area(self):
        return self.width * self.height
    
class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height
        
def print_area(rectangle):
    rectangle.set_width(4)
    rectangle.set_height(5)
    area = rectangle.area()
    print("Area:", area)
    
rectangle = Rectangle(0, 0)    
square = Square(0, 0)

print_area(rectangle)
print_area(square)