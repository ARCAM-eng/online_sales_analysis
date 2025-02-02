# main.py
from product_manager import ProductManager
from cart import Cart


def main():
    # Lista initiala este goala
    manager = ProductManager()
    manager_basket = Cart()
    

    while True:
        # Meniu interactiv
        print("\n--- Meniu ---")
        print("1. Adaugare produs")
        print("2. Afisare toate produsele")
        print("3. Calcul valoare totala inventar")
        print("4. Eliminare produs")
        print("5. Adaugare produs in cos")
        print("6. Valoarea totala a cosului")
        print("7. Afisare produse din cos")
        print("8. Iesire")
        
        choice = input("Alegeti o opțiune : ")

        if choice == "1":
            # Adaugare produs
            name = input("Introduceti numele produsului: ")
            price = float(input("Introduceti pretul : "))
            quantity = int(input("Introduceti cantitatea : "))
            manager.add_product(name, price, quantity)

        elif choice == "2":
            # Afisare toate produsele
            print("\nToate produsele:")
            manager.display_all_products()

        elif choice == "3":
            # Calcul valoare totala stoc
            manager.calculate_total_value()
        
        elif choice == "4":
            # Eliminare produs
            name = input("Introduceți numele produsului de eliminat: ")
            manager.remove_product(name)

        elif choice == "5":
            # Adaugare produs in cos
            name = input("Introduceți numele produsului de adaugat in cos: ")
            product_found = None
            for product in manager.products:
                if product.name == name:
                    product_found = product
                    break
            if product_found:
                manager_basket.add_to_cart(product_found)
            else:
                print(f"Produsul {name} nu este in stoc.")
            
        elif choice == "6":
            # Valoarea totala a cosului
            total_basket = manager_basket.calculate_total()
            print(f"Valoarea coșului este: {total_basket}")
            
        elif choice == "7":
            # Afisare produse din cos
              manager_basket.display_cart()
            
        elif choice == "8":
            # Iesire din program
            print("Iesire din program.")
            break

        else:
            # Optiune invalidă
         print("Optiune invalidă! ")

if __name__ == "__main__":
    main()