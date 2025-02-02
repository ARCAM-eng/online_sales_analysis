# product_manager.py
from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)
        print(f"Produsul {name} a fost adaugat.")

    def display_all_products(self):
        if not self.products:
            print("Nu există produse în lista.")
        else:
            for product in self.products:
                product.display_info()

    def calculate_total_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Valoarea totala a stocului este: {total_value}")
        
    def remove_product(self, name):
     for product in self.products:
        if product.name == name:
            self.products.remove(product)
            print(f"Produsul {name} a fost eliminat.")
            return
     print(f"Produsul {name} nu a fost gasit.")