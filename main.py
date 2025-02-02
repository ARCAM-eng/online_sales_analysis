# main.py
from product_manager import ProductManager

def main():
    # Lista initiala este goala
    manager = ProductManager()

    while True:
        # Meniu interactiv
        print("\n--- Meniu ---")
        print("1. Adaugare produs")
        print("2. Eliminare produs")
        print("3. Iesire")
        
        choice = input("Alegeti o opțiune : ")

        if choice == "1":
            # Adaugare produs
            name = input("Introduceti numele produsului: ")
            price = float(input("Introduceti pretul : "))
            quantity = int(input("Introduceti cantitatea : "))
            manager.add_product(name, price, quantity)

             
        elif choice == "2":
            # Eliminare produs
            name = input("Introduceți numele produsului de eliminat: ")
            manager.remove_product(name)

        elif choice == "3":
            # Iesire din program
            print("Iesire din program.")
            break

        else:
            # Opțiune invalidă
            print("Optiune invalidă! ")

if __name__ == "__main__":
    main()