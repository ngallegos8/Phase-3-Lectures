#First import sqlite3
import sqlite3

#Connect to the database using sqlite3.connect('')
connection = sqlite3.connect("ecommerce.db")

#Create a cursor class object using .cursor()
#This allows you to execute sql commands, using .execute()
#Cursor Reading: https://www.tutorialspoint.com/python_data_access/python_sqlite_cursor_object.htm#:~:text=The%20sqlite3.,of%20the%20Connection%20object%2Fclass
cursor = connection.cursor()

sql_command = """
SELECT products.name, customers.name
FROM orders
JOIN products ON orders.product_id = products.id
JOIN customers ON orders.customer_id = customers.id
"""

cursor.execute(sql_command)
# data = cursor.fetchall() #fetches all rows of a query result set
# print(data)
data1 = cursor.fetchone()  #fetches the next row of a query result set
print(data1)

while True:
    print("Menu\n:")
    print("1. Add a product")
    print("2. View Products")
    print("3. Update product price")
    print("4. Delete product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        sql_command_insert = f"""
            INSERT INTO products (name, price)
        VALUES ('{name}', {price});
        """
        cursor.execute(sql_command_insert)
        connection.commit()
        print("Product added successfully")

    elif choice == "2":
        sql_command_select = """
        SELECT * FROM products
        """
        cursor.execute(sql_command_select)
        data = cursor.fetchall()
        print("Products: ")
        for row in data:
            print(row)

    elif choice == "3":
        product_id = int(input("Enter a product id: "))
        new_price = float(input("Enter new price: "))
        sql_command_update = f"""
        UPDATE products
        SET price = {new_price}
        WHERE id = {product_id}
        """
        cursor.execute(sql_command_update)
        connection.commit()
        print("Price updated successfully")
        
    elif choice == "4":
        product_id = int(input("Enter product id to delete: "))
        sql_command_delete = f"""
        DELETE FROM products
        WHERE id = {product_id}
        """
        cursor.execute(sql_command_delete)
        connection.commit()
        print("Product deleted successfully")

    elif choice == "5":
        print("Exiting...")
        break

    else: 
        print("Invalid choice")
