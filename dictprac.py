invantory = {
    "apples":50 ,
    "bananas" :12,
    "oranges" :30,
    "mangoes" :8
}

invantory["grapes"]=25
invantory["bananas"]= 20
for fruits , quantity in invantory.items():
    if quantity <= 15:
        print(f"low stock : {fruits} - {quantity} left in quantity")

invantory.pop("oranges")
print(invantory)

invantory.get("peaches")
if invantory.get("peaches") == None:
    print(" peaches are not in stock")