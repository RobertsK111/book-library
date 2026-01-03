from book_manager import add_book, check_book, top_issued, top_price
from borrowing_manager import borrow_book, return_book, search_books, top_least_issued

DATA_PATH = "data/library_data.json"


def main():
    while True:
        print("\n=== Bibliotēkas sistēma ===")
        print("1. Pievienot/atjaunot grāmatu")
        print("2. Apskatīt visas grāmatas")
        print("3. Izsniegt grāmatu")
        print("4. Atgriezt grāmatu")
        print("5. Meklēt grāmatas (pēc nosaukuma)")
        print("6. Meklēt grāmatas (pēc autora)")
        print("7. Top 5 izsniegtās grāmatas")
        print("8. Top 5 dārgākās grāmatas")
        print("9. Top 5 vismazāk izsniegtās grāmatas")
        print("0. Iziet")

        choice = input("Izvēlies: ").strip()

        if choice == "1":
            title = input("Nosaukums: ").strip()
            author = input("Autors: ").strip()
            price = float(input("Cena: ").strip().replace(",", "."))
            available = int(input("Pieejamais skaits: ").strip())
            add_book(title, author, price, available, path=DATA_PATH)

        elif choice == "2":
            check_book(path=DATA_PATH)

        elif choice == "3":
            title = input("Nosaukums: ").strip()
            count = int(input("Cik izsniegt?: ").strip())
            print(borrow_book(title, count, path=DATA_PATH))

        elif choice == "4":
            title = input("Nosaukums: ").strip()
            count = int(input("Cik atgriezt?: ").strip())
            print(return_book(title, count, path=DATA_PATH))

        elif choice == "5":
            q = input("Meklēšanas teksts (nosaukums): ").strip()
            results = search_books(q, mode="title", path=DATA_PATH)
            for title, info in results:
                print(f"- {title} | {info.get('author', '-')}, pieejams: {info.get('available', 0)}")

        elif choice == "6":
            q = input("Meklēšanas teksts (autors): ").strip()
            results = search_books(q, mode="author", path=DATA_PATH)
            for title, info in results:
                print(f"- {title} | {info.get('author', '-')}, pieejams: {info.get('available', 0)}")

        elif choice == "7":
            top_issued(path=DATA_PATH)

        elif choice == "8":
            top_price(path=DATA_PATH)

        elif choice == "9":
            items = top_least_issued(n=5, path=DATA_PATH)
            for title, info in items:
                print(f"- {title} (issued: {info.get('issued', 0)})")

        elif choice == "0":
            print("Darbības beigas.")
            break

        else:
            print("Nepareiza izvēle.")


if __name__ == "__main__":
    main()