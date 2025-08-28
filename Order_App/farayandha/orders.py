from persiantools.digits import to_word
from re import match

order_list = []

def show_menu():
    print("1)Add Order")
    print("2)Show Order")
    print("3)Exit")
    option = input("Enter your choice: ")
    print("----------------------------------------")
    return option

def name_validator(name):
    if match(r"^[a-zA-Z\s\d]{3,30}$",name):
        return True
    else:
        return False

def number_validator(number):
    return number > 0


def get_order():
    name = input("Enter product name: ")
    price = int(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    if name_validator(name) and number_validator(price) and number_validator(quantity):
        product = {
            "product": name,
            "price": price,
            "quantity": quantity,
            "total": price * quantity
        }
        order_list.append(product)
        print("Info : Product added to order")
        return product
    else:
        print("Error : Invalid Data !!!")

def get_total():
    total = 0
    for order in order_list:
        total = total + order['total']
    return total

def show_result():
    for order in order_list:
        print(
            f"{order["product"]:12} {order["price"]:>5} * {order["quantity"]:>3} ==> {order["price"] * order["quantity"]:>8}")
    print("----------------------------------------")
    print(f"Total : {get_total():>24} $")
    print(to_word(get_total()))

__all__ = ['show_menu', 'get_order', 'show_result']