def display_catalog():
    products = {
        1: "Laptop",
        2: "Mobile",
        3: "Headphones",
        4: "Keyboard"
    }

    print("PRODUCT CATALOG")
    for item, name in products.items():
        print(item, "-", name)


display_catalog()