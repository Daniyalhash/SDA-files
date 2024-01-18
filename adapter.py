from abc import ABC, abstractmethod

# Target Interface: Rectangle
class Rectangle(ABC):
    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

# Concrete Implementation of Rectangle
class ConcreteRectangle(Rectangle):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

# Adaptee: Square
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_side_length(self):
        return self.side_length

# Adapter: SquareAdapter
class SquareAdapter(Rectangle):
    def __init__(self, square):
        self.square = square

    def get_width(self):
        return self.square.get_side_length()

    def get_height(self):
        return self.square.get_side_length()

# Client
def print_rectangle_dimensions(rectangle):
    print(f"Width: {rectangle.get_width()}, Height: {rectangle.get_height()}")

# Client Code
if __name__ == "__main__":
    # Using a regular rectangle
    rectangle = ConcreteRectangle(10, 5)
    print_rectangle_dimensions(rectangle)

    # Using an adapted square as if it were a rectangle
    square = Square(7)
    adapted_square = SquareAdapter(square)
    print_rectangle_dimensions(adapted_square)
