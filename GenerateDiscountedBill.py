price = 500
quantity = 3
total = price * quantity
if total > 1000:
    discount = total * 0.1
else:
    discount = total * 0.05
final = total - discount
print("Total:", total)
print("Discount:", discount)
print("Final Bill:", final)