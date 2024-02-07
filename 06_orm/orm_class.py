#implement using a class
import sqlite3
connection = sqlite3.connect("ecommerce.db")
cursor = connection.cursor() #allows us to execute sql commands

class Product:
    all = []

    def __init__(self, name, price, id=None):
        self.id = id
        self.name = name
        self.price = price
        Product.all.append(self)

    def save(self):
        sql = f"""
        INSERT INTO products (name, price)
        VALUES (?, ?, ?);
        """
        cursor.execute(sql (None, self.name, self.price))
        connection.commit()

    @classmethod
    def get_product(cls, name):
        sql = f"""
        SELECT * FROM products
        WHERE name = "{name}"
        """
        data = cursor.execute(sql)
        product = data.fetchone()
        if product:
            return Product(product[1], product[2], product[1])
        else:
            return None
        
    @classmethod
    def create_product(cls, name, price):
        sql = f"""
        INSERT INTO products
        VALUES (?, ?, ?);
        """
        cursor.execute(sql, (None, name, price))
        connection.commit()

    

    def update_price(self, new_price):
        self.price = new_price
        sql = f"""
        UPDATE products
        SET price = {new_price}
        WHERE id = {self.id}
        """
        cursor.execute(sql)
        connection.commit()

    def delete(self):
        sql = f"""
        DELETE FROM products
        WHERE name = {self.name}
        """
        cursor.execute(sql)
        connection.commit()

if __name__ == "__main__":
    def view_product():
        input2 = input("Enter a product name: ")
        product = Product.get_product(input2)
        if product:
            # print(product.id, product.name, product.price)
            print("Product found: ", product.name, product.price)
        else:
            print("Product not found")

    def create_product():
        name = input("Enter a product name: ")
        price = input("Enter a product price: ")
        Product.create_product(name, price)
        print("Product created!")

    def update_product():
        input3 = input("Enter a product name to update: ")
        product = Product.get_product(input3)
        if product:
            new_price = input("Enter new price: ")
            product.update_price(new_price)
            print("Product updated!")
        else:
            print("Product not found")

    def delete_product():
        input4 = input("Enter a product name to delete: ")
        product = Product.get_product(input4)
        if product:
            product.delete()
            print("Product deleted!")
        else:
            print("Product not found")

    while True:
        user_input = input("Create, View, Update or Delete a product? (Enter quit to exit) ")

        if user_input.lower() == "view":
            view_product()
        elif user_input.lower() == "create":
            create_product()
        elif user_input.lower() == "update":
            update_product()
        elif user_input.lower() == "delete":
            delete_product()
        elif user_input.lower() == "quit":
            print("Exiting...")
            break
        else:
            print("Invalid input")

        
    

    

    
