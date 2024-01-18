from abc import ABC, abstractmethod

# Implementor
class DrawingAPI(ABC):
    @abstractmethod
    def draw_circle(self, x, y, radius):
        pass

# Concrete Implementors
class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API1: Drawing circle at ({x}, {y}) with radius {radius}")

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API2: Drawing circle at ({x}, {y}) with radius {radius}")

# Abstraction
class Shape:
    def __init__(self, drawing_api):
        self.drawing_api = drawing_api

    def draw(self, x, y, radius):
        self.drawing_api.draw_circle(x, y, radius)

# Client Code
if __name__ == "__main__":
    api1 = DrawingAPI1()
    api2 = DrawingAPI2()

    circle1 = Shape(api1)
    circle2 = Shape(api2)

    circle1.draw(1, 2, 3)
    circle2.draw(5, 7, 11)
