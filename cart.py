
from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart (self, product):
        self.cart_items.append(product)
        print(f"Produsul {product.name} a fost adaugat în coș.")

    def calculate_total(self):
        total_basket = sum(product.price for product in self.cart_items)
        return total_basket

    def display_cart(self):
        if not self.cart_items:
            print("Cosul este gol.")
        else:
            print("Continutul cosului:")
            for product in self.cart_items:
                print(f"Produs: {product.name}, Pret: {product.price}")