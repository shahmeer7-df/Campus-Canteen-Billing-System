
print("===================================")
print("     CAMPUS CANTEEN BILLING")
print("===================================")

print("Menu:")
print("1. Burger       - PKR 300")
print("2. Pizza        - PKR 500")
print("3. Sandwich     - PKR 200")
print("4. Tea          - PKR 100")
print("0. Checkout")

subtotal = 0
total_quantity = 0

while True:
    choice = input("\nSelect an item (0 to checkout): ")

    if choice == "0":
        break

    elif choice == "1":
        item = "Burger"
        price = 300

    elif choice == "2":
        item = "Pizza"
        price = 500

    elif choice == "3":
        item = "Sandwich"
        price = 200

    elif choice == "4":
        item = "Tea"
        price = 100

    else:
        print("Invalid choice! Please select 0 to 4.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        continue

    item_total = price * quantity
    subtotal = subtotal + item_total
    total_quantity = total_quantity + quantity

    print(item, "x", quantity, "=", "PKR", item_total)

print("\n========== FINAL BILL ==========")
print("Total quantity:", total_quantity)
print("Subtotal: PKR", subtotal)

if subtotal >= 1000:
    discount = subtotal * 10 / 100
else:
    discount = 0

final_bill = subtotal - discount

print("Discount: PKR", discount)
print("Final bill: PKR", final_bill)
print("================================")
print("Thank you for visiting!")