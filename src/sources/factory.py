#!/usr/bin/python3.7
#*--------------------------------------------------
#* factory.py
#* excerpt from https://refactoring.guru/design-patterns/factory/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    La clase Creator declara el método de fábrica que se supone que debe devolver un
    objeto de una clase de Producto. Las subclases del Creador normalmente proporcionan la
    implementación de este método.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}\n"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class ConcreteCreator1(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Soy un camión}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Soy una lancha}"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long ascreator.some_operation() the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Yo soy un mero intermediario tipo FACTORY que no se que es lo que estoy creando, pero lo creo.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":

    print("\n\n")
    print("App: Creando un camión")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Creo otro camión")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Creando una lancha")
    client_code(ConcreteCreator2())
