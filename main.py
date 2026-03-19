name=str(input("Enter customer name: "))
item1=str(input("Enter name of item 1: "))
price1=float(input("Enter price of item 1 (KZT): "))
item2=str(input("Enter name of item 2: "))
price2=float(input("Enter price of item 2 (KZT): "))
people=int(input("Enter number of people: "))
subtotal = price1 + price2
tip = subtotal*0.1
total = subtotal + tip
per_person = total / people
print(
    "=" * 30,
    "\n        CAFE BILL\n"+
    "=" * 30,
    "\nCustomer : ", name,
    "\n" + item1 + " : ", price1, "KZT",
    "\n" + item2 + " : ", price2, "KZT",
    "\n" + "-" * 30,
    "\nSubtotal : ", subtotal, "KZT",
    "\nTip (10%) : ", tip, "KZT",
    "\nTotal : ", total, "KZT",
    "\nPer person : ", per_person, "KZT",
    "\n" + "=" * 30)
print("Tip included:", tip > 0)
print("Bill over 5000 KZT:", total > 5000)
# test