# main.py
from product_manager import ProductManager

def main():
    # Lista initiala este goala
    manager = ProductManager()

    while True:
        # Meniu interactiv
        print("\n--- Meniu ---")
        print("1. Adaugare produs")
        print("2. Afisare toate produsele")
        print("3. Calcul valoare totala inventar")
        print("4. Eliminare produs")
        print("5. Iesire")
        
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
            # Iesire din program
            print("Iesire din program.")
            break

        else:
            # Opțiune invalidă
            print("Optiune invalidă! ")

if __name__ == "__main__":
    main()