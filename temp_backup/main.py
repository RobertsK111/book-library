import book_manager


def main():
    while True:
        print("\n=== Bibliotēkas sistēma ===")
        print("1. Pievienot / atjaunināt grāmatu")
        print("2. Apskatīt visas grāmatas")
        print("0. Iziet")

        choice = input("Izvēlies darbību: ")

        if choice == "1":
            title = input("Nosaukums: ")
            author = input("Autors: ")

            try:
                price = float(input("Cena: "))
                available = int(input("Pieejamais skaits: "))
            except ValueError:
                print("Kļūda: cena vai skaits nav skaitlis")
                continue

            book_manager.add_book(title, author, price, available)
            print("Grāmata veiksmīgi pievienota / atjaunināta!")

        elif choice == "2":
            book_manager.check_book()

        elif choice == "0":
            print("Programma tiek aizvērta.")
            break

        else:
            print("Nepareiza izvēle, mēģini vēlreiz.")


if __name__ == "__main__":
    main()
