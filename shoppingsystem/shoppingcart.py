import shoppingsytem
import sqlite3 

items =[]
prices=[]
total = 0
def search_products(item):
    conn = sqlite3.connect(r'C:\Users\Keke\Documents\projects\shoppingsystem\productsdatabase.db')
    cursor = conn.cursor()
    
    search_term = item;

    cursor.execute("SELECT * FROM products WHERE productName LIKE ?", ('%' + search_term + '%',))

    results = cursor.fetchall()
    
    if results:
        print("Search Results:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Price: R{row[2]}")
              
    else:
        print("No products found.")
    
    conn.close()
    return results;

while True:
    item = input("enter item: ")
    search_products(item)
    if item.lower() == "q" :
        break
    else :
        price = float(input(f"enter price of {item} R"))
        items.append(item)
        prices.append(price)

print("-----------YOUR CART-------------")
for item in items:
    print(item)

for price in prices:
    total += price
    
print()
print(f"your total is: R{total}")
shoppingsytem.change(total)