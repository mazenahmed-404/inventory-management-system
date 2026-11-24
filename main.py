
def main():
    inventory = {
        "P001": {"name": "Laptop", "price": 15000, "quantity": 5},
        "P002": {"name": "Mouse", "price": 500, "quantity": 20}
    }

    while True:
        print("\n========== INVENTORY SYSTEM ==========")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Remove Product")
        print("6. Restock Product")
        print("7. Sell Product")
        print("8. Inventory Statistics")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_product(inventory)

        elif choice == "2":
            display(inventory)

        elif choice == "3":
            search(inventory)

        elif choice == "4":
            while True:
                print("\n1. Update price")
                print("2. Update quantity")

                sub = input("Choose an option: ")

                if sub == "1":
                    update_price(inventory)
                    break
                elif sub == "2":
                    update_quantity(inventory)
                    break
                else:
                    print("Choose a valid option!")

        elif choice == "5":
            delete_product(inventory)

        elif choice == "6":
            restock(inventory)

        elif choice == "7":
            sell(inventory)

        elif choice == "8":
            stat(inventory)

        elif choice == "9":
            print("Thank you for using the Inventory System!")
            break

        else:
            print("Enter a valid choice!")


# Adding a product
def add_product(data):
    if data:
        existing_numbers = [
            int(product_id[1:]) for product_id in data
        ]
        next_num = max(existing_numbers) + 1
        new_id = f"P{next_num:03d}"
    else:
        new_id = "P001"

    name = input("Enter the product's name: ").strip()

    while not name:
        print("Product name cannot be empty!")
        name = input("Enter the product's name: ").strip()

    while True:
        try:
            price = float(input("Enter the product's price: "))

            if price > 0:
                break
            else:
                print("Enter a positive price!")

        except ValueError:
            print("Enter a valid price!")

    while True:
        try:
            quantity = int(input("Enter the product's quantity: "))

            if quantity >= 0:
                break
            else:
                print("Quantity cannot be negative!")

        except ValueError:
            print("Enter a valid quantity!")

    data[new_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    print(f"Product added successfully! Product ID: {new_id}")


# Displaying all products
def display(data):
    if not data:
        print("The inventory is empty.")
        return

    print("\n========== INVENTORY ==========")

    for product_id, item in data.items():
        print(f"\nProduct ID: {product_id}")
        print(f"Name: {item['name']}")
        print(f"Price: {item['price']}")
        print(f"Quantity: {item['quantity']}")


# Searching for a product
def search(data):
    product = input("Enter the product ID: ").strip().upper()

    if product in data:
        print("\nProduct found!")
        print(f"ID: {product}")
        print(f"Name: {data[product]['name']}")
        print(f"Price: {data[product]['price']}")
        print(f"Quantity: {data[product]['quantity']}")
    else:
        print("Product not found!")


# Updating product price
def update_price(data):
    product = input("Enter the product ID: ").strip().upper()

    if product not in data:
        print("Product ID not found!")
        return

    while True:
        try:
            new_price = float(input("Enter the new price: "))

            if new_price > 0:
                break
            else:
                print("Enter a positive price!")

        except ValueError:
            print("Enter a valid price!")

    data[product]["price"] = new_price
    print("Product price updated successfully!")


# Updating product quantity
def update_quantity(data):
    product = input("Enter the product ID: ").strip().upper()

    if product not in data:
        print("Product ID not found!")
        return

    while True:
        try:
            new_quantity = int(input("Enter the new quantity: "))

            if new_quantity >= 0:
                break
            else:
                print("Quantity cannot be negative!")

        except ValueError:
            print("Enter a valid quantity!")

    data[product]["quantity"] = new_quantity
    print("Product quantity updated successfully!")


# Deleting a product
def delete_product(data):
    product = input("Enter the product ID to delete: ").strip().upper()

    removed = data.pop(product, None)

    if removed is not None:
        print("Product deleted successfully!")
    else:
        print("Product ID not found!")


# Restocking a product
def restock(data):
    product = input("Enter the product ID: ").strip().upper()

    if product not in data:
        print("Product not found!")
        return

    while True:
        try:
            num = int(input("Enter the number of units to add: "))

            if num > 0:
                break
            else:
                print("Enter a positive number!")

        except ValueError:
            print("Enter a valid positive number!")

    data[product]["quantity"] += num

    print(f"Successfully restocked {num} units!")


# Selling a product
def sell(data):
    product = input("Enter the product ID: ").strip().upper()

    if product not in data:
        print("Product not found!")
        return

    available = data[product]["quantity"]

    if available == 0:
        print("No available items.")
        return

    while True:
        try:
            num = int(input("Enter the number of units to sell: "))

            if num <= 0:
                print("Enter a positive number!")

            elif num > available:
                print(f"You only have {available} available items!")

            else:
                break

        except ValueError:
            print("Enter a valid positive number!")

    data[product]["quantity"] -= num

    print(f"Successfully sold {num} units!")


# Inventory statistics
def stat(data):
    if not data:
        print("The inventory is empty. No statistics available.")
        return

    # Total product types
    count = len(data)
    print(f"\nTotal number of product types: {count}")

    # Total physical units
    total_units = sum(
        item["quantity"] for item in data.values()
    )
    print(f"Total number of units: {total_units}")

    # Total inventory value
    total_value = sum(
        item["price"] * item["quantity"]
        for item in data.values()
    )
    print(f"Total inventory value: {total_value:.2f}")

    # Most expensive product(s)
    maximum = max(
        item["price"] for item in data.values()
    )

    expensive_products = [
        item["name"]
        for item in data.values()
        if item["price"] == maximum
    ]

    print(f"Most expensive product(s): {expensive_products} ({maximum})")

    # Product(s) with the lowest stock
    lowest = min(
        item["quantity"] for item in data.values()
    )

    lowest_stock_products = [
        item["name"]
        for item in data.values()
        if item["quantity"] == lowest
    ]

    print(f"Lowest-stock product(s): {lowest_stock_products} ({lowest})")

    # Products with zero stock
    zero_stocks = [
        item["name"]
        for item in data.values()
        if item["quantity"] == 0
    ]

    if zero_stocks:
        print(f"Products with zero stock: {zero_stocks}")
    else:
        print("There are no products with zero stock.")


main()
