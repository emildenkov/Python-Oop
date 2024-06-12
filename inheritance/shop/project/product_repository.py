from typing import List
from project.food import Food
from project.drink import Drink


class ProductRepository:

    def __init__(self):
        self.products: List[Food, Drink] = []

    def add(self, product: Food or Drink) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> str:
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str):
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join(f"{p.name}: {p.quantity}" for p in self.products)

