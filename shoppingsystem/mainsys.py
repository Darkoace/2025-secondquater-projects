import shoppingsytem
import sqlite3 

items =[]
prices=[]
total = 0
CustomerID = 0

def login():
    username = input("Enter your username: ")
 
    password = input("Enter your password: ")
    if password == "1234":
            print("Welcome to the system!")
            return 0
    else:
            print("Incorrect password.")
            return 1
    
if login() == 1:
    print("Exiting the system due to failed login.")
    exit()
else : #login() == 0:
    print("Login successful. Proceeding with the shopping system.")

while True:

    # Function to search for products in the database
    def search_products(item, quantity):
        import sqlite3

        conn = sqlite3.connect(r'C:\Users\Keke\Documents\projects\shoppingsystem\productsdatabase.db')
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS PRODUCTS (
                PRODUCTID INTEGER NOT NULL,
                productName TEXT NOT NULL PRIMARY KEY,
                price REAL NOT NULL,
                Stock INTEGER NOT NULL
            )
        ''')

        # Normalize search term for case-insensitive match
        search_term = item.lower()

        # Search for matching products
        cursor.execute("SELECT * FROM PRODUCTS WHERE LOWER(productName) LIKE ?", ('%' + search_term + '%',))
        results = cursor.fetchall()

        if results:
            print("Search Results:")
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}, Stock: {row[3]}")
        
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return None 
            # Check if enough stock is available
            if results and row[3] >= quantity:
                new_stock = row[3] - quantity
                cursor.execute("UPDATE PRODUCTS SET Stock = ? WHERE LOWER(productName) = ?", (new_stock, search_term))
                conn.commit()
            else:
                print("Not enough stock available.")
        else:
            print("No products found.")

        conn.close()
        return results

    while True :
        item = input("enter item: ")
        if item.lower() == "q" or item.lower() == "quit":
            break
        else :
                quantity = int(input("enter quantity: ")) 
                products = search_products(item,quantity)
                if products:
                    selected = products[0]  # use the first matched product
                    # Append the product name with quantity to items list
                    items.append(f"{selected[1]} x {quantity}")# product name with quantity  
                    # Append the product price to prices list
                    price = float(selected[2] * quantity)  # product price by quantity
                    prices.append(price)
                    total += price
    Moneypaid = float(input("enter amount paid: R"))
    itemID = selected[0]
    change = Moneypaid - total;
    print("change:{change}")
    shoppingsytem.change(change)


    # Save purchased items to a database
    def tillslip(CustomerID,items, prices, total, Moneypaid, change):
        conn = sqlite3.connect(r'C:\Users\Keke\Documents\projects\shoppingsystem\Productsdatabase.db')
        cursor = conn.cursor()
        # Create the PURCHASED_ITEMS table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS PURCHASED_ITEMS
                        (customerID real,item TEXT, price TEXT, total REAL, Moneypaid REAL, change REAL)''')
        # Insert purchased items into the database
        for item,price in zip( items, prices):
        #items = ', '.join(items)  # Convert list to string
            cursor.execute("INSERT INTO PURCHASED_ITEMS (CustomerID, item, price, total, moneypaid, change)VALUES (?,?, ?, ?, ?, ?)", 
                            ( CustomerID,item, price, 0,0,0))
            if item == items[-1]:
                cursor.execute("INSERT INTO PURCHASED_ITEMS (customerID,item, price, total, moneypaid, change)VALUES (?, ?, ?, ?, ?, ?)", 
                            ( CustomerID,0, 0, float(total), float(Moneypaid), float(change)))

        conn.commit()
        conn.close()

    
    print("-----------YOUR CART-------------")
    print(f"{CustomerID}") 
    print()
    for item, price in zip(items, prices):
        print(f"{item} - R{price}")   
    print()
    print(f"total Cost: R{total}")

    print(f"amount issuid: R{Moneypaid}")

    print(f"change : R{change}")

    # Assuming CustomerID is a variable that holds the customer's ID
    tillslip(CustomerID,items, prices, total, Moneypaid, change)
    
    print()
    print("Thank you for shopping with us!")
    CustomerID += 1;