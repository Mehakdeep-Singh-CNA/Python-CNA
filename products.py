import mysql.connector
from config import db_config


# Set up the database connection
def create_connection():
    """Creates a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print('Connected to MySQL database')
            return connection
    except Error as e:
        print(f'Error connecting to MySQL database: {e}')
        return None


# Create a cursor object to interact with the database
cursor = create_connection().cursor()


# Define the Product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def save(self):
        # Save the product to the database
        sql = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
        values = (self.name, self.price, self.quantity)
        cursor.execute(sql, values)
        db.commit()
    
    def update(self):
        # Update the product in the database
        sql = "UPDATE products SET price = %s, quantity = %s WHERE name = %s"
        values = (self.price, self.quantity, self.name)
        cursor.execute(sql, values)
        db.commit()
    
    def delete(self):
        # Delete the product from the database
        sql = "DELETE FROM products WHERE name = %s"
        values = (self.name,)
        cursor.execute(sql, values)
        db.commit()

# Define a function to display the inventory
def display_inventory():
    # Select all products from the database
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    # Display each product in the inventory
    print("Current Inventory:")
    print("-------------------")
    for product in products:
        print(f"{product[0]} - {product[1]} - ${product[2]:.2f} - {product[3]} in stock")
    print()

# Define a function to add a new product to the inventory
def add_product():
    name = input("Enter the name of the new product: ")
    price = float(input("Enter the price of the new product: "))
    quantity = int(input("Enter the quantity of the new product: "))
    product = Product(name, price, quantity)
    product.save()
    print(f"{name} has been added to the inventory.")
    print()

# Define a function to update an existing product in the inventory
def update_product():
    name = input("Enter the name of the product to update: ")
    price = float(input("Enter the new price of the product: "))
    quantity = int(input("Enter the new quantity of the product: "))
    product = Product(name, price, quantity)
    product.update()
    print(f"{name} has been updated in the inventory.")
    print()

# Define a function to delete a product from the inventory
def delete_product():
    name = input("Enter the name of the product to delete: ")
    product = Product(name, 0, 0)
    product.delete()
    print(f"{name} has been deleted from the inventory.")
    print()

# Define the main function to run the application
def main():
    
    # Display the current inventory
    display_inventory()

    # Loop to prompt the user for an action
    while True:
        action = input("What would you like to do? (add/update/delete/quit): ")
        if action == "add":
            add_product()
            display_inventory()
        elif action == "update":
            update_product()
            display_inventory()
        elif action == "delete":
            delete_product()
            display_inventory()
        elif action == "quit":
            print

if __name__ == '__main__':
    main()            
