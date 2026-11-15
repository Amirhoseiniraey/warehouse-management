products = []

while True:
    print("\n1. Show")
    print("2. Add")
    print("3. Delete")
    print("4. Buy")
    print("5. Sell")
    print("6. Low Stock")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        if len(products) == 0:
            print("No products!")

        for product in products:
            print("----------------")
            print("Name:", product["name"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])

    elif choice == "2":

        name = input("Enter product name: ")
        price = int(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        products.append(product)
        print("Product added!")

    elif choice == "3":

        name = input("Enter product name: ")

        for product in products:
            if product["name"] == name:
                products.remove(product)
                print("Product deleted!")
                break
        else:
            print("Product not found!")

    elif choice == "4":

        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        for product in products:
            if product["name"] == name:
                product["quantity"] += quantity
                print("Stock increased!")
                break
        else:
            print("Product not found!")

    elif choice == "5":

        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        for product in products:
            if product["name"] == name:
                if product["quantity"] >= quantity:
                    product["quantity"] -= quantity
                    print("Product sold!")
                else:
                    print("Not enough stock!")
                break
        else:
            print("Product not found!")

    elif choice == "6":

        found = False

        for product in products:
            if product["quantity"] <= 5:
                print(product["name"], product["quantity"])
                found = True

        if found == False:
            print("No low stock products!")

    elif choice == "7":

        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
