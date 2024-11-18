# Product 1
product_object1 = {
    "ID": 1,
    "Name": "Laptop",
    "Category": "Electronics",
    "Price": 750,
    "Stock": 50,
    "Supplier Email": "supplier1@gmail.com"
}

# Product 2
product_object2 = {
    "ID": 2,
    "Name": "Desk Chair",
    "Category": "Furniture",
    "Price": 100,
    "Stock": 200,
    "Supplier Email": "supplier2@gmail.com"
}

# Product 3
product_object3 = {
    "ID": 3,
    "Name": "Smartwatch",
    "Category": "Electronics",
    "Price": 200,
    "Stock": 150,
    "Supplier Email": "supplier3@gmail.com"
}

# Product 4
product_object4 = {
    "ID": 4,
    "Name": "Notebook",
    "Category": "Stationery",
    "Price": 55,
    "Stock": 0,
    "Supplier Email": "supplier4@gmail.com"
}

# Product 5
product_object5 = {
    "ID": 5,
    "Name": "Running Shoes",
    "Category": "Apparel",
    "Price": 80,
    "Stock": 100,
    "Supplier Email": "supplier5@gmail.com"
}

# List of Products
products = [product_object1, product_object2, product_object3, product_object4, product_object5]

# Iterate through the list of products and print details
for product in products:
    print(f"ID: {product['ID']}, Name: {product['Name']}, Category: {product['Category']}, "
          f"Price: {product['Price']}, Stock: {product['Stock']}, Supplier Email: {product['Supplier Email']}")
