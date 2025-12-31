
import json
from pathlib import Path
from typing import Any


def add_book(title, author, price, available, path='library_data.json'):
    with open(path, 'r', encoding='utf-8') as file:
         data = json.load(file)  #piekļuve JSON failam

    if title in data:   # ja gramata jau eksiste, tad atjaunina datus
        data[title]['author'] = author
        data[title]['price'] = price
        data[title]['available'] += available  # palielina pieejamo skaitu
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
         
    else:  # ja gramata neeksiste, tad pievieno jaunu ierakstu JSON faila
        data[title] = {
            'author': author,
            'price': price,
            'available': available,
            'issued': 0
        }
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
         



def check_book(path='library_data.json'):
    with open(path, 'r', encoding='utf-8') as file:
        data= json.load(file)
    
    if data == {}: # parbauda vai biblioteka nav tukša 
        print("Bibliotēka ir tukša")
        return
    else:
        for title, info in data.items(): # ja nav tukša, izvada visas grāmatas
            print("Nosaukums:" + title)
            print("Autors:" + info['author'])
            print("Cena:" + str(info['price']))
            print("Pieejams:" + str(info['available']))
            print("Izsniegts:" + str(info['issued']))   
            print("------------------------")




def top_issued(path='library_data.json'): 
    with open(path, 'r', encoding='utf-8') as file:
        data= json.load(file) #piekluve 

    if not data:
        print ("Bibliotēka ir tukša")
        return
    
    sorted_issued = sorted(data.items(), key=lambda x: x[1]['issued'], reverse=True)
    top5_issued = sorted_issued[:5] # sortošana

    print("Top 5 izsniegtās grāmatas:")
   
    for title,info in top5_issued: 
            print("Nosaukums: " + title)
            print("Issued: " + str(info['issued']))
            print("------------------------") # izvade




def top_price(path='library_data.json'):
    with open(path, 'r', encoding='utf-8') as file:
        data= json.load(file)

    if not data:
        print("Bibliotēka ir tukša")
        return
    sorted_price= sorted(data.items(), key=lambda x: x[1]['price'], reverse=True)
    top5_price = sorted_price[:5]

    print("Top 5 dārgākās grāmatas:")

    for title, info in top5_price:
        print("Nosaukums: " + title)
        print("Cena: "+  str(info['price']))
        print("------------------------")
    


    























#TODO: 
 
# Top 5 dargakas
#JSON saglabasana

