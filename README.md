
# Inventory Management System

A command-line Inventory Management System built using Python.

This project allows users to manage products, track stock quantities, update prices, and calculate inventory statistics through an interactive terminal menu.

## Features

- Add new products with automatically generated IDs.
- Display all products in the inventory.
- Search for products using their IDs.
- Update product prices and quantities.
- Remove products from the inventory.
- Restock existing products.
- Sell products while preventing overselling.
- Calculate inventory statistics:
  - Total number of product types.
  - Total physical units.
  - Total inventory value.
  - Most expensive product.
  - Product with the lowest stock.
  - Products with zero stock.
- Input validation and error handling.

## Technologies

- Python 3
- Dictionaries and nested dictionaries
- Loops and conditional statements
- Functions
- List comprehensions
- Dictionary methods
- Exception handling

## Requirements

- Python 3.8 or newer.

No external libraries are required.

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/inventory-management-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd inventory-management-system
   ```

3. Run the program:

   ```bash
   python inventory.py
   ```

## Example Product Structure

Products are stored using nested dictionaries:

```python
inventory = {
    "P001": {
        "name": "Laptop",
        "price": 15000,
        "quantity": 5
    }
}
```

## Important Note

The inventory is stored in memory using Python dictionaries.

Product information is not saved permanently, so changes are lost when the program closes.

Persistent storage can be added in a future version.

## Future Improvements

- Save inventory data using JSON or a database.
- Add a graphical user interface.
- Generate inventory reports.
- Add transaction history.

