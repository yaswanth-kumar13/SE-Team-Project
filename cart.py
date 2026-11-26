def display_cart():
    cart = {
        "Laptop": 1,
        "Mobile": 2,
        "Headphones": 1
    }

    print("SHOPPING CART")
    for item, quantity in cart.items():
        print(item, "-", quantity)

    print("Cart updated successfully")


display_cart()