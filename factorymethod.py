from abc import ABC, abstractmethod

# Product interface
class Product(ABC):
    @abstractmethod
    def create(self):
        pass

# Concrete Product A
class ConcreteProductA(Product):
    def create(self):
        return "Product A"

# Concrete Product B
class ConcreteProductB(Product):
    def create(self):
        return "Product B"

# Creator interface
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def get_product(self):
        product = self.factory_method()
        return f"Created {product.create()}"

# Concrete Creator A
class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

# Concrete Creator B
class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Client code
creator_a = ConcreteCreatorA()
result_a = creator_a.get_product()
print(result_a)

creator_b = ConcreteCreatorB()
result_b = creator_b.get_product()
print(result_b)
