inventry = [("laptop" , 50000),("mouse",500),("keyboard",1500)]
total_price = 0 
for (itam_name , price )in inventry:
    print(f"item :{itam_name}|price : {price}")
    total_price += price

print(total_price)