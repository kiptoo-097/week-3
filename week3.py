def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


original_price = int(input('Enter the price:'))
discount_percentage = int(input('Enter discount percentage:'))
final_price = calculate_discount(original_price, discount_percentage)
print("Final price after discount:", final_price)
