#TODO: Pievienot fukncijas no borrowing_manager

from book_manager import add_book, check_book, top_issued, top_price
# from borrowing_manager import borrow_book, return_book

def main():
    while True:
        print("\n Bibliotēkas sistēma")
        print("1. Pievienot/atjaunot grāmatu")
        print("2. Apskatīt visas grāmatas")
        print("3. Top 5 izsniegtās grāmatas")
        print("4. Top 5 dārgākās grāmatas")
        print("0. Iziet")

        choice = input("Izvēlies: ")

        if choice == "1":
            title = input("Nosaukums: ")
            author = input("Autors: ")
            price = float(input("Cena: "))
            available = int(input("Pieejamais skaits: "))
            add_book(title, author, price, available)

        elif choice == "2":
            check_book()
        elif choice == "3":
            top_issued()
        elif choice == "4":
            top_price()
        elif choice == "0":
            print("Darbības beigas.")
            break

        else:
             print("Nepareiza izvēle")

if __name__ == "__main__":
     main()