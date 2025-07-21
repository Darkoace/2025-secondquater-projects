import shoppingsytem

items =[]
prices=[]
total = 0

while True:
    item = input("enter item: ")
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