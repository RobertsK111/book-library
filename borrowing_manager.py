import json

DATA_PATH = "data/library_data.json"

def load_data(path=DATA_PATH):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_data(data, path=DATA_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def borrow_book(title, count, path=DATA_PATH):
    title = title.strip()

    try:
        count = int(count)
    except ValueError:
        return "Skaitlim ir jābūt Veselam skaitlim!"
    
    if count <= 0:
        return "Skaitam ir jābūt lielākam par 0"
    
    data = load_data(path)

    if title not in data:
        return (f"Grāmata ar nosaukumu ({title}) nav atrasta")
    
    if data[title]["available"] < count:
        return (f"Nav pieejamu eksemplāru grāmatai {title}")
    
    data[title]["available"] -= count
    data[title]["issued"] += count

    save_data(data, path)
    return "Grāmata ir izsniegta"


def return_book(title, count, path = DATA_PATH):
    title = title.strip()

    try:
        count = int(count)
    except ValueError:
        return "Skaitam ir jābūt veselam skaitlim"
    if count <= 0:
        return "Skaitam ir jābūt lielākam par 0"
    
    data = load_data(path)

    if title not in data:
        return (f"Grāmata ar nosaukumu ({title}) nav atrasta")
    
    if data[title]["issued"] < count:
        return "Nevar atgriezt grāmatu kas nav izsniegta"
    
    data[title]["available"] += count
    data[title]["issued"] -= count

    save_data(data, path)
    return "Grāmata ir atgriezta"

def search_books(query, mode="title", path=DATA_PATH):
    query = query.strip().lower()
    data = load_data(path)

    results = []

    if mode == "title":
        for title in data:
            if query in title.lower():
                results.append((title, data[title]))

    elif mode == "author":
        for title in data:
            author = data[title]["author"].lower()
            if query in author:
                results.append((title, data[title]))

    return results

def top_least_issued(n=5, path = DATA_PATH):
    data = load_data(path)
    items = list(data.items())

    items.sort(key = lambda x: x[1]["issued"])
    return items[:n]
