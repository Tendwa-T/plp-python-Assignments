

def calculate_discount(price, discount):
    if discount >= 0.2:
        return price*discount
    return price


itemPriceInput = input("Enter item price: ")
itemPrice = int(itemPriceInput)

itemDiscountInput = input("Enter item discount in decimal: ")
itemDiscount = float(itemDiscountInput)
print(calculate_discount(itemPrice, itemDiscount))