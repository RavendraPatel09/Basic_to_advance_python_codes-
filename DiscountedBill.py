amount = 1200
if amount > 1000:
    discount = amount * 0.1
else:
    discount = amount * 0.05
bill = amount - discount
print("Final Bill:", bill)